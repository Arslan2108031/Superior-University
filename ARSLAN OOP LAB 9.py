import csv

class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"


class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        super().__init__(title, author)
        self.genre = genre
        self.pages = pages

    
    def display_info(self):
        info = super().display_info()
        if self.genre and self.pages:
            info += f", Genre: {self.genre}, Pages: {self.pages}"
        return info


class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        super().__init__(title, author)
        self.journal = journal
        self.doi = doi

    def display_info(self):
        info = super().display_info()
        if self.journal and self.doi:
            info += f", Journal: {self.journal}, DOI: {self.doi}"
        return info


def save_books_to_csv(books, filename="books.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Genre", "Pages"])
        writer.writeheader()
        for book in books:
            writer.writerow({
                "Title": book.title,
                "Author": book.author,
                "Genre": book.genre if book.genre else "",
                "Pages": book.pages if book.pages else ""
            })


def save_articles_to_csv(articles, filename="articles.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Author", "Journal", "DOI"])
        writer.writeheader()
        for article in articles:
            writer.writerow({
                "Title": article.title,
                "Author": article.author,
                "Journal": article.journal if article.journal else "",
                "DOI": article.doi if article.doi else ""
            })


def load_books_from_csv(filename="books.csv"):
    books = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                books.append(Book(row["Title"], row["Author"], row["Genre"], row["Pages"]))
    except FileNotFoundError:
        print("Books file not found. Starting fresh.")
    return books


def load_articles_from_csv(filename="articles.csv"):
    articles = []
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                articles.append(Article(row["Title"], row["Author"], row["Journal"], row["DOI"]))
    except FileNotFoundError:
        print("Articles file not found. Starting fresh.")
    return articles

def main():
    books = load_books_from_csv()
    articles = load_articles_from_csv()

    while True:
        print("\nDocument Management System")
        print("1. Add a Book")
        print("2. Add an Article")
        print("3. Display All Books")
        print("4. Display All Articles")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            genre = input("Enter Book Genre (optional): ") or None
            pages = input("Enter Number of Pages (optional): ") or None
            books.append(Book(title, author, genre, pages))
            print("Book added successfully!")

        elif choice == "2":
            title = input("Enter Article Title: ")
            author = input("Enter Article Author: ")
            journal = input("Enter Journal Name (optional): ") or None
            doi = input("Enter DOI (optional): ") or None
            articles.append(Article(title, author, journal, doi))
            print("Article added successfully!")

        elif choice == "3":
            if books:
                print("\nBooks:")
                for i, book in enumerate(books, 1):
                    print(f"{i}. {book.display_info()}")
            else:
                print("No books available.")

        elif choice == "4":
            if articles:
                print("\nArticles:")
                for i, article in enumerate(articles, 1):
                    print(f"{i}. {article.display_info()}")
            else:
                print("No articles available.")

        elif choice == "5":
            save_books_to_csv(books)
            save_articles_to_csv(articles)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
