""" API Rest for file_pdf - VIEW """
from api.v1.views import app_views
from flask import jsonify, request, abort
from datetime import datetime
import requests as re
import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


@app_views.route('/file_pdf/', methods=['POST'])
def file_pdf():
    """Crete the pdf file """
    post = request.get_json(force=True)
    name_file = get_data(post)
    return jsonify({"File": name_file})


def get_data(post):
    """ Get data of request """
    headers = {'User-agent': 'me'}
    url = 'https://www.etnassoft.com/api/v1/get/?category_id=' + \
        post['categorie_id'] + "&results_range=0,10"
    list_book = re.get(url, headers=headers, allow_redirects=False).json()
    data_pdf = [("Id", "Title", "Author")]
    for book in list_book:
        id = book['ID']
        title = book['title']
        author = book['author']
        data_pdf.append((id, title, author))
    name_file = export_to_pdf(data_pdf)
    return name_file


def export_to_pdf(data):
    name_file = "openLibra_" + \
        str(datetime.now().strftime("%Y%m%d_%H%M%S")) + ".pdf"
    c = canvas.Canvas(name_file, pagesize=A4)
    w, h = A4
    max_rows_per_page = 45
    # titles
    c.drawString(28, h - 50, "API Supplier: OpenLibra")
    # Margin.
    x_offset = 28
    y_offset = 100
    # Space between rows.
    padding = 15

    xlist = [x + x_offset for x in [0, 50, 400, 552]]
    ylist = [h - y_offset - i*padding for i in range(max_rows_per_page + 1)]

    for rows in grouper(data, max_rows_per_page):
        rows = tuple(filter(bool, rows))
        c.grid(xlist, ylist[:len(rows) + 1])
        for y, row in zip(ylist[:-1], rows):
            for x, cell in zip(xlist, row):
                c.drawString(x + 2, y - padding + 3, str(cell))
        c.showPage()
    c.save()
    return name_file


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args)
