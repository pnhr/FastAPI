from typing import List
from employee import Employee


class EmployeeRepo:
    def __init__(self):
        self.empList:List[Employee] = []

    def get_employees(self) -> List[Employee]:
        
        emp = Employee(id=1, name="Padmasekhar", surname="Pottepalem")
        emp2 = Employee(id=2, name="Narmada", surname="Pottepalem")
        emp3 = Employee(id=3, name="Hetanshi", surname="Pottepalem")
        emp4 = Employee(id=4, name="Hetanshi", surname="Pottepalem")
        emp5 = Employee(id=5, name="Admin")

        self.empList = [emp, emp2, emp3, emp4, emp5]

        return self.empList
    
    def get_employee_by_id(self, emp_id) -> Employee:
        self.get_employees()
        emp = next(filter(lambda x: x.id == emp_id, self.empList), None)
        return emp
    

    def add_employee(self, emp:Employee) -> bool:
        self.get_employees()
        count = len(self.empList)
        self.empList.append(emp)
        upd_cnt = len(self.empList)
        return count < upd_cnt
    


    def update_employee(self, updEmp:Employee) -> bool:
        self.get_employees()
        emp = next(filter(lambda x: x.id == updEmp.id, self.empList), None)
        if emp != None:
            if updEmp.name != None:
                emp.name = updEmp.name
            if updEmp.surname != None:
                emp.surname = updEmp.surname

            return True
        return False
    
    def delete_employee(self, employee_id:int) -> bool:
        self.get_employees()
        emp = next(filter(lambda x: x.id == employee_id, self.empList), None)
        if emp != None:
            self.empList.remove(emp)
            return True
        return False