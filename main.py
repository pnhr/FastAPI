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
    <link rel="icon" href="/images/favicon.ico" />
    <title>Python POC</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;1,100;1,300;1,400;1,500&display=swap"
        rel="stylesheet">

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

    <style>
        body {
            font-family: 'Roboto', sans-serif;
        }

        .navbar.bg-light {
            background-color: aquamarine !important;
        }

        .app-card-img {
            height: 215px !important;
        }
    </style>
</head>

<body>

    <nav class="navbar navbar-light bg-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">
                Padmasekhar
            </a>
        </div>
    </nav>

    <div class="container mt-1">
        <div class="card">
            <div class="card-header bg-primary text-light">Python POC</div>
            <div class="card-body">
                <p>Please click below link to see sample APIs developed using python</p>
                <a href="/docs" class="btn btn-primary">API docs</a>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
        crossorigin="anonymous"></script>
</body>

</html>
    """