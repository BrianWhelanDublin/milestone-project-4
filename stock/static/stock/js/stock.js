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

let newImageInput = document.querySelector("#new-image-input")

newImageInput.addEventListener("change", ()=>{
    let file = newImageInput[0].files[0]
    document.querySelector(".image-name").innerHTML = `
    New image: ${file.name}
    `
})