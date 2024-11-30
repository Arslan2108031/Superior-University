import csv


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        return f"Employee ID: {self.employee_id}, Position: {self.position}"

class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def additional_info(self):
        return f"Department: {self.department}"

    def display_all_info(self):
        return (
            f"{self.display_info()} | "
            f"{Employee.display_info(self)} | "
            f"{self.additional_info()}"
        )

def read_employees_from_file(filename="employees.csv"):
    employees = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                employee = Staff(
                    row["Name"], int(row["Age"]),
                    row["Employee ID"], row["Position"], row["Department"]
                )
                employees.append(employee)
    except FileNotFoundError:
        print("File not found. A new file will be created.")
    return employees

def write_employees_to_file(employees, filename="employees.csv"):
    with open(filename, mode="w", newline="") as file:
        fieldnames = ["Name", "Age", "Employee ID", "Position", "Department"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for employee in employees:
            writer.writerow({
                "Name": employee.name,
                "Age": employee.age,
                "Employee ID": employee.employee_id,
                "Position": employee.position,
                "Department": employee.department,
            })

def add_employee(employees):
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    position = input("Enter Position: ")
    department = input("Enter Department: ")
    new_employee = Staff(name, age, employee_id, position, department)
    employees.append(new_employee)
    print("Employee added successfully!")

def main():
    employees = read_employees_from_file()

    while True:
        print("\nEmployee Management System")
        print("1. Display All Employees")
        print("2. Add New Employee")
        print("3. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            if employees:
                for i, emp in enumerate(employees, 1):
                    print(f"{i}. {emp.display_all_info()}")
            else:
                print("No employee data available.")

        elif choice == "2":
            add_employee(employees)

        elif choice == "3":
            write_employees_to_file(employees)
            print("Employee data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
