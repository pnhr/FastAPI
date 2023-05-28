import uvicorn
from typing import List, Union
from fastapi import APIRouter, HTTPException, Path, Query, Body
from fastapi.responses import FileResponse
from models.ErrorModel import ErrorModel
from models.employee import Employee
from repo.employee_repo import EmployeeRepo

description = "Just for learning CURD oprations using SQL Server and Python"
employeeApi = APIRouter(prefix="/employee")

@employeeApi.get("/", description="Fetches all active employees from the system")
def get():
    try:
        repo = EmployeeRepo()
        empList = repo.get_employees()
        return list(empList)
    except Exception as e:
        return ErrorModel(str(e))



@employeeApi.get("/getbyid/{emp_id}", description="Fetches an active employees whose employee id matches with the given id")
def get(emp_id:int = Path(title="Employee Id", description="Please send a valid employee id")):
    try:
        repo = EmployeeRepo()
        emp = repo.get_employee_by_id(emp_id)

        if emp != None:
            return emp
        
        raise HTTPException(status_code=404, detail="employee not found")
    except HTTPException:
        raise
    except Exception as e:
        return ErrorModel(str(e))
    

@employeeApi.post("/create", description="Creates an employee in the system")
def create_employee(employee: Employee):
    try:
        repo = EmployeeRepo()
        is_added = repo.add_employee(employee)

        if is_added:
            return repo.get_employees()
        
        raise HTTPException(status_code=500, detail="Error occured while adding employee!")
    except HTTPException:
        raise
    except Exception as e:
        return ErrorModel(str(e))



@employeeApi.put("/update", description="Updates an employee whos employee id matches with the given employee id in the system")
def update_employee(employee: Employee):
    try:
        repo = EmployeeRepo()
        is_updated = repo.update_employee(employee)
        
        if is_updated:
            return repo.get_employees()
        
        raise HTTPException(status_code=404, detail="employee not found")
    except HTTPException:
        raise
    except Exception as e:
        return ErrorModel(str(e))
    


@employeeApi.delete("/delete", description="Inactivates an employee whos employee id matches with the given employee id in the system")
def delete_employee(emp_id:int):
    try:
        repo = EmployeeRepo()
        is_deleted = repo.delete_employee(emp_id)
        return repo.get_employees()
    except Exception as e:
        return ErrorModel(str(e))