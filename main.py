from employee_manager import EmployeesManager, Employee
from ui import AppUI

if __name__ == "__main__":
    manager = EmployeesManager()
    app = AppUI(manager)
    app.run()