from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import Gender, User, Role, UserUpdateRequest

from models import User

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("fcbe1b9f-40b9-49bf-bed8-dc3fecf26f5e"),
        first_name="Bob",
        last_name="Smith",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    ),
    User(
        id=UUID("2705bc43-8514-4070-b07a-31f85fe0cf7e"),
        first_name="Jennifer",
        last_name="Smith",
        gender=Gender.female,
        roles=[Role.user]
    ),
    User(
        id=UUID("7f4956b1-a9f1-4659-b22e-c6aaeaf48257"),
        first_name="John",
        last_name="Jones",
        gender=Gender.male,
        roles=[Role.student]
    )
]

@app.get("/")
async def root():
    return {"Hello": "Jay"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist."
        )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user_id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.role is not None:
                user.roles = user_update.roles
            return
        raise HTTPException(
            status_code=404,
            detail=f"user with id: {user_id} does not exist."
        )