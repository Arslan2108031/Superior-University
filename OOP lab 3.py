class Rectangle:
    def __init__(self, width, height):
      
        self.width = width
        self.height = height

    def __str__(self):
        
        return f"Rectangle: {self.width} x {self.height}"

    def area(self):
       
        return self.width * self.height

    def perimeter(self):
       
        return 2 * (self.width + self.height)



if __name__ == "__main__":
    
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))

    
    rect = Rectangle(width, height)

    print(rect)

    
    print(f"Area: {rect.area()}")

  
    print(f"Perimeter: {rect.perimeter()}")
class Rectangle:
    def __init__(self, width, height):
       
        self.width = width
        self.height = height

    def __str__(self):
       
        return f"Rectangle: {self.width} x {self.height}"

    def area(self):
       
        return self.width * self.height

    def perimeter(self):
       
        return 2 * (self.width + self.height)



if __name__ == "__main__":
    
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))

    
    rect = Rectangle(width, height)

    
    print(rect)

    
    print(f"Area of the rectangle: {rect.area()}")

    
    print(f"Perimeter of the rectangle: {rect.perimeter()}")
