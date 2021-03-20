// js to sort items from select box

let sortSelector = document.querySelector("#sort-selector")

sortSelector.addEventListener("change", ()=>{
    let currentUrl = new URL(window.location);

    let selectedValue = sortSelector.value
    if(selectedValue != "reset"){
        let sort = selectedValue.split("_")[0];
        let direction = selectedValue.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    }else{
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

         window.location.replace(currentUrl);
    }
})

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