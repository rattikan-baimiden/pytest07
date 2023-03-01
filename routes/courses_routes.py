from fastapi import APIRouter

from models.courses_model import Course
from config.database import collection_name

from schemas.courses_schema import courses_serializers, course_serializer
from bson import ObjectId

course_api_router = APIRouter()

@course_api_router.get("/hello")
async def get_hello():
    return {"msg":"Hello World"}

# retrieve
@course_api_router.get("/")
async def get_courses():
    courses = courses_serializers(collection_name.find())
    return courses

@course_api_router.get("/{id}")
async def get_course(id: str):
    # return {"test": id}
    return course_serializer(collection_name.find_one({"_id": ObjectId(id)}))


# post
@course_api_router.post("/")
async def create_course(course: Course):
    _id = collection_name.insert_one(dict(course))
    return courses_serializers(collection_name.find({"_id": _id.inserted_id}))


# update
@course_api_router.put("/{id}")
async def update_course(id: str, course: Course):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(course)
    })
    return courses_serializers(collection_name.find({"_id": ObjectId(id)}))

# delete
@course_api_router.delete("/{id}")
async def delete_course(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}