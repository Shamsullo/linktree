
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


firebase.auth().signInWithPhoneNumber(sessionStorage.getItem('phone_number'), appVerifier)
    .then((confirmationResult) => {
        window.confirmationResult = confirmationResult;
        localStorage.removeItem('for_sms');
    }).catch((error) => {

    window.recaptchaVerifier.render().then(function (widgetId) {
        grecaptcha.reset(widgetId);
    })
});

function codeConfirmation() {
    const code = document.getElementById('form_input_id').value
    confirmationResult.confirm(code).then((result) => {
        window.location.href = $("#redirect_page").attr("data-url")

    }).catch((error) => {
        alert('код неправильный')
    });
}
