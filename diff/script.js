const uploadBtn = document.getElementById("uploadBtn");
const videoInput = document.getElementById("videoInput");
const gallery = document.getElementById("videoGallery");

uploadBtn.addEventListener("click", () => videoInput.click());

videoInput.addEventListener("change", (event) => {
  const files = event.target.files;
  gallery.innerHTML = ""; // Clear gallery before showing new videos

  Array.from(files).forEach((file) => {
    const videoURL = URL.createObjectURL(file);
    const card = document.createElement("div");
    card.classList.add("video-card");

    const video = document.createElement("video");
    video.src = videoURL;
    video.controls = true;

    card.appendChild(video);
    gallery.appendChild(card);
  });
});
