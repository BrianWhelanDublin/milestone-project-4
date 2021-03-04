// code to update quantity of item in cart
let updateLink = document.querySelector(".update-quantity-link");

updateLink.addEventListener("click",()=>{
    let form = document.querySelector(".cart-quantity-form");
    form.submit();
})

// code to remove items from the cart
let removeLink = document.querySelector(".remove-cart-item");

removeLink.addEventListener("click", ()=>{
    let csrfToken = "{{ csrf_token }}";
    let item_id = removeLink.getAttribute("id").split("remove_")[1];
    let url = `/cart/remove/${item_id}`
    let data = {"csrfmiddlewaretoken": csrfToken}

    fetch(url, {
        body: data,
        method: "post"
    }).then(()=>{
        location.reload();
    })
})