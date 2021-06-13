// change top navigation colour on scroll

window.addEventListener("scroll", () => {
    let topNavigation = document.querySelector(".top-navigation");
    if (window.scrollY >= 100) {
        topNavigation.classList.add("top-nav-colored");
    } else {
        topNavigation.classList.remove("top-nav-colored");
    }
});

// new items slider code inspired by The WebShala on youtube details in readme.

const container = document.querySelector(".new-item-slider");
const allItems = document.querySelectorAll(".new-item-slide");
const firstItem = document.querySelector(".new-item-slide");
const rightArrow = document.querySelector("#arrow-right");
const leftArrow = document.querySelector("#arrow-left");
const itemWidth = firstItem.clientWidth;
const margin = 20;
let items = 0;
let jumpSlideWidth = 0;
let slider = document.querySelector(".new-item-slider-container");
let sliderWidth = slider.offsetWidth;

let breakPoints = [
    { breakPoint: { width: 0, item: 1 } }, 
    { breakPoint: { width: 760, item: 2 } },
    { breakPoint: { width: 992, item:3 } },
    { breakPoint: { width: 1400, item: 4 } }, 
];

const load = () => {
    breakPoints.forEach(el => {
        if (window.innerWidth > el.breakPoint.width) {
            items = el.breakPoint.item;
        }
    });
    setItemsMargins();
};

const setItemsMargins = () => {
    allItems.forEach(el => {
       el.style.margin = (margin / 2) + "px";
    });
};

rightArrow.addEventListener("click", () => {
    let totalWidth = sliderWidth * (allItems.length / items);
    if (rightArrow.classList.contains("clickable")) jumpSlideWidth = jumpSlideWidth + (itemWidth + margin);
    if (jumpSlideWidth > 0) leftArrow.classList.add("clickable");
    if (jumpSlideWidth < (totalWidth)) container.style.marginLeft = -jumpSlideWidth + "px";
    if ((jumpSlideWidth >= (totalWidth - sliderWidth)) && (jumpSlideWidth < (totalWidth))) rightArrow.classList.remove("clickable");
});

leftArrow.addEventListener("click", () => {
    if (leftArrow.classList.contains("clickable")) jumpSlideWidth = jumpSlideWidth - (itemWidth + margin);
    if (jumpSlideWidth >= 0) {
        container.style.marginLeft = -jumpSlideWidth + "px";
        rightArrow.classList.add("clickable");
    }
    if (jumpSlideWidth == 0) leftArrow.classList.remove("clickable");
});

load();
