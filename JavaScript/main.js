var head = document.getElementsByTagName("head");
head = head[0];
head.appendChild(createElementFromHTML("<script src='https://www.gstatic.com/firebasejs/4.12.0/firebase.js'></script>"));
var config = {
    apiKey: "AIzaSyC2hKva7INTFpaEia78duupQXL4XqZN3Ic",
    authDomain: "weblearn-js.firebaseapp.com",
    databaseURL: "https://weblearn-js.firebaseio.com",
    projectId: "weblearn-js",
    storageBucket: "weblearn-js.appspot.com",
    messagingSenderId: "356304795464"
  };
  firebase.initializeApp(config);
function weblearn(func,params){
    postToDB(func,params);
    return [[1,1,1][2,2,2][3,3,3]];
}

function postToDB(func,params){
    firebase.database().ref(func+"/input").set(params);
}

function getOutput(func, earlierOutput){
    
}

function createElementFromHTML(htmlString) {
  var div = document.createElement('div');
  div.innerHTML = htmlString.trim();

  // Change this to div.childNodes to support multiple top-level nodes
  return div.firstChild; 
}