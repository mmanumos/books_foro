""" API Rest for categories_sub - VIEW """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.users import User
from models.comments import Comment

# Allowed attributes to modify and create
attr = ['username', 'password', 'first_name', 'last_name']


def set_obj(obj, **data):
    """ set the attributes of an object """
    not_key = ['id', 'created_at']
    for key, value in data.items():
        if key not in not_key:
            setattr(obj, key, value)


@app_views.route('/users/<user_id>/', methods=['GET'])
def all_users(user_id):
    """ Return a list with all users """
    try:
        obj = storage.get(User, user_id)
        return jsonify(obj.to_dict())
    except Exception:
        abort(404)


@app_views.route('/users/', methods=['POST'])
def create_user():
    """ Creation of user """
    # try:
    data = request.get_json(force=True)
    # attributes validation
    for at in attr:
        if at not in data.keys():
            return jsonify({"Error": str("Missing " + at)})
    obj = User()
    set_obj(obj, **data)
    storage.insert(obj)
    obj = obj.to_dict()
    del obj['password']
    return jsonify(obj)
    # except Exception:
    # abort(404)


@app_views.route('/users/<user_id>/', methods=['PUT'])
def update_user(user_id):
    """ updating a user """
    try:
        data = request.get_json(force=True)
        # attributes validation
        for key in data.keys():
            if key not in attr:
                return jsonify({"Error": "Invalid action"}), 404
        obj = storage.get(User, user_id)
        set_obj(obj, **data)
        storage.commit()
        return jsonify(obj.to_dict())
    except Exception:
        abort(404)


@app_views.route('/users/<user_id>/', methods=['DELETE'])
def delete_user(user_id):
    """ delete a user """
    try:
        obj = storage.get(User, user_id)
        if obj is not None:
            for key, value in storage.all(Comment).items():
                if value.id_user == obj.id:
                    storage.delete(value)
            storage.delete(obj)
        return jsonify({})
    except Exception:
        abort(404)


@app_views.route('/users/login/', methods=['POST'])
def login():
    # get data
    data = request.get_json(force=True)
    obj = None
    if 'username' not in data.keys() or 'password' not in data.keys():
        return jsonify({"Error": "username and password are missing"})
    users = storage.all(User)
    # validation username and password
    for key, value in users.items():
        if value.username == data['username'] and value.password == data['password']:
            obj = storage.get(User, value.id)
    if obj is None:
        return jsonify({"error": "user_not_found"})
    obj = obj.to_dict()
    del obj['password']
    return jsonify(obj)

 # md5 for password
    # password = data['password']
    # m = hashlib.md5()
    # m.update(str.encode(password))
    # data['password'] = m.hexdigest()
