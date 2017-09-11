function alert(msg) {
	$('#alert_placeholder').html('<div class="alert"><a class="close" data-dismiss="alert">x</a><span>' + msg + '</span></div>')
	console.log(msg);
}
var alert;
bootstrap_alert = function() {}
bootstrap_alert.warning = function(message) {
            $('#alert_placeholder').html('<div class="alert"><a class="close" data-dismiss="alert">×</a><span>'+message+'</span></div>')
        };
$(function(){
	$('button').click(function(){
		var email = $('#user').val();
		var pass = $('#pass').val();
		$.ajax({
			url: '/loginUser',
			data: {'email':email, 'password': pass},
			type: 'POST',
			success: function(response){
				console.log(response);
				alert($.parseJSON(response).status);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
