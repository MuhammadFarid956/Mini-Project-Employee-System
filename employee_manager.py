import csv
import os
from utility import *
from employees import *

FILENAME = "data_employee.csv"

class EmployeesManager:
    def __init__(self):
        self.employees = {}

        try:
            with open(FILENAME, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    id_employee = row[0]
                    name = row[1]
                    age = row[2]
                    salary = row[3]

                    # Save employe to dictionary
                    self.employees[id_employee] = {'name': name, 'age': age, 'salary': salary}
        except FileNotFoundError:
            print("File not found.")

    def gen_id_emp(self):
        last_id = 0
        try:
            with open(FILENAME, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    code = row[0]
                    if code.startswith('EMP'):
                        num = int(code[3:])
                        if num > last_id:
                            last_id = num
        except FileNotFoundError:
            pass
        return f'EMP{last_id + 1:03d}'

    def list_employees(self):
        print("\n--- Employee List ---")
        if not os.path.exists(FILENAME):
            print("\nEmployee list is empty.\n")
            return
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            print(f"{'ID' : <8} | {'Name' : <20} | {'Age' : <5} | {'Salary' : >10}")
            print("-" * 50)
            for row in reader:
                print(f"{row[0] : <8} | {row[1] : <20} | {row[2] : <5} | RP {int(row[3]) :,}")

    def add_employee(self):
        id_employee = self.gen_id_emp()
        name = input("\nEnter employee name :")
        age = input_is_valid("Enter employee age :")
        salary = input_is_valid("Enter employee salary :")

        with open(FILENAME, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id_employee, name, age, salary])
        print(f"\nEmployee {name} added with ID {id_employee}.\n")
    
    def update_employee(self):
        print("--- Update Data Employee ---")
        self.list_employees()

        id_target = input("\nEnter the ID of the employee to update: ")

        temporary_data = []
        found = False

        try:
            with open(FILENAME, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == id_target:
                        print(f"Old Data:\nName: {row[1]}\nAge: {row[2]}\nSalary: {row[3]}\n")
                        print("Enter new data (Leave blank to keep current value)")
                        new_age = input_is_valid("New Age: ")
                        new_salary = input_is_valid("New Salary: ")

                        # logic if new data is blank, keep old data
                        if new_age > 0:
                            row[2] = new_age
                        if new_salary > 0:
                            row[3] = new_salary
                        found = True
                        print("EmpLoyee data updated seccessfully.")
                    
                    temporary_data.append(row)
        except FileNotFoundError:
            print("File not found.")
            return
        
        if found:
            with open(FILENAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(temporary_data)
            print("File CSV updated successfully.")
        else:
            print("Error: Employee ID not found.")


    def delete_employees_with_age(self, age_from, age_to):
        for emp in self.employees:
            if age_from <= emp.age <=age_to:
                print(f"Deleting employee: {emp.name}")
                self.employees.remive(emp)
    
    def find_employee_by_name(self, name):
        for emp in self.employees: 
            if emp.name == name:
                return emp
            return None
        
    def update_salary_by_name(self, name, salary):
        emp = self.find_employee_by_name(name)
        if emp is None:
            print("Error: No employee found!")
        else:
            emp.salary = salary
            print(f"EMployee {name}'s salary updated to {salary}.")

if __name__ == "__main__":
    manager = EmployeesManager()
    manager.list_employees()