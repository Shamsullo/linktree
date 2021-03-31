firebase.initializeApp(firebaseConfig);
user_phone_number = ''

let ui = new firebaseui.auth.AuthUI(firebase.auth());
ui.start('#firebaseui-auth-container', {
    callbacks: {
        signInSuccessWithAuthResult: function (authResult) {
            let user = authResult.user;
            document.getElementById("form_div").hidden = false;
            user_phone_number = user.phoneNumber 
            return false;
        }
    },
    signInOptions: [
        {
            provider: firebase.auth.PhoneAuthProvider.PROVIDER_ID,
            recaptchaParameters: {
                size: 'invisible',
            },
            defaultCountry: 'KG',
        },
    ],
});

// Asyncronicly chekc if the user exist
$(document).ready(function () {
    $(document).on(
        'input',
        'input[name=phoneNumber]',
        debounce(function (e) {
            let elements = document.getElementsByClassName('firebaseui-id-country-selector-code')
            let phone = elements['0'].innerHTML + e.target.value
            console.log(phone)
            $.ajax({
                type: 'GET',
                url: "/users/already_exist/",
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

$('label[for=id_phone_number], input#id_phone_number').hide();

window.addEventListener( "load", function () {
    function sendData() {
        phone = user_phone_number;
        first_name = $('#id_first_name').val();
        surname = $('#id_last_name').val();
        birthday = $('#id_birthday').val();
        password1 = $('#id_password1').val();
        password2 = $('#id_password2').val();
        data = {
            'phone_number': phone,
            'first_name': first_name,
            'last_name': surname,
            'birthday': birthday,
            'password1': password1,
            'password2': password2
        };

        $.ajaxSetup({ 
            beforeSend: function(xhr, settings) {
                function getCookie(name) {
                    var cookieValue = null;
                    if (document.cookie && document.cookie != '') {
                        var cookies = document.cookie.split(';');
                        for (var i = 0; i < cookies.length; i++) {
                            var cookie = jQuery.trim(cookies[i]);
                            // Does this cookie string begin with the name we want?
                            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                break;
                            }
                        }
                    }
                    return cookieValue;
                }
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    // Only send the token to relative URLs i.e. locally.
                    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                }
            } 
       });
        $.ajax({
            type: 'Post',
            url: $(form).attr('action'),
            data: this.data,
            success: function (response) {
                console.log("Form was sent");
                window.location.replace("/");
            },
            error: function (response) {
                console.log(response)
            }
        })
    }

    // Access the form element...
    const form = document.getElementById( "myForm" );

    // ...and take over its submit event.
    form.addEventListener( "submit", function ( event ) {
        event.preventDefault();
        sendData();
    } );

} );
