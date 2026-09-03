# Maintain book records containing book ID, title, author, and
# availability status. Implement operations to:
# - Add a book.
# - Search for a book.
# - Issue a book.
# - Return a book.
# - Display available books.

FILENAME = "books.csv"


def add_book(book_id, title, author):
    with open(FILENAME, "a") as f:
        f.write(f"{book_id},{title},{author},Available\n")


def read_books():
    books = []
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                book_id, title, author, status = line.strip().split(",")
                books.append({"id": book_id, "title": title, "author": author, "status": status})
    except FileNotFoundError:
        pass
    return books


def write_books(books):
    with open(FILENAME, "w") as f:
        for b in books:
            f.write(f"{b['id']},{b['title']},{b['author']},{b['status']}\n")


def search_book(book_id):
    books = read_books()
    for b in books:
        if b["id"] == book_id:
            return b
    return None


def issue_book(book_id):
    books = read_books()
    for b in books:
        if b["id"] == book_id and b["status"] == "Available":
            b["status"] = "Issued"
            write_books(books)
            return f"Book {book_id} issued successfully"
    return "Book not available"


def return_book(book_id):
    books = read_books()
    for b in books:
        if b["id"] == book_id and b["status"] == "Issued":
            b["status"] = "Available"
            write_books(books)
            return f"Book {book_id} returned successfully"
    return "Invalid return request"


def display_available_books():
    return [b for b in read_books() if b["status"] == "Available"]


if __name__ == "__main__":
    open(FILENAME, "w").close()  # reset file for demo

    add_book("B01", "Python Basics", "John Doe")
    add_book("B02", "Data Structures", "Jane Smith")

    print(issue_book("B01"))
    print("Search B01:", search_book("B01"))
    print(return_book("B01"))
    print("Available Books:", display_available_books())
