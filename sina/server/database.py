"""
This app uses MongoDB as the database engine.
To make use of Template design pattern for transactions 'beanie'
library has been exploited which provides a robust object document
mapper 
"""

from beanie import init_beanie
import motor.motor_asyncio
from server.models.instagram import LoginCookie
from server.models.auth import User
from server.settings import DATABASE
 
async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        DATABASE['URL']
    )
    db = client[DATABASE['NAME']]
    await init_beanie(database=db, document_models=[LoginCookie, User])
    