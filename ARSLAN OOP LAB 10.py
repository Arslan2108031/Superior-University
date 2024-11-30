import csv


class Employee:
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


def save_employees_to_csv(employees, filename="employees.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Salary", "Role", "Additional Info"])
        for employee in employees:
            if isinstance(employee, Manager):
                writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(),
                                 "Manager", employee.get_department()])
            elif isinstance(employee, Worker):
                writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(),
                                 "Worker", employee.get_hours_worked()])


def load_employees_from_csv(filename="employees.csv"):
    employees = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["Role"] == "Manager":
                    employees.append(Manager(row["Name"], int(row["Age"]), float(row["Salary"]), row["Additional Info"]))
                elif row["Role"] == "Worker":
                    employees.append(Worker(row["Name"], int(row["Age"]), float(row["Salary"]), int(row["Additional Info"])))
    except FileNotFoundError:
        print("No previous employee records found. Starting fresh.")
    return employees


def add_employee(employees):
    role = input("Enter role (Manager/Worker): ").strip().lower()
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    salary = float(input("Enter salary: "))

    if role == "manager":
        department = input("Enter department: ")
        employees.append(Manager(name, age, salary, department))
        print("Manager added successfully!")
    elif role == "worker":
        hours_worked = int(input("Enter hours worked: "))
        employees.append(Worker(name, age, salary, hours_worked))
        print("Worker added successfully!")
    else:
        print("Invalid role. Please try again.")


def display_employees(employees):
    if employees:
        for i, employee in enumerate(employees, 1):
            print(f"{i}. {employee.display_info()}")
    else:
        print("No employees to display.")


def update_employee(employees):
    display_employees(employees)
    index = int(input("Enter the number of the employee to update: ")) - 1
    if 0 <= index < len(employees):
        employee = employees[index]
        name = input("Enter new name (leave blank to keep current): ")
        if name:
            employee.set_name(name)

        age = input("Enter new age (leave blank to keep current): ")
        if age:
            employee.set_age(int(age))

        salary = input("Enter new salary (leave blank to keep current): ")
        if salary:
            employee.set_salary(float(salary))

        if isinstance(employee, Manager):
            department = input("Enter new department (leave blank to keep current): ")
            if department:
                employee.set_department(department)
        elif isinstance(employee, Worker):
            hours_worked = input("Enter new hours worked (leave blank to keep current): ")
            if hours_worked:
                employee.set_hours_worked(int(hours_worked))
        print("Employee updated successfully!")
    else:
        print("Invalid selection. Please try again.")


def delete_employee(employees):
    display_employees(employees)
    index = int(input("Enter the number of the employee to delete: ")) - 1
    if 0 <= index < len(employees):
        employees.pop(index)
        print("Employee deleted successfully!")
    else:
        print("Invalid selection. Please try again.")


def main():
    employees = load_employees_from_csv()

    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            display_employees(employees)
        elif choice == "3":
            update_employee(employees)
        elif choice == "4":
            delete_employee(employees)
        elif choice == "5":
            save_employees_to_csv(employees)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
