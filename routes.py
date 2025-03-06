from fastapi import APIRouter, HTTPException
from user import User
from datetime import datetime
import random
import config

router = APIRouter()

def id_generator():
    generated_id = random.randint(1, 100)
    return generated_id

def valid_data(user: dict):
    if "name" not in user or "family" not in user or "email_adress" not in user:
        raise HTTPException(status_code=400, detail="something missing")



users_db = {}

@router.get("/users/all")
def get_all_user():
    return config.get_all_user() 
   
@router.get("/users/{id}")
def get_user(id: int):
    return config.get_user_id(id)

@router.post("/users")
def create_user(user: dict):
    current_id = id_generator()
    date_now = str(datetime.now())
    valid_data(user)
    user = User(id = current_id, name = user["name"], family = user["family"], email_adress = user["email_adress"], created_date = date_now, updated_date = date_now)
    users_db[current_id] = user
    config.insert_user(user)
    return user
    
@router.delete("/users/{id}")
def delete_user(user_id: int):
    return config.delete_user(user_id)

@router.put("/users/{id}")
def update_user(user: dict, user_id: int):
    updated_time = str(datetime.now())
    valid_data(user)
    return config.update_user_by_id(name = user["name"], family = user["family"], email = user["email_adress"],user_id=user_id)

