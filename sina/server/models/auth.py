from beanie import Document
from pydantic import BaseModel

class User(Document):
    username: str 
    password: str 

class Token(BaseModel):
    access_token :str
    token_type :str


class TokenData(BaseModel):
    usernames : str or None = None 


class User(Document):
    username :str 
    password: str

    @classmethod
    def find_user(cls, username):
        return cls.find_one(
            {"username": username}
        )
    
    class Config:
        json_schema_extra = {
            'example': {
                'username':'922tech',
                'password':'1234'
            }
        }
    

class UserCreate(User):
    username: str
    password: str


class UserInDB(User):
    password :str
