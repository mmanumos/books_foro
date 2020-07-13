/* Selects */
/* list books*/
$.ajax({
    url: 'https://www.etnassoft.com/api/v1/get/?get_categories=all',
    type: 'GET',
    success: function (data) {
        let result = JSON.parse(data);
        for (var i = 0; i < result.length; i++) {
            $('#categories').append(
                "<option value='" + result[i].category_id + "'> " + result[i].name + "</option>"
            );
        }
    },
    error: function (myerror) {
        console.log(myerror);
    }
});





// Generate buttons
$("#info_gen").hide();


// generate excel
$('#generate_excel').click(function () {
    //let title = $("#title").val();
    let categorie_id = $("#categories").val();

    if (categorie_id == "") {
        alert('Please choose a category');
    }
    else {
        $("#info_gen").show();
        let filter = {
            "categorie_id": categorie_id,
        };

        let url = "http://localhost:5001/api/v1/file_excel/";
        $.ajax({
            type: "POST",
            url: url,
            data: JSON.stringify(filter),
            ContentType: 'Application/json',
            success: function (result) {
                $("#info_gen").hide();
                alert('File has been created in root directory of the application with the name: ' + result.File);
            },
            error: function (myerror) {
                console.log(myerror);
            }
        });
    }
});