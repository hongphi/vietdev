function like(type, id) {
	if ($('#' + type + '_' + id).hasClass('like')) {
		var url = "/qna/like/" + type + "/" + id;
		$.get(url, function (data) {
			$('#' + type + '_' + id).removeClass('like');
			$('#' + type + '_' + id).addClass('unlike');
			$('#' + type + '_' + id).find('.status_like').text("unlike");
			$('#' + type + '_' + id).find('.total').text(data);
            $('#q_' + id).find('.mini-counts').text(data)
		});

	} else {
		var url = "/qna/unlike/" + type + "/" + id;
		$.get(url, function (data) {
			$('#' + type + '_' + id).removeClass('unlike');
			$('#' + type + '_' + id).addClass('like');
			$('#' + type + '_' + id).find('.status_like').text("like");
			$('#' + type + '_' + id).find('.total').text(data);
            $('#q_' + id).find('.mini-counts').text(data)
		});
	}
}

$(document).ready(function(){
    $('#markItUp').markItUp(mySettings);
});
