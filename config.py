from datetime import datetime
import psycopg2
from user import User

conn_details = {
    'dbname': 'sohba',  
    'user': 'admin',      
    'password': 'secret', 
    'host': 'localhost',     
    'port': '5432'          
}

#test_connect

try:
    conn = psycopg2.connect(**conn_details)
    print("connect succes")
except Exception as e:
    print(f"not success: {e}")

def insert_user(user: User):
    with conn.cursor() as cursor:
        insert_query = '''
            INSERT INTO "public"."user" (id, name, family, email, created_date, updated_date)
            VALUES (%s, %s, %s, %s, %s, %s);
            '''
        data = (user.id, user.name, user.family, user.email_adress, user.created_date, user.updated_date)
        cursor.execute(insert_query, data)
        conn.commit()
        print("INSERTED SUCCESSFULLY")    

def get_all_user():
    with conn.cursor() as cursor:
        select_query = ''' SELECT * FROM "public"."user" '''
        cursor.execute(select_query)
        records = cursor.fetchall()
        list_of_users = {}
        for row in records:
            user = User(id = row[0], name = row[1], family = row[2], email_adress = row[3], created_date = row[4], updated_date = row[5])
            list_of_users[row[0]] = user
        return list_of_users

def get_user_id(user_id):
    with conn.cursor() as cursor:
        select_query = '''SELECT * FROM "public"."user" WHERE id = %s;'''
        cursor.execute(select_query, (user_id,))
        row = cursor.fetchone()
        print (row)
        if row:
            user =  User(id = row[0], name = row[1], family = row[2], email_adress = row[3], created_date = row[4], updated_date = row[5])
            return user
        else:
            return "No User Found"

def delete_user(id):
    with conn.cursor() as cursor:
        try: 
            delete_query = '''DELETE FROM "public"."user" WHERE id = %s;'''
            cursor.execute(delete_query, (id,))
            conn.commit()
            return "user Id: " + str(id) + "deleted succesfully"     
        except Exception as e:
            return "somthing wrong: " + str(e)  

def update_user_by_id(user_id, name, family, email):
    with conn.cursor() as cursor:
        select_query = '''SELECT * FROM "public"."user" WHERE id = %s;'''
        cursor.execute(select_query, (user_id,))
        row = cursor.fetchone()
        if row:
            update_query = '''
                UPDATE "public"."user"
                SET name = %s, family = %s, email = %s, updated_date = %s
                WHERE id = %s;
            '''
            updated_date = datetime.now()
            data = (name, family, email, updated_date, user_id)
            cursor.execute(update_query, data)
            conn.commit()
            return "updated successfully" + str(user_id)
        else:
            return "No User Found" + str(user_id) 
