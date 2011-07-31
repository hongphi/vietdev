function like(type, id) {
	if ($('#q_' + id).hasClass('like')) {
		var url = "/qna/like/" + type + "/" + id;
		$.get(url, function (data) {			
			$('#q_' + id).removeClass('like');
			$('#q_' + id).addClass('unlike');
			$('#q_' + id).find('.status').text("Unlike");
			$('#q_' + id).find('.total').text(data);
		});
		
	} else {
		var url = "/qna/unlike/" + type + "/" + id;
		$.get(url, function (data) {			
			$('#q_' + id).removeClass('unlike');
			$('#q_' + id).addClass('like');
			$('#q_' + id).find('.status').text("Like");
			$('#q_' + id).find('.total').text(data);
		});
	}		
}