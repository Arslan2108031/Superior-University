
class Item:
    def __init__(self, title, author):
       
        self.title = title
        self.author = author

    def display_info(self):
        
        print(f"Title: {self.title}, Author: {self.author}")


class Book(Item):
    def __init__(self, title, author, pages):
       
        super().__init__(title, author)  
        self.pages = pages

    def additional_info(self):
       
        print(f"Pages: {self.pages}")



class Magazine(Item):
    def __init__(self, title, author, issue_number):
      
        super().__init__(title, author)  
        self.issue_number = issue_number

    def additional_info(self):
      
        print(f"Issue Number: {self.issue_number}")



if __name__ == "__main__":
   
    my_book = Book("1984", "George Orwell", 328)
    my_book.display_info() 
    my_book.additional_info()  
    
    print()  

    my_magazine = Magazine("Tech Today", "John Doe", 45)
    my_magazine.display_info() 
    my_magazine.additional_info()  