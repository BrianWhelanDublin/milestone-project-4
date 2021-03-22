// New-in stock slider
let rightArrow = document.querySelector("#arrow-right");
let leftArrow = document.querySelector("#arrow-left");
let newItemSlider = document.querySelector(".new-item-slider")

let mediaQuery = window.matchMedia('(max-width: 1200px)')

rightArrow.addEventListener("click", () => {
    if (mediaQuery.matches) {
        newItemSlider.scrollLeft += 290;
    } else {
        newItemSlider.scrollLeft += 440;
    }
    leftArrow.classList.add("arrow-active");
    if (newItemSlider.scrollLeft >= 2500) {
        rightArrow.classList.remove("arrow-active")
    }
})
leftArrow.addEventListener("click", () => {
    if (mediaQuery.matches) {
        newItemSlider.scrollLeft -= 290;
        if (newItemSlider.scrollLeft <= 290) {
            leftArrow.classList.remove("arrow-active")
        }
    } else {
        newItemSlider.scrollLeft -= 440;
        if (newItemSlider.scrollLeft <= 440) {
            leftArrow.classList.remove("arrow-active")
        }
    }
    rightArrow.classList.add("arrow-active");
})


// change top navigation colour on scroll
window.addEventListener("scroll", () => {
    let topNavigation = document.querySelector(".top-navigation");
    if (window.scrollY >= 100) {
        topNavigation.classList.add("top-nav-colored")
    } else {
        topNavigation.classList.remove("top-nav-colored")
    }
})
