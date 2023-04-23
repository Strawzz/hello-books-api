from flask import Blueprint

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [Book(1, "Daisy", "A good novel."),
    Book(2, "A Clean Well-lighted Place", "A good short story."),
    Book(3, "Shanghai Flowers", "A realistic novel about courtesan life.")]

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)

