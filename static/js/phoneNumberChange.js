firebase.initializeApp(firebaseConfig);
let ui = new firebaseui.auth.AuthUI(firebase.auth());
ui.start('#firebaseui-auth-container', {
    callbacks: {
        signInSuccessWithAuthResult: function (authResult,) {
            let user = authResult.user;
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);

                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            var csrftoken = getCookie('csrftoken');
            fetch($('#firebaseui-auth-container').attr('data-url2'), {
                method: 'POST',
                credentials: 'include',
                body: JSON.stringify({'phone_number':user.phoneNumber}),
                headers: new Headers({
                    'X-CSRFToken': csrftoken,
                })
            })

            return true
        }
    },

    // signInSuccessUrl: $('#firebaseui-auth-container').attr('data-url3'),
    signInSuccessUrl: '/users/phone-number-change-done/',
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
