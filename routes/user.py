from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from config.db import db
from schemas.user import users_entity, user_entity
from models.user import User, ListUser
from bson import ObjectId
from pydantic import BaseModel


user = APIRouter()


class Response_Default(BaseModel):
    sucess: bool
    message: str


class Reponse_Created_User(Response_Default):
    id: str


@user.get("/users", response_model=ListUser)
def find_all_users():
    return JSONResponse(content=users_entity(db.user.find()), status_code=status.HTTP_208_ALREADY_REPORTED)


@user.get("/users/{id}", response_model=User)
def find_user(id: str):
    try:
        return user_entity(db.user.find_one({"_id": ObjectId(id)}))
    except Exception as error:
        if error.__cause__ == None:
            return JSONResponse(content={"success": False,"message": f"The user_id {id}, not found"}, status_code=status.HTTP_404_NOT_FOUND)


@user.post("/users", response_model=Reponse_Created_User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    try:
        new_user = dict(user)

        id = db.user.insert_one(new_user).inserted_id

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"sucess": True, "message": "user created successfully", "user_id": str(id)},
        )
    except Exception as error:
        print(error.__cause__)


@user.put("/users/{id}", response_model=Response_Default)
def update_user(id: str, user: User):
    db.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})

    return {"sucess": True, "message": "user successfully deleted"}


@user.delete("/users/{id}", response_model=Response_Default)
def delete_user(id: str):
    db.user.find_one_and_delete({"_id": ObjectId(id)})

    return JSONResponse(content={"sucess": True, "message": "user successfully deleted"}
    )
