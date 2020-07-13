from flask import Flask, render_template, url_for, make_response, redirect
app = Flask(__name__)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/new_account')
def new_account():
    return render_template('new_account.html')


@app.route('/account')
def account():
    return render_template('account.html')


@app.route('/books')
def books():
    return render_template('books.html')


@app.route('/new_book')
def new_book():
    return render_template('new_book.html')


@app.route('/edit_book/<book_id>/')
def edit_book(book_id):
    return render_template('edit_book.html')


@app.route('/comments/book/<book_id>/')
def comments(book_id):
    return render_template('comments.html')


@app.route('/new_comment/book/<book_id>/')
def new_comment(book_id):
    return render_template('new_comment.html')


@app.route('/edit_comment/<comment_id>/')
def edit_comment(comment_id):
    return render_template('edit_comment.html')


@app.route('/reports/')
def reports():
    return render_template('reports.html')


@app.route('/')
def redirect_default():
    """ Redirect to login like default page """
    response = make_response(redirect("/login"))
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
