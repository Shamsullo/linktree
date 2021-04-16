let timerBlock = $('.timer__seconds');
var num = 59;

var index = num;
var timerId = setInterval(function () {
    timerBlock.html(--index);
    if (index < 10) {
        timerBlock.prepend(0);
    }
}, 1000);

setTimeout(function () {
    clearInterval(timerId);
    $('.sms__timer').html('Отправить снова').removeAttr('disabled').addClass('active')
}, num * 1000);
