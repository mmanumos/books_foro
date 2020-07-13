let PageURL = window.location.pathname;
let url_var = PageURL.split('/');
let id_book = url_var[3];

$('#route_new_comment').attr("href", '/new_comment/book/' + id_book + '/');

/* Info Book*/
$.ajax({
    url: 'http://localhost:5001/api/v1/books/' + id_book + '/',
    type: 'GET',
    success: function (result) {
        $('#book_title').text(result.title);
        $('#publi_date').text(result.publication_date);
    },
    error: function (myerror) {
        console.log(myerror);
    }
});


/* List comments */
$.ajax({
    url: 'http://localhost:5001/api/v1/books/' + id_book + '/comments/',
    type: 'GET',
    success: function (result) {
        for (var i = 0; i < result.length; i++) {
            $('#list_comments').append(
                "<div class='comment__description'> \
                    <p class= 'comment__description--user'> User: <span> " + result[i].user_name + " </span></p> \
                    <p class='comment__description--text'>" + result[i].text + " </p> \
                    <p class='comment__description--date'>Date: <span> "+ result[i].created_at + "</span></p> \
                    <a class='new__comment' href='/edit_comment/" + result[i].id + "/'>Edit</a> \
                    <button class='new__comment delete_comment_btn' id='" + result[i].id + "' >Delete</button> \
                </div> "
            );
        }
    },
    error: function (myerror) {
        console.log(myerror);
    }
});


/* Delete comment */
$('#list_comments').on('click', '.delete_comment_btn', function (e) {
    let id_comment = $(this).attr("id")
    $(this).parent().remove();

    let url = 'http://localhost:5001/api/v1/comments/' + id_comment + '/';
    $.ajax({
        type: "DELETE",
        url: url,
        success: function (result) {
            alert('Comment has been removed.');
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });

});