firebase.initializeApp(firebaseConfig);
let user_phone_number = ''

let ui = new firebaseui.auth.AuthUI(firebase.auth());
ui.start('#firebaseui-auth-container', {
    callbacks: {
        signInSuccessWithAuthResult: function (authResult) {
            let user = authResult.user;
            document.getElementById("form_div").hidden = false;
            user_phone_number = user.phoneNumber;
            return false;
        }
    },
    signInOptions: [
        {
            provider: firebase.auth.PhoneAuthProvider.PROVIDER_ID,
            recaptchaParameters: {
                size: 'normal',
            },
            defaultCountry: 'KG',
        },
    ],
});

// Asynchronously check if the user exist
$(document).ready(function () {
    $(document).on(
        'input',
        'input[name=phoneNumber]',
        debounce(function (e) {
            let elements = document.getElementsByClassName('firebaseui-id-country-selector-code')
            let phone = elements['0'].innerHTML + e.target.value
            $.ajax({
                type: 'GET',
                url: $('#firebaseui-auth-container').attr('data_url'),
                data: {"phoneNumber": phone},
                success: function (response) {
                    if (response["is_taken"]) {
                        alert("User with this number already exist");
                    } 
                },
                error: function (response) {
                    console.log(response)
                }
            })

        }, 800)
    );

    function debounce(callback, delay) {
        let timeout;
        return function () {
            let args = arguments;
            clearTimeout(timeout);
            timeout = setTimeout(
                function () {
                    callback.apply(this, args);
                }.bind(this),
                delay
            );
        };
    }
});
