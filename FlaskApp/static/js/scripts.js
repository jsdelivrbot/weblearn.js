function weblearn(funcID,params){
		asyncStuff(funcID,params);
}

function asyncStuff(funcID,params){
	$.ajax({
			type : "POST",
			url :'http://localhost:5000',
			data: {
				function: funcID,
				params : params
			},
			success: function(result) {
				var finalResult=result;
				//var finalResult = (stringTo1DArray(result));
				process(finalResult);
			},
			error: function(error){
				console.log(error);
			}
		});
}

function finisher(){
	return finalReturnedResult;
}

function stringTo1DArray(inputStr){
	var jsarrlen = (inputStr.length+1)/2;
	var final = new Array(jsarrlen);
	var jsarrfillcnt = 0;
	for(var i = 0; i<inputStr.length; i+=2){
		final[jsarrfillcnt]=parseInt(inputStr.charAt(i));
		jsarrfillcnt++;
	}
	return final
}

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}