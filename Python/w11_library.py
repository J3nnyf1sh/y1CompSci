class Book:

    def __init__(self, ibsn, author, title):
        self.available = True
        self.ibsn = ibsn
        self.author = author
        self.title = title

    def borrow(self):
        self.available = False

    def returnBook(self):
        self.available = True

    def getAvailabilityString(self):
        if self.available == False:
            return "unavailable"
        else:
            return "available"
    
    def __str__(self):
        Output = f"{self.title} by {self.author}"
        return Output


class DigitalBook(Book):
    
    def __init__(self, ibsn, author, title, compatibilities):
        super().__init__(ibsn, author, title)
        self.compatibility = set(compatibilities)
    
    def borrow(self):
        self.available = True
    
    def addCompatibility(self, newCompatibility):
        self.compatibility.append(newCompatibility)

    def __str__(self):
        Output = f"Digital book of {self.title} by {self.author}"
        return Output

class Library():
    def __init__(self):
        self.books = []
    
    def addBook(self, book):
        self.books.append(book)

    def borrowBook(self, book):
        book.borrow()
    
    def returnBook(self, book):
        book.returnBook()

    def __str__(self):
        Output = f"{self.books}"
        return Output
    
def main():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
    book2 = Book("1984", "George Orwell", "978-0451524935")
    book3 = DigitalBook("1984", "George Orwell", "978-0451524935", "Kindle")
    
    Library.addBook(book1)
    Library.addBook(book2)
    Library.addBook(book3)
    
    print(book1.getAvailabilityString())
    print(book2.getAvailabilityString())
    print(book3.getAvailabilityString())

    

    

    
        