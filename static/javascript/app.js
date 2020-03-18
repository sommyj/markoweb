
var category = document.getElementsByName('category');

category[0].onclick = function(){
  // console.log("yam");

    category[1].firstElementChild.setAttribute("src", "/static/images/goat1.png");
    category[0].firstElementChild.setAttribute("src", "/static/images/growth1.png");

    // console.log(category[0].firstElementChild.getAttribute("src"));

    category[0].classList.add('active');
    category[1].classList.remove('active');


    var prodCate = document.querySelector(".product-category").style.left ="0";
}

category[1].onclick = function(){
    category[1].firstElementChild.setAttribute("src", "/static/images/goat2.png");
    category[0].firstElementChild.setAttribute("src", "/static/images/growth2.png");

    category[1].classList.add('active');
    category[0].classList.remove('active');

    var prodCate = document.querySelector(".product-category").style.left ="-100%";

}
