from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

@app.get("/")

def index():
    return {"message": "Hello World"}


@app.get("/about")

def about():
    return {"message": "About"}

@app.get("/users/{id}")

def user(id: int, limit: Optional[int] = None):
    if limit is None:
        return {"message": f"User {id}"}
    else:
        return {"message": f"User {id} with limit {limit}"}


class Request(BaseModel):
    name: str
    age: int
    email: str
@app.post("/")

def index(request: Request):
    return {"data":request}