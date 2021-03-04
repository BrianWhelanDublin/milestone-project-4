// code to update quantity of item in cart
let updateLink = document.querySelectorAll(".update-quantity-link");

updateLink.forEach((link)=>{
link.addEventListener("click",()=>{
    let form = link.previousElementSibling
    form.submit()
})
})



// code to remove items from the cart
let removeLink = document.querySelectorAll(".remove-cart-item");

removeLink.forEach((link)=>{
    link.addEventListener("click", ()=>{
    let csrfToken = "{{ csrf_token }}";
    let itemId = link.getAttribute("id").split("remove_")[1];
    let url = `/cart/remove/${itemId}`
    let data = {"csrfmiddlewaretoken": csrfToken}

    fetch(url, {
        body: data,
        method: "POST"
    }).then(()=>{
     
      location.reload();
    })
})
})
