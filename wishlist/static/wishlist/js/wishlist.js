// javascript to add items and remove items from the wishlist. I placed it in the general js folder as it is being used across a number of apps

let wishlistButton = document.querySelectorAll(".wishlist-button")
    wishlistButton.forEach((button) => {
        button.addEventListener("click", (event) => {
            event.preventDefault()
            let itemId = button.getAttribute("id").split("wish_")[1];
            console.log(itemId)
            let url = `/wishlist/add/${itemId}/`
            console.log(url)
            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken
                },
            }).then(() => {
                document.location.reload();
            }).catch((error) => {
                alert("Opps something has gone wrong.");
            });
        })
    })

let wishlistLikedButton = document.querySelectorAll(".wishlist-button-liked")
    wishlistLikedButton.forEach((button) => {
        button.addEventListener("click", (event) => {
            event.preventDefault()
            let itemId = button.getAttribute("id").split("liked_")[1];
            console.log(itemId)
            let url = `/wishlist/remove/${itemId}/`
            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken
                },
            }).then(() => {
               document.location.reload();
            }).catch((error) => {
                alert("Opps something has gone wrong.");
            });
        })
    })

let editButton = document.querySelector(".edit")
let deleteButton = document.querySelector(".delete-wishlist")
editButton.addEventListener("click", ()=>{
    deleteButton.classList.toggle("hidden-button")
     wishlistLikedButton.forEach((button)=>{
         button.classList.toggle("hidden-button")
     })
  
})