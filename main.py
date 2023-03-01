from fastapi import FastAPI
from routes.courses_routes import course_api_router

app = FastAPI()

app.include_router(course_api_router)