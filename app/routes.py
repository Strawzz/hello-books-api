from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

books_bp = Blueprint("books", __name__, url_prefix="/books")

# helper functions

def valid_book(book_id):

    try:
        book_id = int(book_id)
    except:
        message = f"book #{book_id} invalid"
        abort(make_response(f"message: {message}", 400))

    book = Book.query.get(book_id)

    if not book:
        message = f"book #{book_id} not found"
        abort(make_response(f"message:{message}", 404))
    
    return book

# def valid_paragrams_number(request_body):

#     if "title" not in request_body or "description" not in request_body:
#         message = "Please offer all the query paragrams"
#         abort (make_response(f"message: {message}", 400)) 
#     return


# route functions

@books_bp.route("", methods=["POST"])
def post_a_book():

    request_body = request.get_json()

    valid_paragrams_number(request_body)
    
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    message = f"Book {new_book.title} successfully created"
    return make_response(jsonify(f"message: {message}"), 201)



@books_bp.route("/<book_id>", methods = ["PUT"])
def update_book(book_id):

    book = valid_book(book_id)
    request_body = request.get_json()
    valid_paragrams_number(request_body)

    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()

    return make_response(f"Book #{book.id} successfully updated", 200)


@books_bp.route("/<book_id>", methods = ["DELETE"])
def delete_book(book_id):

    book = valid_book(book_id)

    db.session.delete(book)
    db.session.commit()

    message = f"Book #{book.id} successfully deleted"

    return make_response(f"message: {message}", 200)


@books_bp.route("", methods=["GET"])
def read_all_books():

    # this code replaces the previous query all code
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()
    # end of the new code

    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })

    return jsonify(books_response)



@books_bp.route("/<book_id>", methods = ["GET"])
def get_one_book(book_id):

    book = valid_book(book_id)

    return book.to_dict()




