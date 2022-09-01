
from fastapi import FastAPI
from routes.user import user

app = FastAPI()

app.get('/', tags=["start"])
def home():
    return "Wellcome"

app.include_router(user, prefix="/v1/dasboard", tags=["Users"])
