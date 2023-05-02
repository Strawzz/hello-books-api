from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

books_bp = Blueprint("books", __name__, url_prefix="/books")
# helper functions

def valid_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"book {book_id} invalid"}, 400))

    book = Book.query.get(book_id)
    if not book:
        abort(make_response({"message":f"book {book_id} not found"}, 404))
    
    return book

# route functions


@books_bp.route("/<book_id>", methods = ["GET"])
def handle_book(book_id):
    book = valid_book(book_id)

    return {
        "id":book.id,
        "title": book.title,
        "description": book.description
    }

@books_bp.route("/<book_id>", methods = ["PUT"])
def update_book(book_id):
    book = valid_book(book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"Book #{book.id} successfully updated")


@books_bp.route("/<book_id>", methods = ["DELETE"])
def delete_book(book_id):
    book = valid_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book {book.id} successfully deleted")

@books_bp.route("", methods=["GET"])
def handle_books():
    
    books = Book.query.all()
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)


#     elif request.method == "POST":
#         request_body = request.get_json()
#         new_book = Book(title=request_body["title"],
#                         description=request_body["description"])

#         db.session.add(new_book)
#         db.session.commit()

#         return make_response(f"Book {new_book.title} successfully created", 201)



# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         })
#     return jsonify(books_response)

# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     # try:
#     #     book_id = int(book_id)
#     # except:
#     #     return {"message":f"book {book_id} invalid"}, 400

#     # for book in books:
#     #     if book.id == book_id:
#     #         return {
#     #             "id": book.id,
#     #             "title": book.title,
#     #             "description": book.description
#     #         }
#     #     return {"message":f"book {book_id} not found"}, 404
#     book = valid_book(book_id)
#     return {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }



