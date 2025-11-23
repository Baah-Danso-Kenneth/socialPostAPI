from . import models
from fastapi import FastAPI
from pydantic import BaseModel
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


class Post(BaseModel):
    title: str
    body: str


@app.get('/')
def root():
    return {"message": "hello world"}

@app.post('/create')
def create_post(post: Post):
    new_post = f"the {post.title} and its content {post.body}"
    return new_post