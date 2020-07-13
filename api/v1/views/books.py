""" API Rest for books - VIEW """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.books import Book

# Allowed attributes to modify and create
attr = ['title', 'publication_date']


def set_obj(obj, **data):
    """ set the attributes of an object """
    not_key = ['id', 'created_at']
    for key, value in data.items():
        if key not in not_key:
            setattr(obj, key, value)


@app_views.route('/books/', methods=['GET'])
def all_books():
    """ Return a list with all books """
    try:
        all = storage.all(Book)
        list_book = []
        for key, value in all.items():
            list_book.append(value.to_dict())
        return jsonify(list_book)
    except Exception:
        abort(404)


@app_views.route('/books/<book_id>/', methods=['GET'])
def get_book(book_id):
    """ Return a list with all books """
    try:
        obj = storage.get(Book, book_id)
        return jsonify(obj.to_dict())
    except Exception:
        abort(404)


@app_views.route('/books/', methods=['POST'])
def create_book():
    """ Creation of book """
    try:
        data = request.get_json(force=True)
        # attributes validation
        for at in attr:
            if at not in data.keys():
                return jsonify({"Error": str("Missing " + at)})
        obj = Book()
        set_obj(obj, **data)
        storage.insert(obj)
        return jsonify(obj.to_dict())
    except Exception:
        abort(404)


@app_views.route('/books/<book_id>/', methods=['PUT'])
def update_book(book_id):
    """ updating a book """
    try:
        data = request.get_json(force=True)
        # attributes validation
        for key in data.keys():
            if key not in attr:
                return jsonify({"Error": "Invalid action"}), 404
        obj = storage.get(Book, book_id)
        set_obj(obj, **data)
        storage.commit()
        return jsonify(obj.to_dict())
    except Exception:
        abort(404)


@app_views.route('/books/<book_id>/', methods=['DELETE'])
def delete_book(book_id):
    """ delete a book """
    try:
        obj = storage.get(Book, book_id)
        if obj is not None:
            for com in obj.comments:
                storage.delete(com)
            storage.delete(obj)
        return jsonify({})
    except Exception:
        abort(404)
