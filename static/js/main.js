// change top navigation colour on scroll
window.addEventListener("scroll", () => {
    let topNavigation = document.querySelector(".top-navigation");
    if (window.scrollY >= 100) {
        topNavigation.classList.add("top-nav-colored")
    } else {
        topNavigation.classList.remove("top-nav-colored")
    }
})

// show side nav when hamburger clicked
let hamburger = document.querySelector(".hamburger")
let sideNav = document.querySelector(".side-nav")
let navClose = document.querySelector(".nav-close")
let sideMenu = document.querySelector(".side-nav-menu")
hamburger.addEventListener("click", () => {
    sideNav.classList.add("side-nav-show")
    sideMenu.classList.add("side-menu-open")
    sideMenu.classList.remove("side-menu-close")
})

// show furniture sublist
let furnitureLink = document.querySelector(".furniture-nav-link")
let furnitureSubList = document.querySelector(".furniture-sublist")
furnitureLink.addEventListener("click", () => {
    furnitureSubList.classList.toggle("sublist-show")
})

// show search sublist
let searchNavLink = document.querySelector(".search-navlink")
let searchSubList = document.querySelector(".search-sublist")
searchNavLink.addEventListener("click", () => {
    searchSubList.classList.toggle("sublist-show")
})

// close navbar when the close button is clicked
navClose.addEventListener("click", () => {
    sideMenu.classList.remove("side-menu-open")
    sideMenu.classList.add("side-menu-close")
    if (furnitureSubList.classList.contains("sublist-show")) {
        furnitureSubList.classList.remove("sublist-show")
    }
    if (searchSubList.classList.contains("sublist-show")) {
        searchSubList.classList.remove("sublist-show")
    }
    setTimeout(() => {
        sideNav.classList.remove("side-nav-show")
    }, 500)
})


// animation on scroll same code used in my milestone 2 project
const animationOnScroll = () => {
    let animationElement = document.querySelectorAll(".animation-element");
    animationElement.forEach((element) => {
        // Code taken from the tutorial
        let position = element.getBoundingClientRect().top;
        let screenPosition = window.innerHeight / 1.2;
        if (position < screenPosition) {
            element.classList.add("animation-active");
        }
    });
};
// call function when window is scrolled
window.addEventListener("scroll", animationOnScroll);

// Code from Bootstrap to initialize the toasts
let toastElList = [].slice.call(document.querySelectorAll('.toast'))
let toastList = toastElList.map(function (toastEl) {
    return new bootstrap.Toast(toastEl)
})
toastList.forEach((toast) => {
    toast.show()
})