from fastapi import FastAPI
from pydantic import BaseModel
from main import app


app = FastAPI()

fakedb = []

class Course(BaseModel):
    id: int
    name: str
    price: float
    is_early_bird: bool = None
    

@app.get("/")
async def root():
    return {"mssg":"welcome to codingMania"}

@app.get("/courses")
async def get_courses():
    return fakedb

@app.post("/courses")
async def add_courses(course: Course):
    # if fakedb["id"] == course.id:
     fakedb.append(course.dict())
     return fakedb[-1]
 
@app.get("/courses/{course_id}")
async def get_a_course(course_id: int):
    course = course_id 
    return fakedb[course]



@app.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    fakedb.pop(course_id )
    return {"mssg":"deleted successfully"}

