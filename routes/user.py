from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from config.db import db
from schemas.user import users_entity, user_entity
from models.user import User
from bson import ObjectId
from pydantic import BaseModel


user = APIRouter()


class Response_Default(BaseModel):
    sucess: bool
    message: str


class Reponse_Created_User(Response_Default):
    id: str


@user.get("/users", response_model=list[User], tags=["Users"])
def find_all_users():
    return JSONResponse(content=users_entity(db.user.find()), status_code=status.HTTP_208_ALREADY_REPORTED)


@user.get("/users/{id}", response_model=User, tags=["Users"])
def find_user(id: str):
    return user_entity(db.user.find_one({"_id": ObjectId(id)}))


@user.post("/users", response_model=Reponse_Created_User, tags=["Users"])
def create_user(user: User):
    new_user = dict(user)

    id = db.user.insert_one(new_user).inserted_id

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"sucess": True, "message": "user created successfully", "user_id": str(id)},
    )


@user.put("/users/{id}", response_model=Response_Default, tags=["Users"])
def update_user(id: str, user: User):
    db.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

    return {"sucess": True, "message": "user successfully deleted"}


@user.delete("/users/{id}", response_model=Response_Default, tags=["Users"])
def delete_user(id: str):
    db.user.find_one_and_delete({"_id": ObjectId(id)})

    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content={"sucess": True, "message": "user successfully deleted"}
    )
