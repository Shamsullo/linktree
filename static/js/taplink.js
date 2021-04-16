function copytext(el) {
    var $tmp = $("<textarea>");
    $("body").append($tmp);
    $tmp.val($(el).text()).select();
    document.execCommand("copy");
    $tmp.remove();
}

$('.copy__icon').on('click', function () {
    copytext('#taplink-link');
    $('.taplink__copy').addClass('active');
    setTimeout(function () {
        $('.taplink__copy').removeClass('active');
    }, 3000);
})
