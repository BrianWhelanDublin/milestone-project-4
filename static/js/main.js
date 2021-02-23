// show side nav when hamburger clicked
let hamburger = document.querySelector(".hamburger")
let sideNav = document.querySelector(".side-nav")
let navClose = document.querySelector(".nav-close")


hamburger.addEventListener("click", ()=>{
    sideNav.classList.add("side-nav-show")
})
navClose.addEventListener("click", () => {
        sideNav.classList.remove("side-nav-show")
})