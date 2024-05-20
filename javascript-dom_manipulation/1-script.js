const header = document.querySelector("header");
const divss = document.querySelector("div");

function changeRed() {
  header.style.color = "red";
}

divss.addEventListener("click", changeRed);
