class Book:
    def __init__(self, title, author, publication_year):
        """
        Constructor method to initialize the title, author, and publication year of the book.
        
        Parameters:
        title (str): The title of the book.
        author (str): The author of the book.
        publication_year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        """
        Method to return a string representation of the book object.
        
        Returns:
        str: A string representing the book in the format 'Title: [title], Author: [author], Publication Year: [publication_year]'.
        """
        return f"Title: {self.title}, Author: {self.author}, Publication Year: {self.publication_year}"

# Example of how to use the Book class
if __name__ == "__main__":
    # Creating an instance of the Book class
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
    
    # Displaying the book details using the __str__ method
    print(book)

