from pydantic import BaseModel, EmailStr, Field

class Student(BaseModel):
    name : str
    age : int
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10)

new_student = {'name' : 'Jags', 'age': '32', 'email': 'abc@gmail.com', 'cgpa': 9}

student = Student(**new_student)

print(student)