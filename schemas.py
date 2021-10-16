from pydantic import BaseModel
from typing import List, Optional


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


"""LOGIN SCHEMAS"""
class Login(BaseModel):
    username: str
    password: str



"""TOKEN SCHEMAS"""
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


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