// https://www.kirupa.com/html5/accessing_your_webcam_in_html5.htm
var video = document.querySelector("#videoElement");

function vid(video) {
  if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(function (stream) {
        video.srcObject = stream;
        console.log("Something went right!");
      })
      .catch(function (err0r) {
        console.log("Something went wrong!");
      });
  }
}

vid(video)