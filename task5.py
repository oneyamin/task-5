# Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn  # private
        self.available = True

    def show_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}, Available: {self.available}")

    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn


# Member class
class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id  # private
        self.borrowed = []

    def get_id(self):
        return self.__membership_id

    def set_id(self, new_id):
        self.__membership_id = new_id

    def borrow(self, book):
        if book.available:
            self.borrowed.append(book)
            book.available = False
            print(f"{self.name} borrowed {book.title}")
        else:
            print(f"{book.title} is not available")

    def return_book(self, book):
        if book in self.borrowed:
            self.borrowed.remove(book)
            book.available = True
            print(f"{self.name} returned {book.title}")
        else:
            print("Book not found in borrowed list")


# StaffMember class (inherits from Member)
class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        library.books.append(book)
        print(f"{self.name} added book: {book.title}")


# Library class
class Library:
    def __init__(self):
        self.books = []

    def show_books(self):
        if not self.books:
            print("Library is empty.")
        for book in self.books:
            book.show_info()


# Test example
lib = Library()
staff = StaffMember("Ali", "M100", "S200")

b1 = Book("Python Basics", "John Doe", "001")
b2 = Book("OOP Made Easy", "Jane Smith", "002")

staff.add_book(lib, b1)
staff.add_book(lib, b2)

lib.show_books()

member = Member("Sara", "M101")
member.borrow(b1)
member.borrow(b2)
member.return_book(b1)

lib.show_books()
