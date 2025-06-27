const video = document.getElementById("video");
const canvas = document.getElementById("canvas");
const result = document.getElementById("result");

// Start webcam
navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
  video.srcObject = stream;
});

setInterval(() => {
  const context = canvas.getContext("2d");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  context.drawImage(video, 0, 0, canvas.width, canvas.height);
  const dataUrl = canvas.toDataURL("image/jpeg");

  fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ image: dataUrl }),
  })
    .then((response) => response.json())
    .then((data) => {
      result.innerText = data.emotion;
    });
}, 2000);
