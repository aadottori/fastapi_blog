from pydantic import BaseModel
from typing import List


"""BLOG SCHEMAS"""
class BlogBase(BaseModel):
    title: str
    body: str
    user_id: int

class Blog(BlogBase):
    class Config():
        orm_mode = True


"""USER SCHEMAS"""
class User(BaseModel):
    name: str
    email: str
    password: str


"""SHOW SCHEMAS"""
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    class Config():
        orm_mode = True


class ShowBlog(Blog):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode = True