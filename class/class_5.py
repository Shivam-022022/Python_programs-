class Book:

    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


books = []

for i in range(3):
    book_id = input("Enter book ID: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))

    book = Book(book_id, title, author, price)
    books.append(book)

for book in books:
    book.display()
    print()