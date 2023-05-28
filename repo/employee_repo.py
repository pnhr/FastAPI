import pyodbc
import pandas as pd
from typing import List, Optional
from models.employee import Employee
from repo.database import *


class EmployeeRepo:
    
    def __init__(self):
        self.empList:List[Employee] = []
        self.db = Database()


    def get_employees(self) -> List[Employee]:
        empDbList:List[Employee] = []
        query = "SELECT * FROM tblEmployees WHERE IS_ACTIVE = 1"

        for row in self.db.execute_select(query):
            emp  = Employee(id = row.ID, name=row.FIRST_NAME, surname=row.LAST_NAME)
            self.empList.append(emp)
        return self.empList
    
    
    def get_employee_by_id(self, emp_id) -> Employee:
        query = f"SELECT * FROM tblEmployees WHERE IS_ACTIVE = 1 AND ID = {emp_id}"
        data = self.db.execute_select(query)
        if len(data) > 0:
            row = next(iter(data), None)
            emp  = Employee(id = row.ID, name=row.FIRST_NAME, surname=row.LAST_NAME)
            return emp
    

    def add_employee(self, emp:Employee) -> bool:
        query = f"INSERT INTO tblEmployees (FIRST_NAME, LAST_NAME, IS_ACTIVE) VALUES ('{emp.name}','{emp.surname}', 1)"
        self.db.execute_dml(query)
        return True
    


    def delete_employee(self, employee_id:int) -> bool:
        query = f"UPDATE tblEmployees SET IS_ACTIVE = 0 WHERE ID = {employee_id}"
        exec = self.db.execute_dml(query)
        return exec.rowcount > 0



    def update_employee(self, updEmp:Employee) -> bool:
        query = "UPDATE tblEmployees SET"
        if updEmp.name != None:
            query += " " + f"FIRST_NAME = '{updEmp.name}'"
        if updEmp.name != None and updEmp.surname != None:
            query += ", " + f"LAST_NAME = '{updEmp.surname}'"
        elif updEmp.name == None and updEmp.surname != None:
            query += " " + f"LAST_NAME = '{updEmp.surname}'"

        query += " " + f"WHERE ID = {updEmp.id}"

        exec = self.db.execute_dml(query)
        return exec.rowcount > 0
    


    