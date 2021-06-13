// javascript to add items and remove items from the wishlist.

let wishlistButton = document.querySelectorAll(".wishlist-btn-add");
if (wishlistButton){
wishlistButton.forEach((button) => {
        button.addEventListener("click", (event) => {
            event.preventDefault();
            let itemId = button.getAttribute("id").split("wish_")[1];
            let url = `/wishlist/add/${itemId}/`;
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
        });
    });
}

let wishlistLikedButton = document.querySelectorAll(".wishlist-btn-liked");
if (wishlistLikedButton){
 wishlistLikedButton.forEach((button) => {
        button.addEventListener("click", (event) => {
            event.preventDefault();
            let itemId = button.getAttribute("id").split("liked_")[1];
            let url = `/wishlist/remove/${itemId}/`;
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
        });
    });
}


let editButton = document.querySelector(".edit");
let deleteButton = document.querySelector(".delete-wishlist");
if (editButton){
editButton.addEventListener("click", ()=>{
    deleteButton.classList.toggle("hidden-button");
     wishlistLikedButton.forEach((button)=>{
         button.classList.toggle("hidden-button");
     });
});
}
