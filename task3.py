class Book:
    def __init__(self, name, author, count=1):
        self.name = name
        self.author = author
        self.count = count

    def __str__(self):
        return f"'{self.name}' by {self.author} | Available: {self.count}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author):

        for book in self.books:
            if book.name == name and book.author == author:
                book.count += 1
                print("Book already exists, increased count")
                return

        #
        new_book = Book(name, author)
        self.books.append(new_book)
        print("Book added")

    def user_take_book(self, name, author):
        for book in self.books:
            if book.name == name and book.author == author:
                if book.count > 0:
                    book.count -= 1
                    print("You took the book")
                else:
                    print("No copies available")
                return

        print("Book not found")

    def show_books(self):
        if not self.books:
            print("Library is empty")
            return

        print("\nLibrary books:")
        for book in self.books:
            print(book)
            lib = Library()

            lib.add_book("Harry Potter", "J.K. Rowling")
            lib.add_book("Harry Potter", "J.K. Rowling")
            lib.add_book("Harry Potter", "Another Author")

            lib.show_books()

            lib.user_take_book("Harry Potter", "J.K. Rowling")
            lib.user_take_book("Harry Potter", "J.K. Rowling")
            lib.user_take_book("Harry Potter", "J.K. Rowling")  # перевірка на 0

            lib.user_take_book("Unknown Book", "No Author")  # неіснуюча книга

            lib.show_books()