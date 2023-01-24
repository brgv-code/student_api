# create a fastapi get request to get the data from the database
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schemas.student import Student
from config.db import con
from models.students import students

app = FastAPI()


# @app.get("/api/students")
# async def get_students():
#     return JSONResponse(content={"name": "John", "age": 30})
# get the data from the database students and return it as a json response
@app.get("/api/students")
async def get_students():
    data = con.execute(students.select()).fetchall()
    # return data.fetchall()
    return {
        "status": "success",
        "data": data
    }


# insert data into the database


@app.post("/api/students")
async def create_student(student: Student):
    data = con.execute(students.insert().values(
        name=student.name, age=student.age, email=student.email, country=student.country))
    if data.is_insert:
        return JSONResponse(content={"message": "Student created successfully"})
    else:
        return JSONResponse(content={"message": "Error creating student"})

# edit data in the database


@app.put("/api/students/{id}")
async def update_student(id: int):
    data = con.execute(students.select().where(students.c.id == id)).fetchall()
    return {"data": data}

#update data in the database

@app.patch("/api/students/{id}")
async def update_student(id: int, student: Student):
    data = con.execute(students.update().where(students.c.id == id).values(
        name=student.name, age=student.age, email=student.email, country=student.country))
    if data:
        return JSONResponse(content={"message": "Student updated successfully"})
    else:
        return JSONResponse(content={"message": "Error updating student"})
#delete data from the database
@app.delete("/api/students/{id}")
async def delete_student(id: int):
    data = con.execute(students.delete().where(students.c.id == id))
    if data:
        return JSONResponse(content={"message": "Student deleted successfully"})
    else:
        return JSONResponse(content={"message": "Error deleting student"})
    
#search data from the database
@app.get("/api/students/{id}")
async def search_student(id: int):
    data = con.execute(students.select().where(students.c.id == id)).fetchall()
    if data:
        return {"status": "Student found successfully", "data": data}
    else:
        return JSONResponse(content={"message": "Student not found"})