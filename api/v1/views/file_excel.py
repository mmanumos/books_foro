""" API Rest for categories_sub - VIEW """
from api.v1.views import app_views
from flask import jsonify, request, abort
from openpyxl import Workbook
from datetime import datetime
import requests as re


@app_views.route('/file_excel/', methods=['POST'])
def file_excel():
    """Crete the file excel """
    post = request.get_json(force=True)
    name_file = get_data(post)
    return jsonify({"File": name_file})


def get_data(post):
    """ Return data """
    headers = {'User-agent': 'me'}
    url = 'https://www.etnassoft.com/api/v1/get/?category_id=' + \
        post['categorie_id'] + "&results_range=0,10"
    data = re.get(url, headers=headers, allow_redirects=False).json()
    name_file = create_excel(data)
    return name_file


def create_excel(data):

    workbook = Workbook()
    sheet = workbook.active

    sheet["A1"] = "Id"
    sheet["B1"] = "Title"
    sheet["C1"] = "Author"

    row = 2
    for book in data:
        sheet[f"A{row}"] = book['ID']
        sheet[f"B{row}"] = book['title']
        sheet[f"C{row}"] = book['author']
        row = row + 1

    name_file = "openlibra_" + \
        str(datetime.now().strftime("%Y%m%d_%H%M%S")) + ".xlsx"
    workbook.save(name_file)
    return name_file
