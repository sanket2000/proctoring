console.log("Hello world");
function myFunction() {
	var txt = "";
	txt += "<p>innerWidth: " + window.innerWidth + "</p>";
	txt += "<p>innerHeight: " + window.innerHeight + "</p>";
	txt += "<p>outerWidth: " + window.outerWidth + "</p>";
	txt += "<p>outerHeight: " + window.outerHeight + "</p>";
	txt += "<p>ScreenX: " + window.screenX + "</p>";
	txt += "<p>ScreenY: " + window.screenY + "</p>";

	document.getElementById("screenSize").innerHTML = txt;
	console.log("Hello world");
}