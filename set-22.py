# Create a set containing available books and another set containing
# requested books. Determine which requested books are available.

def available_requested_books(available, requested):
    return available & requested


if __name__ == "__main__":
    available_books = {"Python Basics", "Data Structures", "AI Fundamentals", "Web Dev"}
    requested_books = {"Data Structures", "Machine Learning", "Web Dev"}

    print(f"Available books: {available_books}")
    print(f"Requested books: {requested_books}")
    print(f"Requested books available: {available_requested_books(available_books, requested_books)}")
