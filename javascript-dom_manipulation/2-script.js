const header = document.querySelector("header");
const divss = document.querySelector("div");

function changeRed() {
  header.classList.add("red");
}

divss.addEventListener("click", changeRed);
