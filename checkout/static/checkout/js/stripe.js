// javascript to set up the stripe card element using the stripe documentation.

let stripePublicKey = document.querySelector("#id_stripe_public_key").innerHTML.slice(1, -1);

let clientSecret = document.querySelector("#id_client_secret").innerHTML.slice(1, -1);

let stripe = Stripe(stripePublicKey);

let elements = stripe.elements();

let style = {
    base: {
        color: "#000",
        fontFamily: "'Roboto', sans-serif",
        fontSmoothing: "antialiased",
        fontSize: "14px",
        "::placeholder": {
            color: "rgba(21, 50, 67, .7)"

        }
    },
    invalid: {
        color: "#dc3545",
        iconColor: "#dc3545"
    }
};

let card = elements.create("card", {
    style: style
});

card.mount("#card-element");

// Javascript to handle realtime errors

card.addEventListener("change", (event) => {
    let errorDisplay = document.querySelector("#card-errors");
    if (event.error) {
        let markup = `
            <p class="fs-5 mt-1">
            <i class="las la-exclamation-circle fs-5" aria-hidden="true"></i>
            ${event.error.message}</p>`;
        errorDisplay.innerHTML = markup;
    } else {
        errorDisplay.textContent = "";
    }
});


let form = document.querySelector('#checkout-form');
form.addEventListener('submit', (event) => {
    event.preventDefault();
    card.update({
        "disabled": true
    });

    document.querySelector("#checkout_submit").setAttribute("disabled", true);
    document.querySelector(".loading").classList.add("loading-show");
    let saveButton = document.querySelector("#save-info");
    let saveInfo = false;
    if (saveButton) {
        saveInfo = Boolean(saveButton.hasAttribute("checked"));
    }

    let csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value;

    let postData = new FormData();
    postData.set("csrfmiddlewaretoken", csrfToken);
    postData.set("client_secret", clientSecret);
    postData.set("save_info", saveInfo);
    let url = "/checkout/cache_checkout_data/";
    // stack overflow  code to help with the fetch and CSRF tokens
    fetch(url, {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
        },
        body: postData
    }).then(() => {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: form.full_name.value.trim(),
                    phone: form.contact_number.value.trim(),
                    email: form.email.value.trim(),
                    address: {
                        line1: form.street_address_1.value.trim(),
                        line2: form.street_address_2.value.trim(),
                        city: form.town_or_city.value.trim(),
                        country: form.country.value.trim(),
                        state: form.county.value.trim(),
                    }
                }
            },
            shipping: {
                name: form.full_name.value.trim(),
                phone: form.contact_number.value.trim(),
                address: {
                    line1: form.street_address_1.value.trim(),
                    line2: form.street_address_2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    country: form.country.value.trim(),
                    postal_code: form.eircode.value.trim(),
                    state: form.county.value.trim(),
                }
            },
        }).then((result) => {
            let errorDisplay = document.querySelector("#card-errors");
            if (result.error) {
                let markup = `
                    <p class="fs-5 mt-1 text-danger">
                    <i class="las la-exclamation-circle fs-5" aria-hidden="true"></i> ${result.error.message}</p>`;
                errorDisplay.innerHTML = markup;
                document.querySelector(".loading").classList.remove("loading-show");
                card.update({
                    "disabled": false
                });
                document.querySelector("#checkout_submit").removeAttribute("disabled");
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).catch((error) => {
        location.reload();
    });
});