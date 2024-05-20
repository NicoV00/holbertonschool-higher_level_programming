const toggleHeader = document.querySelector("#toggle_header");
const header = document.querySelector("header");

function chColors() {
  header.classList.toggle("red");
  header.classList.toggle("green");
}

toggleHeader.addEventListener("click", chColors);
