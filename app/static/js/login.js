
bootstrap_alert = function() {}
bootstrap_alert.warning = function(message) {
            $('#alert_placeholder').html('<div class="alert"><a class="close" data-dismiss="alert">×</a><span>'+message+'</span></div>')
        };
 $(document).ready({
   $('#loginForm').submit(function(){
		var email = $('#email').val();
		var pass = $('#password').val();
		$.ajax({
			url: '/loginUser',
			data: 'json',
			type: 'POST',
			success: function(response){
			    console.log(response);
				bootstrap_alert.warning(response.status);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});

