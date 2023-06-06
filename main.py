import employee.EmployeeApi as emp
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles



templates = Jinja2Templates(directory="templates")

description = "Just for learning CURD oprations using SQL Server and Python"
app = FastAPI(title="Employee Management", description = description)
app.mount("/static", StaticFiles(directory="templates"), name="static")
app.include_router(emp.employeeApi)

@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return FileResponse("favicon.ico")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})