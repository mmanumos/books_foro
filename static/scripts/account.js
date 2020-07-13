let id_user_account = sessionStorage.getItem('id_user');
console.log('id_user_account ' + id_user_account);
if (id_user_account == null) {
    location.href = "login";
}


/* Update user*/
$.ajax({
    url: 'http://localhost:5001/api/v1/users/' + id_user_account + '/',
    type: 'GET',
    success: function (result) {
        $("#username").val(result.username);
        $("#password").val(result.password);
        $("#first_name").val(result.first_name);
        $("#last_name").val(result.last_name);

    },
    error: function (myerror) {
        console.log(myerror);
    }
});


// Edit
$('#edit_user_btn').click(function () {
    console.log('Entra');
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

    let url = 'http://localhost:5001/api/v1/users/' + id_user_account + '/';
    $.ajax({
        type: "PUT",
        url: url,
        data: JSON.stringify(user),
        ContentType: 'Application/json',
        success: function (result) {
            console.log(result);
            if (result) {
                alert('User is updated');
                window.location.href = "account";
            }
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});

/* Delete user*/
$('#delete_user_btn').click(function () {
    console.log('entra');
    let url = 'http://localhost:5001/api/v1/users/' + id_user_account + '/';
    $.ajax({
        type: "DELETE",
        url: url,
        success: function (result) {
            console.log(result);
            alert('Account has been deleted');
            location.href = "login";
        },
        error: function (myerror) {
            console.log(myerror);
        }
    });
});