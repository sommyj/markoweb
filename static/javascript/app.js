var category = document.getElementsByName('category');

category[0].onclick = function(){
    category[0].classList.add('active');
    category[1].firstElementChild.setAttribute("src", "../images/goat (1).png");
    category[0].firstElementChild.setAttribute("src", "../images/growth (1).png");

    category[1].classList.remove('active');

    var prodCate = document.querySelector(".product-category").style.left ="0";
}

category[1].onclick = function(){
    category[1].classList.add('active');
    category[1].firstElementChild.setAttribute("src", "../images/goat (2).png");
    category[0].firstElementChild.setAttribute("src", "../images/growth (2).png");
    category[0].classList.remove('active');
    var prodCate = document.querySelector(".product-category").style.left ="-100%";

}
