import uvicorn
import employee.EmployeeApi as emp
from typing import List, Union
from fastapi import FastAPI, HTTPException, Path, Query, Body
from fastapi.responses import FileResponse, HTMLResponse
from models.ErrorModel import ErrorModel
from models.employee import Employee
from repo.employee_repo import EmployeeRepo


description = "Just for learning CURD oprations using SQL Server and Python"
app = FastAPI(title="Employee Management", description = description)
app.include_router(emp.employeeApi)

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/", response_class=HTMLResponse)
def home():
    HTMLResponse("")
    return """
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta http-equiv="X-UA-Compatible" content="IE=edge">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Employee Management</title>
                </head>
                <body>
                    <h1>Welcome!</h1>
                    <p>Click <a href="/docs">here</a> for API documentation</p>
                </body>
            </html>
    """