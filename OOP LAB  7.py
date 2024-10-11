#TASK 1
class Vehicle:
    def __init__(self, make, model):
       
        self.make = make
        self.model = model

    def display_info(self):
        
        print(f"Make: {self.make}, Model: {self.model}")



class Car(Vehicle):
    def __init__(self, make, model, num_doors):
       
        super().__init__(make, model) 
        self.num_doors = num_doors

    def additional_info(self):
    
        print(f"Number of doors: {self.num_doors}")



class LuxuryCar(Car):
    def __init__(self, make, model, num_doors, features):
       
        super().__init__(make, model, num_doors)  
        self.features = features

    def additional_info(self):
       
        print(f"Number of doors: {self.num_doors}")
        print(f"Luxury Features: {', '.join(self.features)}")



def main():
   
    vehicle = Vehicle("Toyota", "Corolla")
    print("Vehicle Info:")
    vehicle.display_info()
    print()


    car = Car("Honda", "Civic", 4)
    print("Car Info:")
    car.display_info()
    car.additional_info()
    print()

   
    luxury_car = LuxuryCar("BMW", "7 Series", 4, ["Leather Seats", "Sunroof", "Heated Steering Wheel"])
    print("Luxury Car Info:")
    luxury_car.display_info()
    luxury_car.additional_info()


if __name__ == "__main__":
    main()





#TASK 2
class Employee:
    def __init__(self, name, position):
       
        self.name = name
        self.position = position

    def display_info(self):
       
        print(f"Name: {self.name}, Position: {self.position}")


class Manager(Employee):
    def __init__(self, name, position, department):
       
        super().__init__(name, position)  
        self.department = department

    def additional_info(self):
       
        print(f"Department: {self.department}")


class Worker(Employee):
    def __init__(self, name, position, hours_worked):
       
        super().__init__(name, position)  
        self.hours_worked = hours_worked

    def additional_info(self):
       
        print(f"Hours Worked: {self.hours_worked}")



def main():
   
    manager = Manager("Arslan" ,"Manager", "Sales")
    print("Manager Info:")
    manager.display_info()
    manager.additional_info()
    print()

   
    worker = Worker("Sami", "Worker", 40)
    print("Worker Info:")
    worker.display_info()
    worker.additional_info()
    print()



if __name__ == "__main__":
    main()
