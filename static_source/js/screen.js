$(document).ready(function() {

    $('html').ajaxSend(function(event, xhr, settings) {
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
    });

    $('.download_btn').click( function() {
        $(this).hide();
        $('.download_msg').show();
        var t=setTimeout("downloadIt()", 3000);
        return false;
    });

    $('#ifile_url').focus( function() {
		$(this).select();
	});
    $('#ifile_url').mouseup( function(e) {
        e.preventDefault();
	});

    $('#form_check_link').submit( function() {
        var ifile_url = $('#ifile_url').val();
        if (ifile_url) {
            $.ajax({
                type: 'GET',
                url: '/check/ifile_url',
                data: {
                    ifile_url: ifile_url
                },
                beforeSend:function() {
                    $(".loader").show();
                    $('#btn_check_link').hide();
                },
                success:function(data){
                    $(".loader").hide();
                    if(data==1) {
                        var $lefty = $('#form_check_link').next();
                        $lefty.animate({
                          left: parseInt($lefty.css('left'),10) == 0 ? -$lefty.outerWidth() : 0
                        });
                    }
                }
            });
        }
        return false;
    });
});

function downloadIt() {
    window.location = $('#direct_url').val();
}

