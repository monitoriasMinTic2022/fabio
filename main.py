from fastapi import FastAPI
from models.user import User
from db.user_db import set_user, database_users

api = FastAPI()


@api.post("/users")
def saveUser(user: User):
    set_user(user)
    return database_users
    