""" Init views """
from flask import Blueprint
# The blueprint is recorded in order to able use the views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

if app_views is not None:
    from api.v1.views.index import *
    from api.v1.views.books import *
    from api.v1.views.comments import *
    from api.v1.views.users import *
    from api.v1.views.file_excel import *
