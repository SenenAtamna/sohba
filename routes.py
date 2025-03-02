from fastapi import APIRouter, HTTPException
from user import User
from datetime import datetime
import random


router = APIRouter()

def id_generator():
    generated_id = random.randint(1, 100)
    return generated_id

def valid_data(user: dict):
    if "name" not in user or "family" not in user or "email_adress" not in user:
        raise HTTPException(status_code=400, detail="something missing")

def user_check(id):
    if id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

users_db = {}

@router.get("/users/all")
def get_all_user():
    return users_db




@router.get("/users/{id}")
def get_user(id: int):
    user_check(id)
    return users_db[id]

@router.post("/users")
def create_user(user: dict):
    current_id = id_generator()
    date_now = str(datetime.now())
    valid_data(user)
    user = User(id = current_id, name = user["name"], family = user["family"], email_adress = user["email_adress"], created_date = date_now)
    users_db[current_id] = user
    return user
    
@router.delete("/users/{id}")
def delete_user(user_id: int):
    user_check(id)
    del users_db[user_id]
    return {"message": "user deleted successfully"}

@router.put("/users/{id}")
def update_user(user: dict, user_id: int):
    user_check(user_id)
    created_date = users_db[user_id].created_date
    updated_time = str(datetime.now())
    valid_data(user)
    user = User(id = user_id, name = user["name"], family = user["family"], email_adress = user["email_adress"],created_date = created_date, updated_date = updated_time)
    users_db[user_id] = user
    return user