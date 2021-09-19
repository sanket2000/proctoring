console.log("Hello world");

window.addEventListener("resize", myFunction);
window.addEventListener("mousemove", myFunction);

function myFunction(event) {
	var txt = "";
	txt += "<p>innerWidth: " + window.innerWidth + "</p>";
	txt += "<p>innerHeight: " + window.innerHeight + "</p>";
	txt += "<p>outerWidth: " + window.outerWidth + "</p>";
	txt += "<p>outerHeight: " + window.outerHeight + "</p>";
	txt += "<p>ScreenX: " + window.screenX + "</p>";
	txt += "<p>ScreenY: " + window.screenY + "</p>";
	txt += "<p>MouseX: " + event.offsetX + "</p>";
	txt += "<p>MouseY: " + event.offsetY + "</p>";

	document.getElementById("screenSize").innerHTML = txt;
	console.log("Hello world");
}
