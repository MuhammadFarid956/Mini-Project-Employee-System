from employee_manager import *

class FrontendManager:
    def __init__(self):
        self.EmployeesManager = EmployeesManager()
    
    def show_menu(self):
        messages = [
            "1. Add a new employee",
            "2. List all employees",
            "3. Delete by age range",
            "4. Update salary given a name",
            "5. End program"
        ]
        print("\n--- Employee Management System Menu ---")
        print("\n".join(messages))
        msg = f"Enter your choice (from 1 to {len(messages)}):"
        return input_is_valid(msg, 1, len(messages))
    
    def run(self):
        while True:
            choice = self.show_menu()

            if choice == 1:
                self.EmployeesManager.add_employee()
            elif choice == 2:
                self.EmployeesManager.list_employees()
            elif choice == 3:
                age_from = input_is_valid(f"\nEnter age from: ")
                age_to = input_is_valid(f"\nEnter age to: ")
                self.EmployeesManager.delete_employees_with_age(age_from, age_to)
            elif choice == 4:
                name = input("\nEnter employee name:\n ")
                salary = input("\nEnter employee salary:\n")
                self.EmployeesManager.update_salary_by_name(name, salary)
            else:
                print("\nExiting program. Goodbye!")
                break