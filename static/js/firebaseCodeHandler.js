
console.log('Number:', sessionStorage.getItem('phone_number'))
document.getElementById("phone-number").innerHTML = sessionStorage.getItem('phone_number');

firebase.initializeApp(firebaseConfig);
firebase.analytics();

window.recaptchaVerifier = new firebase.auth.RecaptchaVerifier('sign-in-button', {
    'size': 'invisible',
    'callback': (response) => {
        onSignInSubmit();
    }
});

const appVerifier = window.recaptchaVerifier;
document.getElementById('sign-in-button').click()
console.log('hello')


firebase.auth().signInWithPhoneNumber(sessionStorage.getItem('phone_number'), appVerifier)
    .then((confirmationResult) => {
        console.log('hello from confirmation')
        window.confirmationResult = confirmationResult;
        localStorage.removeItem('for_sms');
    }).catch((error) => {
        console.log('another hello')
        console.log(error)
    window.recaptchaVerifier.render().then(function (widgetId) {
        grecaptcha.reset(widgetId);
    })
});


function codeConfirmation() {
    const code = document.getElementById('form_input_id').value
    confirmationResult.confirm(code).then((result) => {
        window.location.href = $("#redirect_page").attr("data-url")
        const user = result.user;
        console.log("user:", user)
        // user.getIdToken(true).then(function (user_token) {
        //     localStorage.setItem('user_token', user_token)
        // })
    }).catch((error) => {
        alert('код неправильный')
    });
}
