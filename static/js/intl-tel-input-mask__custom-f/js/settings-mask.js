// settings for two mask

var telNumber = 0;
var inputPhoneMask = $('.form__input-tel');


$(window).on('load', function () {
  initMask();
  setTimeout(function () {
    telNumber = inputPhoneMask.attr('placeholder').replace(/[0-8]/g, '9');
    maskPhoneField();
  }, 500);
});

// init for intlTelInput.js

function initMask() {
  var input = $(".form__input-tel");
  input.each(function (i, obj) {
    intlTelInput(obj, {
      separateDialCode: true,
      preferredCountries: ['kg'],
      onlyCountries: ['kg', 'kz', 'ru'],
      utilsScript: utilsPath,
      nationalMode: false,
    });
    obj.addEventListener("countrychange", function () {
      $(this).val('');
      telNumber = $(this).attr('placeholder').replace(/[0-8]/g, '9');
      maskPhoneField();
    });
  })
}

// init for imask.js

function maskPhoneField() {
  inputPhoneMask.mask(telNumber);
}



// <script src="js/jquery-2.2.4.js"></script> -- 1 подключить Jquery
// <script src="intl-tel-input-mask__custom/js/intlTelInput.js"></script> -- 2 подключить intlTelInput.js
// <script src="intl-tel-input-mask__custom/js/imask.js"></script> -- 3 подключить imask.js
// <script src="intl-tel-input-mask__custom/js/settings-mask.js"></script> -- 3 подключить иницилизацию settings-mask.js
// <link rel="stylesheet" href="intl-tel-input-mask__custom/css/intlTelInput.css"> -- 4 подключить стили intlTelInput.css

// https://github.com/digitalBush/jquery.maskedinput -- ссылки для дополнительных настроек масок
// https://github.com/jackocnr/intl-tel-input.git -- ссылки для дополнительных настроек масок