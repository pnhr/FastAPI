import uvicorn
from typing import Union
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from ErrorModel import ErrorModel
from employee import Employee
from employee_repo import EmployeeRepo

app = FastAPI()

favicon_path = "favicon.ico"

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse(favicon_path)

@app.get("/")
def get():
    try:
        repo = EmployeeRepo()
        empList = repo.get_employees()
        return empList
    except Exception as e:
        return ErrorModel(e)



@app.get("/getbyid/{emp_id}")
def get(emp_id:int):
    try:
        repo = EmployeeRepo()
        emp = repo.get_employee_by_id(emp_id)

        if emp != None:
            return emp
        
        raise HTTPException(status_code=404, detail="employee not found")
    except HTTPException:
        raise
    except Exception as e:
        return ErrorModel(str(e.args[0]))
    


@app.post("/save")
def save_employee(employee: Employee):
    try:
        repo = EmployeeRepo()
        is_added = repo.add_employee(employee)

        if is_added:
            return repo.empList
        
        raise HTTPException(status_code=500, detail="Error occured while adding employee!")
    except HTTPException:
        raise
    except Exception as e:
        return ErrorModel(e)



@app.put("/update")
def update_employee(employee: Employee):
    try:
        repo = EmployeeRepo()
        is_updated = repo.update_employee(employee)
        
        if is_updated:
            return repo.empList
        
        raise HTTPException(status_code=404, detail="employee not found")
    except HTTPException:
        raise
    except Exception as e:
        return ErrorModel(e)

@app.delete("/delete")
def delete_employee(emp_id:int):
    try:
        repo = EmployeeRepo()
        is_deleted = repo.delete_employee(emp_id)
        return repo.empList
    except Exception as e:
        return ErrorModel(e)