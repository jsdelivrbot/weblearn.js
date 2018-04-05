var dayList="[";
for (var t = 1; t<32; t++){
	dayList = dayList + "[" + t + "],";
}
dayList = dayList.substring(0,dayList.length-1);
dayList = dayList+"]"
for(var i = 1; i<32; i++){
	var inputString = 'Stock price on day ' + i.toString() + ':<input type="text" id="'+ i.toString() + '"></input><br />';
	var htmlObject = htmlToElement(inputString);
	var myDiv = document.getElementById("myDiv");
	myDiv.appendChild(htmlObject);
	document.getElementById(i.toString()).value = i.toString();
}
document.getElementById("myDiv").appendChild(htmlToElement('<button id="submitButton" onclick="execute()">Get Predicted Stock Value on day 32</button><br />Predicted stock price for the 32nd day:'));

function execute(){
	var inputArray = Array(31);
	for(var j = 0; j<31; j++){
		var inputVal = (document.getElementById((j+1).toString())).value;
		inputArray[j]="["+inputVal+"]";
	}
	var params = "["+dayList+",";
	params = params + "["+inputArray.toString()+"],";
	params = params + "32]";
	weblearn('linear_regression',params);
}

//weblearn(funcID,params);

function acceptWeblearnResult(param){
    var resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "";
    resultDiv.appendChild(htmlToElement(param.toString()));
}

function htmlToElement(html) {
    var template = document.createElement('template');
    html = html.trim(); // Never return a text node of whitespace as the result
    template.innerHTML = html;
    return template.content;
}