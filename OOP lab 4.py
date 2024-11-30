class Book:
    def __init__(self, title, author, publication_year):
       
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
      
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"


if __name__ == "__main__":
   
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    
    
    print(book)

