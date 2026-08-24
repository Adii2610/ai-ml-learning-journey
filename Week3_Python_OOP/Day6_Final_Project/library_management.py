class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book.title}")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You have successfully borrowed '{book.title}'.")
                    return
                else:
                    print(f"Sorry, '{book.title}' is already borrowed.")
                    return
        print(f"No book found with ISBN {isbn}.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"You have successfully returned '{book.title}'.")
                    return
                else:
                    print(f"The book '{book.title}' was not borrowed.")
                    return
        print(f"No book found with ISBN {isbn}.")

    def display_books(self):
        print("\nLibrary Inventory:")
        for book in self.books:
            print(book)
        print()

# Example usage
if __name__ == "__main__":
    lib = Library()
    b1 = Book("Python Crash Course", "Eric Matthes", "101")
    b2 = Book("Clean Code", "Robert C. Martin", "102")

    lib.add_book(b1)
    lib.add_book(b2)

    lib.display_books()

    lib.borrow_book("101")
    lib.display_books()

    lib.return_book("101")
    lib.display_books()
