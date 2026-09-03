# Create a dictionary containing book IDs and book names.
#
# Implement:
# - Add a book
# - Search a book
# - Remove a book
# - Display all books
# - Count total books

books = {"B01": "Python Basics", "B02": "Data Structures"}


def add_book(book_id, title):
    books[book_id] = title


def search_book(book_id):
    return books.get(book_id, "Book not found")


def remove_book(book_id):
    return books.pop(book_id, None) is not None


def display_all_books():
    return books


def total_books():
    return len(books)


if __name__ == "__main__":
    add_book("B03", "AI Fundamentals")

    print(f"All books: {display_all_books()}")
    print(f"Search 'B02': {search_book('B02')}")
    print(f"Total books: {total_books()}")

    remove_book("B01")
    print(f"After removing B01: {display_all_books()}")
