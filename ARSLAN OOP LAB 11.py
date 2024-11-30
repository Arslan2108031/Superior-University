from abc import ABC, abstractmethod
import csv


class AbstractEmployee(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_age(self):
        pass

    @abstractmethod
    def set_age(self, age):
        pass

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def set_salary(self, salary):
        pass

    @abstractmethod
    def display_info(self):
        pass


class Employee(AbstractEmployee):
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        return f"Name: {self.__name}, Age: {self.__age}, Salary: {self.__salary}"


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def display_info(self):
        return super().display_info() + f", Department: {self.__department}"


class Worker(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked

    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    def display_info(self):
        return super().display_info() + f", Hours Worked: {self.__hours_worked}"


def load_employees(filename):
    employees = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Type"] == 'Manager':
                    employees.append(Manager(row['Name'], int(row['Age']), float(row['Salary']), row['Department']))
                elif row['Type'] == 'Worker':
                    employees.append(Worker(row['Name'], int(row['Age']), float(row['Salary']), int(row['Hours Worked'])))
    except FileNotFoundError:
        pass  
    return employees


def save_employees(filename, employees):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['Type', 'Name', 'Age', 'Salary', 'Department', 'Hours Worked']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for emp in employees:
            if isinstance(emp, Manager):
                writer.writerow({
                    'Type': 'Manager',
                    'Name': emp.get_name(),
                    'Age': emp.get_age(),
                    'Salary': emp.get_salary(),
                    'Department': emp.get_department(),
                    'Hours Worked': ''
                })
            elif isinstance(emp, Worker):
                writer.writerow({
                    'Type': 'Worker',
                    'Name': emp.get_name(),
                    'Age': emp.get_age(),
                    'Salary': emp.get_salary(),
                    'Department': '',
                    'Hours Worked': emp.get_hours_worked()
                })


def main():
    employees = load_employees('employees.csv')

    while True:
        print("\n=== Employee Management System ===")
        print("1. Add Manager")
        print("2. Add Worker")
        print("3. Display All Employees")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            department = input("Enter department: ")
            employees.append(Manager(name, age, salary, department))
            print("Manager added successfully!")

        elif choice == '2':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            salary = float(input("Enter salary: "))
            hours_worked = int(input("Enter hours worked: "))
            employees.append(Worker(name, age, salary, hours_worked))
            print("Worker added successfully!")

        elif choice == '3':
            if not employees:
                print("No employees found!")
            else:
                for i, emp in enumerate(employees, 1):
                    print(f"{i}. {emp.display_info()}")

        elif choice == '4':
            emp_name = input("Enter the name of the employee to update: ")
            for emp in employees:
                if emp.get_name() == emp_name:
                    print("1. Update Name")
                    print("2. Update Age")
                    print("3. Update Salary")
                    if isinstance(emp, Manager):
                        print("4. Update Department")
                    elif isinstance(emp, Worker):
                        print("4. Update Hours Worked")
                    update_choice = input("Enter your choice: ")
                    if update_choice == '1':
                        emp.set_name(input("Enter new name: "))
                    elif update_choice == '2':
                        emp.set_age(int(input("Enter new age: ")))
                    elif update_choice == '3':
                        emp.set_salary(float(input("Enter new salary: ")))
                    elif update_choice == '4':
                        if isinstance(emp, Manager):
                            emp.set_department(input("Enter new department: "))
                        elif isinstance(emp, Worker):
                            emp.set_hours_worked(int(input("Enter new hours worked: ")))
                    print("Employee updated successfully!")
                    break
            else:
                print("Employee not found!")

        elif choice == '5':
            emp_name = input("Enter the name of the employee to delete: ")
            for emp in employees:
                if emp.get_name() == emp_name:
                    employees.remove(emp)
                    print("Employee deleted successfully!")
                    break
            else:
                print("Employee not found!")

        elif choice == '6':
            save_employees('employees.csv', employees)
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
