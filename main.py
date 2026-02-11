from employee_manager import EmployeesManager
from ui import AppUI

if __name__ == "__main__":
    manager = EmployeesManager()
    app = AppUI(manager)
    app.run()

if __name__ == "__main__":
    manager = EmployeesManager()