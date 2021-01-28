var modal = document.getElementById("popupmic");
var modal1 = document.getElementById("popuptext");
var btn = document.getElementById("mike");
var btn1 = document.getElementById("texty");


var span = document.getElementsByClassName("close")[0];
var span1 = document.getElementsByClassName("closee")[0];

btn1.onclick = function(){
modal1.style.display = "block";
}


span.onclick = function() {
modal.style.display = "none";
}
span1.onclick = function() {
modal1.style.display = "none";
}

window.onclick = function(event) {
if (event.target == modal) {
modal.style.display = "none";
}
}

window.onclick = function(event) {
if (event.target == modal1) {
modal1.style.display = "none";
}
}
const speechRecognition  = window.webkitSpeechRecognition;

const Recognition = new speechRecognition();

Recognition.onstart = function (){
console.log('voice is activated');
}
var x = false;
Recognition.onresult = function(event){
  const current = event.resultIndex;
  const transcript = event.results[current][0].transcript;
  if (transcript.includes('time') == true){
    var d = new Date();
    var time =  d.getHours() + ' : ' + d.getMinutes();
    console.log('The current time is ' + time);
    read('The current time is ' + time)
  }
  else{
    console.log(event)
    modal.style.display = "none";
    console.log(transcript);
    after(transcript)
  }
};

function after (transcript){
fetch(`${window.origin}/speak`, {
  method: "POST",
  credentials: "include",
  body: JSON.stringify(transcript),
  cache: "no-cache",
  headers: new Headers({
    "content-type": "application/json"
  })
})
.then(function(response) {
if (response.status !== 200) {
 console.log(`Looks like there was a problem. Status code: ${response.status}`);
 return;
}
response.json().then(function(data) {
 const current = data.resultIndex;
 mess = data[0].message
 read(mess);
 console.log(data[0].message);
});
})
.catch(function(error) {
console.log("Fetch error: " + error);
});
};






btn.addEventListener('click',() => {
Recognition.start();
modal.style.display = "block";
});

function read(mess){
const speech = new SpeechSynthesisUtterance();
speech.text = mess;
speech.volume = 1;
speech.pitch = 1;
speech.rate = 1;
window.speechSynthesis.cancel();
window.speechSynthesis.speak(speech)
}
