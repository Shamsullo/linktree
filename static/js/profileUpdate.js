
    $(document).ready(function(){
        $('.js-edit, .js-save').on('click', function(){
            var $form = $(this).closest('form');
            $form.toggleClass('is-readonly is-editing');
            var isReadonly  = $form.hasClass('is-readonly');
            $form.find('input,textarea').prop('disabled', isReadonly);
        });
    });

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

    function updateFirstName() {
        fetch($('#first_name').attr('action'), {
            method: 'PUT',
            credentials: 'include',
            body: JSON.stringify({'first_name':$('#first_name_input').val()}),
            headers: new Headers({
                'X-CSRFToken': csrftoken,
            })
        })
    }

    function updateLastName() {
        fetch($('#last_name').attr('action'), {
            method: 'PUT',
            credentials: 'include',
            body: JSON.stringify({'last_name':$('#last_name_input').val()}),
            headers: new Headers({
                'X-CSRFToken': csrftoken,
            })
        })
    }

