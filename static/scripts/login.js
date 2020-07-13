/* Removing session */
sessionStorage.clear();

$.ajax({
    url: 'http://localhost:5001/api/v1/status',
    type: 'GET',
    success: function (data) {
        if (data.status == "OK") {
            console.log('API STATUS OK');
        }
    },
    error: function () {
        console.log('error API connection');
    }
});



// Login
$('#login_btn').click(function () {
    let username = $("#username").val();
    let password = $("#password").val();
    let user = {
        "username": username,
        "password": password
    };
    let url = "http://localhost:5001/api/v1/users/login/";

    $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify(user),
        ContentType: 'Application/json',
        success: function (result) {
            if (result.error == "user_not_found") {
                alert('User not found')
            }
            else {
                id_user = result.id;
                sessionStorage.setItem('id_user', id_user);
                location.href = "books";
            }
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});