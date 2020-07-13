/* Get the id_book */
let PageURL = window.location.pathname;
let url_var = PageURL.split('/');
let id_book = url_var[3];

/* Get the id_user */
let id_user_comment = sessionStorage.getItem('id_user');

/* Info Book*/
$.ajax({
    url: 'http://localhost:5001/api/v1/books/' + id_book + '/',
    type: 'GET',
    success: function (result) {
        $("#book_title").text(result.title);
        $("#publi_date").text(result.publication_date);
    },
    error: function (myerror) {
        console.log(myerror);
    }
});

// Create book
$('#new_comment_btn').click(function () {
    let text = $("#text_comment").val();
    let comment = {
        "id_book": id_book,
        "id_user": id_user_comment,
        "text": text
    };

    let url = "http://localhost:5001/api/v1/comments/";
    $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify(comment),
        ContentType: 'Application/json',
        success: function (result) {
            alert('Comment has been created')
            location.href = "/comments/book/" + id_book + "/";
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});
