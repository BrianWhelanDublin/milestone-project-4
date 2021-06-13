// select buttons for number input
let increaseBtn = document.querySelectorAll(".plus-btn");
let decreaseBtn = document.querySelectorAll(".minus-btn");
increaseBtn.forEach((button) => {
    button.addEventListener("click", (event) => {
        let clickedButton = event.target;
        let inputContainer = clickedButton.parentElement.parentElement.children[1];
        let input = inputContainer.children[1].children[0];
        let max = input.getAttribute("max");
        let inputValue = input.value;
        let newValue = parseInt(inputValue) + 1;
        if (inputValue < max) {
            input.value = newValue;
        }
    });
});
decreaseBtn.forEach((button) => {
    button.addEventListener("click", (event) => {
        let clickedButton = event.target;
        let inputContainer = clickedButton.parentElement.parentElement.children[1];
        let input = inputContainer.children[1].children[0];
        let min = input.getAttribute("min");
        let inputValue = input.value;
        let newValue = parseInt(inputValue) - 1;
        if (inputValue > min) {
            input.value = newValue;
        }
    });
});