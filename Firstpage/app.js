const text = document.querySelector(".title");
const changeColor = document.querySelector(".changeColor");
const userList = document.querySelectorAll(".name-list li");

changeColor.addEventListener("click", function () {
  changeColor.classList.toggle("klik");
});

for (user of userList) {
  user.addEventListener("click", function () {
    this.classList.toggle("klik");
  });
}
