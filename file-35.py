# Create a directory structure for a library application with separate
# packages for:
#   a) Books
#   b) Members
#   c) Transactions
# Each package should contain suitable modules and a main program should
# combine all functionality.
#
# NOTE: A real project would use "books/", "members/", and
# "transactions/" packages, each with their own modules. It is
# simulated here in one file using clearly labelled sections, so it
# matches the file-XX.py naming convention used for this exercise set.

# ---------- books package ----------
books = {}


def add_book(book_id, title, author):
    books[book_id] = {"title": title, "author": author, "available": True}


def display_books():
    return books
# ---------- end books package ----------


# ---------- members package ----------
members = {}


def add_member(member_id, name):
    members[member_id] = {"name": name, "borrowed_books": []}
# ---------- end members package ----------


# ---------- transactions package ----------
def issue_book(member_id, book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        members[member_id]["borrowed_books"].append(book_id)
        return f"Book {book_id} issued to member {member_id}"
    return "Book not available"


def return_book(member_id, book_id):
    if book_id in members[member_id]["borrowed_books"]:
        members[member_id]["borrowed_books"].remove(book_id)
        books[book_id]["available"] = True
        return f"Book {book_id} returned by member {member_id}"
    return "Invalid return request"
# ---------- end transactions package ----------


if __name__ == "__main__":
    add_book("B01", "Python Basics", "John Doe")
    add_book("B02", "Data Structures", "Jane Smith")
    add_member("M01", "Ritesh Agale")

    print(issue_book("M01", "B01"))
    print("Books:", display_books())
    print("Members:", members)
    print(return_book("M01", "B01"))
