/* Get the id_book */
let PageURL = window.location.pathname;
let url_var = PageURL.split('/');
let id_comment = url_var[url_var.length - 2];


/* Info comment*/
$.ajax({
    url: 'http://localhost:5001/api/v1/comments/' + id_comment + '/',
    type: 'GET',
    success: function (result) {
        $("#text_comment").text(result.text);
    },
    error: function (myerror) {
        console.log(myerror);
    }
});


// Edit comment
$('#edit_book_btn').click(function () {
    let text = $("#text_comment").val();
    let comment = {
        "text": text
    };

    let url = 'http://localhost:5001/api/v1/comments/' + id_comment + '/';
    $.ajax({
        type: "PUT",
        url: url,
        data: JSON.stringify(comment),
        ContentType: 'Application/json',
        success: function (result) {
            console.log(result);
            alert('Comment has been edited')
            location.href = "/edit_comment/" + id_comment + "/";
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});
