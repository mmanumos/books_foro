// Login
$('#create_user_btn').click(function () {
    let username = $("#username").val();
    let password = $("#password").val();
    let first_name = $("#first_name").val();
    let last_name = $("#last_name").val();

    let user = {
        "username": username,
        "password": password,
        "first_name": first_name,
        "last_name": last_name
    };

    for (const [key, value] of Object.entries(user)) {
        if (value == '') {
            alert('Missing fields');
            location.href = "new_account";
            break
        }
    }

    let url = "http://localhost:5001/api/v1/users/";
    $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify(user),
        ContentType: 'Application/json',
        success: function (result) {
            id_user = result.id;
            sessionStorage.setItem('id_user', id_user);
            alert('Successful registration Welcome!');
            location.href = "books";
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});