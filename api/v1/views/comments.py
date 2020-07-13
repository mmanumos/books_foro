""" API Rest for comments - VIEW """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.comments import Comment
from models.users import User

# Allowed attributes to create
attr = ['id_book', 'id_user', 'text']


def set_obj(obj, **data):
    """ set the attributes of an object """
    not_key = ['id', 'created_at']
    for key, value in data.items():
        if key not in not_key:
            setattr(obj, key, value)


@app_views.route('/books/<book_id>/comments', methods=['GET'])
def all_comments(book_id):
    """ Return a list with all comments by book """
    try:
        all = storage.all(Comment)
        list_comment = []
        list_comment_user = []
        for key, value in all.items():
            if value.id_book == int(book_id):
                list_comment.append(value.to_dict())
        # Adding full name to the comment
        for com in list_comment:
            usr = storage.get(User, com['id_user'])
            com['user_name'] = usr.first_name + " " + usr.last_name
            list_comment_user.append(com)
        return jsonify(list_comment_user)
    except Exception:
        abort(404)


@app_views.route('/comments/<comment_id>/', methods=['GET'])
def get_comment(comment_id):
    """ Return a comment """
    try:
        obj = storage.get(Comment, comment_id)
        return jsonify(obj.to_dict())
    except Exception:
        abort(404)


@ app_views.route('/comments/', methods=['POST'])
def create_comment():
    """ Creation of comment """
    try:
        data = request.get_json(force=True)
        # attributes validation
        for at in attr:
            if at not in data.keys():
                return jsonify({"Error": str("Missing " + at)})
        obj = Comment()
        set_obj(obj, **data)
        storage.insert(obj)
        return jsonify(obj.to_dict())
    except Exception:
        abort(404)


@ app_views.route('/comments/<comment_id>/', methods=['PUT'])
def update_comment(comment_id):
    """ updating a comment """
    try:
        data = request.get_json(force=True)
        # attributes validation
        for key in data.keys():
            if key != 'text':
                return jsonify({"Error": "Invalid action"}), 404
        obj = storage.get(Comment, comment_id)
        obj.text = data['text']
        storage.commit()
        return jsonify(obj.to_dict())
    except Exception:
        abort(404)


@ app_views.route('/comments/<comment_id>/', methods=['DELETE'])
def delete_comment(comment_id):
    """ delete a comment """
    try:
        obj = storage.get(Comment, comment_id)
        if obj is not None:
            storage.delete(obj)
        return jsonify({})
    except Exception:
        abort(404)
