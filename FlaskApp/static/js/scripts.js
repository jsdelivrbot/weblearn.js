$(function(){
	$('button').click(function(){
		var data = {"test1":"hi!"};
		$.ajax({
			type : "POST",
			url :'http://localhost:5000',
			data: data,
			success: function(result) {
				console.log(result);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
