// places the image name underneat the add image button
let newImageInput = document.querySelector(".new-image-input");
newImageInput.addEventListener("change", ()=>{
   let file = newImageInput.files[0];
   document.querySelector("#image-name").innerHTML = `
   New Image: <span class="blue">${file.name}</span>
   `;
});