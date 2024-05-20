const updateHeadtxt = document.getElementById("update_header");

function updatHeader() {
  document.querySelector("header").textContent = "New Header!!!";
}

updateHeadtxt.addEventListener("click", updatHeader);
