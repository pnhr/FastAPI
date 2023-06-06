import pyodbc

class Database:
    def connect():
        # connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', 
        #                             host = 'PADMASEKHAR-NEW', 
        #                             database = 'EmployeeManagment', 
        #                             trusted_connection='yes')

        connection = pyodbc.connect(driver = '{ODBC Driver 17 for SQL Server}', 
                                    host = 'psnaz.database.windows.net', 
                                    database = 'psn',
                                    UID='psn',
                                    PWD='MySelf@123',
                                    trusted_connection='no')
        
        return connection
    
    def execute_select(self, query:str):
        con = Database.connect()
        employeeList = con.execute(query)
        return employeeList.fetchall()
    
    def execute_dml(self, query:str):
        con = Database.connect()
        exec = con.execute(query)
        con.commit()
        return exec

    def execute_dml_uncommit(self, query:str):
        con = Database.connect()
        return con.execute(query)