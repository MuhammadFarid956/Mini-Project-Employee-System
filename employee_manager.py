import csv
import os

FILENAME = "data_employee.csv"

class Employee:
    def __init__(self, id_emp, name, age, salary):
        self.id = id_emp
        self.name = name
        self.age = int(age)
        self.salary = float(salary)
    
    def to_list(self):
        return [self.id, self.name, self.age, self.salary]
    
    def __str__(self):
        return f"{self.id:<10} | {self.name:<20} | {self.age:<5} | Rp {self.salary:<10.2f}"
    
class EmployeesManager:
    def __init__(self):
        self.employees = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(FILENAME):
            return
        
        try:
            with open(FILENAME, 'r') as file:
                reader = csv.reader(file)
                self.employees = [Employee(*row) for row in reader if row]

        except Exception as e:
            print(f"Error loading data: {e}")

    def save_data(self):
        try:
            with open(FILENAME, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows([emp.to_list() for emp in self.employees])
        except Exception as e:
            print(f"Error saving data: {e}")
            
    def gen_id(self):
        if not os.path.exists(FILENAME):
            return 'EMP001'
        last_id = self.employees[-1].id
        num = int(last_id.replace("EMP", "")) + 1
        return f"EMP{num:03d}"
    
    # --- CRUD OPERATIONS ---
    def add_employee(self, name, age, salary):
            new_id = self.gen_id()
            new_emp = Employee(new_id, name, age, salary)
            self.employees.append(new_emp)
            self.save_data()
            return new_emp 

    def find_by_id(self, id_target):
        return next((emp for emp in self.employees if emp.id == id_target), None)
    
    def update_employee(self, id_target, name=None, age=None, salary=None):
        emp = self.find_by_id(id_target)
        if emp:
            if name: emp.name = name
            if age: emp.age = int(age)
            if salary: emp.salary = float(salary)
            self.save_data()
            return True
        return False

    def delete_emp(self, id_target):
        emp = self.find_by_id(id_target)
        if emp:
            self.employees.remove(emp)
            self.save_data()
            return True
        return False
    
if __name__ == "__main__":
    manager = EmployeesManager()
    manager.add_employee("Mbappe", 30, 4000000 )