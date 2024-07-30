from pydantic import BaseModel
from datetime import date

class StudentDataTypeIn(BaseModel):
  name: str
  dob: date

class StudentDataType(BaseModel):
  id: int
  name: str
  dob: date