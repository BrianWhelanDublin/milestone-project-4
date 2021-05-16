// New-in stock slider
window.onload = () =>{
let rightArrow = document.querySelector("#arrow-right");
let leftArrow = document.querySelector("#arrow-left");
let newItemSlider = document.querySelector(".new-item-slider");
let slide = document.querySelector(".item-container");
let slidesAmount = newItemSlider.getElementsByTagName("li").length;
let slideWidth = slide.offsetWidth;
let sliderWidth = newItemSlider.clientWidth;
let sliderMaxLength = slidesAmount * slideWidth;
let lastSlide = sliderMaxLength - sliderWidth - slideWidth;

rightArrow.addEventListener("click", () => {
    newItemSlider.scrollLeft += slideWidth;
    leftArrow.classList.add("arrow-active");
    if (newItemSlider.scrollLeft >= lastSlide) {
        rightArrow.classList.remove("arrow-active");
    }
});

leftArrow.addEventListener("click", () => {
    newItemSlider.scrollLeft -= slideWidth;
    if (newItemSlider.scrollLeft <= slideWidth) {
        leftArrow.classList.remove("arrow-active");
    }
    rightArrow.classList.add("arrow-active");
});
}


// change top navigation colour on scroll
window.addEventListener("scroll", () => {
    let topNavigation = document.querySelector(".top-navigation");
    if (window.scrollY >= 100) {
        topNavigation.classList.add("top-nav-colored");
    } else {
        topNavigation.classList.remove("top-nav-colored");
    }
});