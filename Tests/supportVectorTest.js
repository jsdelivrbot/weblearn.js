var params = "[[[-1, -1], [-2, -1], [1, 1], [2, 1]],[1, 1, 2, 2],[-0.8, -1]]";
var funcID = "support_vector_machine";
weblearn(funcID,params);
function acceptWeblearnResult(param){
	console.log(param);
}