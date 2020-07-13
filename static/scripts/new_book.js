// Create book
$('#create_book_btn').click(function () {
    let title = $("#title").val();
    let publication_date = $("#publication_date").val();

    let book = {
        "title": title,
        "publication_date": publication_date
    };

    let url = "http://localhost:5001/api/v1/books/";
    $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify(book),
        ContentType: 'Application/json',
        success: function (result) {
            console.log(result);
            alert('Book has been created')
            location.href = "books";
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});