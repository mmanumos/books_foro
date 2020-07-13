/* list books*/
$.ajax({
    url: 'http://localhost:5001/api/v1/books/',
    type: 'GET',
    success: function (result) {
        for (var i = 0; i < result.length; i++) {
            $('#list_books').append(
                "<div class='books__item'> \
                    <img class='books__item--img' src='/static/img/book-black.png' alt='Book'> \
                    <div class='books_item--description'> \
                        <h2>" + result[i].title + "</h2> \
                        <p> Publication date: " + result[i].publication_date + "</p> \
                    </div> \
                    <a class='button button_a' href='/comments/book/" + result[i].id + "/'>Comments</a> \
                    <a class='button button_a' href='/edit_book/" + result[i].id + "/'>Edit</a> \
                    <button class='button button_a delete_book_btn' id='" + result[i].id + "' >Delete</button> \
                </div>"
            );
        }
    },
    error: function (myerror) {
        console.log(myerror);
    }
});

/* Delete book */
$('#list_books').on('click', '.delete_book_btn', function (e) {
    let id_book = $(this).attr("id")
    $(this).parent().remove();

    let url = 'http://localhost:5001/api/v1/books/' + id_book + '/';
    $.ajax({
        type: "DELETE",
        url: url,
        success: function (result) {
            console.log(result);
            alert('Book has been removed with its comments.');
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });

});
