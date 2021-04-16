MicroModal.init({
  openClass: 'is-open',
  disableScroll: true,
});

if ($(window).width() < 768) {
  $('.taplink__click').html('Получите ссылку' + '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">\n' +
      '                                             <path fill-rule="evenodd" clip-rule="evenodd"\n' +
      '                                                 d="M17.5858 13.0001H4C3.44772 13.0001 3 12.5524 3 12.0001C3 11.4478 3.44772 11.0001 4 11.0001H17.5858L12 5.41429C11.6095 5.02376 11.6095 4.3906 12 4.00008C12.3905 3.60955 13.0237 3.60955 13.4142 4.00008L20.7071 11.293C21.0976 11.6835 21.0976 12.3167 20.7071 12.7072L13.4142 20.0001C13.0237 20.3906 12.3905 20.3906 12 20.0001C11.6095 19.6096 11.6095 18.9764 12 18.5859L17.5858 13.0001Z"\n' +
      '                                                 fill="#374257"/>\n' +
'                                                 </svg>')
}

$('.form__eye').on('click', function () {
  if ($(this).siblings('.form__input').attr('type') === 'password') {
    $(this).addClass('active');
    $(this).siblings('.form__input').attr('type', 'text');
  } else {
    $(this).removeClass('active');
    $(this).siblings('.form__input').attr('type', 'password');
  }
})
