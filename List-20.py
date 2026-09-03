# Create a list of books.
# Implement:
# • Add a new book
# • Search a book
# • Remove a book
# • Display all books
# • Count total books

books = ["Python", "Java", "C++"]

new_book = input("Enter book to add: ")
books.append(new_book)

search = input("Enter book to search: ")
if search in books:
    print("Book found")
else:
    print("Book not found")

remove = input("Enter book to remove: ")
if remove in books:
    books.remove(remove)

print("Books:", books)
print("Total books:", len(books))
