def course_serializer(course) -> dict:
    return {
        "id": str(course["_id"]),
        "course_code": course["course_code"],
        "course_name": course["course_name"],
        "year": course["year"],
        "group": course["group"],
        "number": course["number"],
    }

def courses_serializers(courses) -> list:
    return [course_serializer(course) for course in courses]