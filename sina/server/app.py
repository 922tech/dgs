from fastapi import FastAPI
from server.routes.login import router as login_router
from server.routes.instagram import router as instagram_router
from server.database import init_db

app = FastAPI()
app.include_router(login_router)
app.include_router(instagram_router)


@app.on_event("startup")
async def start_db() -> dict:
    await init_db()


@app.get("/", tags=["Root"])
async def index() -> dict:
    return {"message": "Welcome to app!"}





'https://medium.com/@gurramakhileshwar333/get-your-beanies-a-beginners-guide-to-beanie-mongodb-odm-for-python-b715c3f59a92'