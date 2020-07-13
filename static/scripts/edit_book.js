/* Get the id_book */
let PageURL = window.location.pathname;
let url_var = PageURL.split('/');
let id_book = url_var[url_var.length - 2];

/* Info Book*/
$.ajax({
    url: 'http://localhost:5001/api/v1/books/' + id_book + '/',
    type: 'GET',
    success: function (result) {
        $("#title").val(result.title);
        $("#publication_date").val(result.publication_date);
    },
    error: function (myerror) {
        console.log(myerror);
    }
});

// Edit book
$('#edit_book_btn').click(function () {
    let title = $("#title").val();
    let publication_date = $("#publication_date").val();

    let book = {
        "title": title,
        "publication_date": publication_date
    };

    let url = "http://localhost:5001/api/v1/books/" + id_book + "/";
    $.ajax({
        type: "PUT",
        url: url,
        data: JSON.stringify(book),
        ContentType: 'Application/json',
        success: function (result) {
            console.log(result);
            alert('Book has been edited')
            location.href = "/edit_book/" + id_book + "/";
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});