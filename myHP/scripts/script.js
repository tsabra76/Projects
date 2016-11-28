var mainImage = document.getElementById("mainImage");
var sub = document.getElementById("subtext");

var imageArray = ["images/one.jpg", "images/two.jpg", "images/three.jpg", "images/four.jpg", "images/five.jpg", "images/six.jpg", "images/seven.jpg", "images/eight.jpg"];
var textArray = ["Mt Diablo Park","Seals sunning themselves on the pier","Mt Diablo Park, overlooking Concord", "Sailboat on the Bay", "San Francisco skyline from the Bay", "Seals hanging out on the piers in San Francisco", "Southern shoreline of Alameda","Sunset on the Bay"];

var imageIndex = 0;
var textIndex = 0;

function changeImage() {
	mainImage.setAttribute("src", imageArray[imageIndex]);
	imageIndex++;
	sub.innerHTML = textArray[textIndex];
	textIndex++;
	
	if (imageIndex >= imageArray.length) {
		imageIndex = 0;
		textIndex = 0;
		}
}

window.onload = function() {
  setInterval(changeImage, 10000);
}

