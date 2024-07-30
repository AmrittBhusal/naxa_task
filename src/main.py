from fastapi  import FastAPI
from tortoise import generate_config,Tortoise
from tortoise.contrib.fastapi import register_tortoise

from src.database.models import Student
from src.schema import StudentDataType,StudentDataTypeIn
from src.database.config import TORTOISE_ORM   
from typing import List 


Tortoise.init_models(["src.database.models"], "models")


app=FastAPI()

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=True)

@app.post("/createstudent",response_model=StudentDataType)
async def create_students(data:StudentDataTypeIn):
    data_dict = data.dict()
    student_data = await Student.create(**data_dict)
    return {
        "id": student_data.id,
        "name": student_data.name,
        "dob" : student_data.dob
    }
    
@app.get("/readstudent",response_model=List[StudentDataType])
async def read_student():
    students= await Student.all()
    return students



@app.get("/readstudent/{id}",response_model=List[StudentDataType])
async def read_student(id:int):
    students= await Student.filter(id=id)
    return students
    
