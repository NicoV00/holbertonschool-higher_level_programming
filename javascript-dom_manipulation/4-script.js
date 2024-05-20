const mylist = document.querySelector(".my_list");
const addItem = document.getElementById("add_item");

function add_item() {
  const new_item = document.createElement("li");
  new_item.textContent = "Item";
  mylist.appendChild(new_item);
}

addItem.addEventListener("click", add_item);
