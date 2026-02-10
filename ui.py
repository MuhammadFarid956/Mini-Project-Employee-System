import os
from utility import *
from employee_manager import *

class AppUI:
    def __init__(self, manager):
        self.manager = EmployeesManager()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_menu(self):
        print("\n" + "="*40)
        print(f"{'EMPLOYEE MANAGEMENT SYSTEM':^40}")
        print("="*40)
        print("1. Add Employee\n2. View Employees\n3. Update Employee\n4. Delete Employee\n5. Exit")
        print("="*40)

    def header_table(self):
        print("\n" + "-"*65)
        print(f"{'ID':<5} | {'Name':<20} | {'Age':<5} | {'Salary':<15}")
        print("-"*65)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option (1-5):").strip() 

            if choice == '1':
                self.menu_add()
            elif choice == '2':
                self.menu_view()
            elif choice == '3':
                self.menu_update()
            elif choice == '4':
                self.menu_delete()
            elif choice == '5':
                print("Exiting the program. Godbye!")
                break
            else:
                print("Invalid choice. Please selec a valid option.")
            
            input("\nPress Enter to continue...")
            self.clear_screen()

    # --- CRUD OPERATION HANDLERS ---
    def menu_add(self):
        print("\n[ ADD NEW EMPLOYEE]")
        name = input("Enter Name : ")
        age = input_is_valid("Enter Age : ")
        salary = input_is_valid("Enter salary : ")

        emp = self.manager.add_employee(name, age, salary)
        print(f"\nEmployee {emp.name} added sucessfully with ID {emp.id}.")
    
    def menu_view(self):
        print("\n[ VIEW EMPLOYEES ]")
        if not self.manager.employees:
            print("Empty data.")
        else:
            self.header_table()
            for emp in self.manager.employees:
                print(emp)

    def menu_update(self):
        self.menu_view()
        if not self.manager.employees:
            return
        
        id_target = input("\nEnter Employee ID : ").upper()
        new_salary = input_is_valid("Enter new salary : ")

        if self.manager.update_employee(id_target, salary = new_salary):
            print(f"Employee salary {id_target} updated successfully.")
        else:
            print("Employee ID not found.")
    
    def menu_delete(self):
        self.menu_view()
        if not self.manager.employees:
            return
        
        id_target = input("\nEnter Employee ID to delete : ").upper()
        confirm = input(f"Confirm delete Employee {id_target}? (y/n) : ").lower()

        if confirm == 'y':
            if self.manager.delete_emp(id_target):
                print(f"Employe {id_target} deleted successfully.")
            else:
                print("Error: Employe ID not found.")









