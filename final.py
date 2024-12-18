import csv
import os
import re

class Employee:
    def __init__(self, emp_id, name, position, salary, email):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

    def update_details(self, name=None, position=None, salary=None, email=None):
        if name:
            self.name = name
        if position:
            self.position = position
        if salary is not None:
            self.salary = salary
        if email:
            self.email = email

    def display(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Email: {self.email}"

class EmployeeManager:
    def __init__(self, filename='employees.csv'):
        self.filename = filename
        self.employees = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader, None)  
                for row in reader:
                    if row:  
                        emp_id, name, position, salary, email = row
                        self.employees.append(Employee(emp_id, name, position, float(salary), email))


    def save_data(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for emp in self.employees:
                writer.writerow([emp.emp_id, emp.name, emp.position, emp.salary, emp.email])

    def add_employee(self, emp_id, name, position, salary, email):
        new_employee = Employee(emp_id, name, position, salary, email)
        self.employees.append(new_employee)
        self.save_data()

    def update_employee(self, emp_id, name=None, position=None, salary=None, email=None):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                emp.update_details(name, position, salary, email)
                self.save_data()
                return True
        return False

    def delete_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]
        self.save_data()

    def search_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp.display()
        return "Employee not found."

    def list_all_employees(self):
        return [emp.display() for emp in self.employees]

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_salary(salary):
    return isinstance(salary, (int, float)) and salary >= 0

def main():
    manager = EmployeeManager()
    
    while True:
        print("\nEmployee Data Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Search Employee")
        print("5. List All Employees")
        print("6. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Name: ")
            position = input("Enter Position: ")
            salary = float(input("Enter Salary: "))
            email = input("Enter Email: ")
            if is_valid_email(email) and is_valid_salary(salary):
                manager.add_employee(emp_id, name, position, salary, email)
                print("Employee added successfully.")
            else:
                print("Invalid email or salary.")

        elif choice == '2':
            emp_id = input("Enter Employee ID to update: ")
            name = input("Enter new Name (leave blank to keep current): ")
            position = input("Enter new Position (leave blank to keep current): ")
            salary_input = input("Enter new Salary (leave blank to keep current): ")
            salary = float(salary_input) if salary_input else None
            email = input("Enter new Email (leave blank to keep current): ")
            if email and not is_valid_email(email):
                print("Invalid email.")
                continue
            if salary is not None and not is_valid_salary(salary):
                print("Invalid salary.")
                continue
            if manager.update_employee(emp_id, name or None, position or None, salary, email or None):
                print("Employee updated successfully.")
            else:
                print("Employee not found.")

        elif choice == '3':
            emp_id = input("Enter Employee ID to delete: ")
            manager.delete_employee(emp_id)
            print("Employee deleted successfully.")

        elif choice == '4':
            emp_id = input("Enter Employee ID to search: ")
            print(manager.search_employee(emp_id))

        elif choice == '5':
            employees = manager.list_all_employees()
            if employees:
                print("\nList of Employees:")
                for emp in employees:
                    print(emp)
            else:
                print("No employees found.")

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()