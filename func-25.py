# Create functions to add books, issue books, return books, search books, and
# display available books. Maintain book availability using dictionaries.

library = {}


def add_book(book_id, title, copies):
    library[book_id] = {"title": title, "copies": copies}


def issue_book(book_id):
    if book_id in library and library[book_id]["copies"] > 0:
        library[book_id]["copies"] -= 1
        return f"Issued: {library[book_id]['title']}"
    return "Book not available"


def return_book(book_id):
    if book_id in library:
        library[book_id]["copies"] += 1
        return f"Returned: {library[book_id]['title']}"
    return "Invalid book id"


def search_book(title):
    return [b for b in library.values() if title.lower() in b["title"].lower()]


def display_books():
    return {bid: b for bid, b in library.items() if b["copies"] > 0}


if __name__ == "__main__":
    add_book(1, "Python Basics", 3)
    add_book(2, "Data Structures", 2)

    print(issue_book(1))
    print(return_book(1))
    print("Search results:", search_book("Python"))
    print("Available Books:", display_books())
