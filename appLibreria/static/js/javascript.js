$(document).ready(function() {
    $('#loginButton').click(function() {
        let email = $('#loginEmail').val();
        let password = $('#loginPassword').val();

        if(!validateEmail(email)) {
            alert('El correo electrónico no es válido');
            $('#loginEmail').css('border', '1px solid red');
        } else {
            $('#loginEmail').css('border', '1px solid green');
        }

        if(password.length >= 8) {
            $('#loginPassword').css('border', '1px solid green');
        } else {
            $('#loginPassword').css('border', '1px solid red');
            alert('La contraseña debe tener al menos 8 caracteres');
        }
    });



    $('#signupButton').click(function() {
        let email = $('#signupEmail').val();
        let password = $('#signupPassword').val();

        if(!validateEmail(email)) {
            alert('El correo electrónico no es válido');
            $('#signupEmail').css('border', '1px solid red');
        } else {
            $('#signupEmail').css('border', '1px solid green');
        }

        if(password.length >= 8) {
            $('#signupPassword').css('border', '1px solid green');
        } else {
            $('#signupPassword').css('border', '1px solid red');
            alert('La contraseña debe tener al menos 8 caracteres');
        }
    });

    function validateEmail(email) {
        let expReg = /^[a-z0-9!#$%&'+/=?^_{|}~-]+(?:\.[a-z0-9!#$%&'+/=?^_{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
        return expReg.test(email);
    }
});
