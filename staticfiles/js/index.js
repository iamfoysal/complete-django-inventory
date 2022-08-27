//  Message section
const message = document.querySelector('.message');
if (message) {
   setTimeout(() => {
     message.classList.add("message-hide");
   }, 5000);
}


//index page styling control

document.querySelector(".jsFilter").addEventListener("click", function () {
    document.querySelector(".filter-menu").classList.toggle("active");
  });
  
  document.querySelector(".grid").addEventListener("click", function () {
    document.querySelector(".list").classList.remove("active");
    document.querySelector(".grid").classList.add("active");
    document.querySelector(".products-area-wrapper").classList.add("gridView");
    document
      .querySelector(".products-area-wrapper")
      .classList.remove("tableView");
  });
  
  document.querySelector(".list").addEventListener("click", function () {
    document.querySelector(".list").classList.add("active");
    document.querySelector(".grid").classList.remove("active");
    document.querySelector(".products-area-wrapper").classList.remove("gridView");
    document.querySelector(".products-area-wrapper").classList.add("tableView");
  });
  
  
