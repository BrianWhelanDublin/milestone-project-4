let stripePublicKey = document.querySelector("#id_stripe_public_key").innerHTML.slice(1, -1);

let clientSecret = document.querySelector("#id_client_secret").innerHTML.slice(1,-1);

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

let card = elements.create("card", {style:style});
card.mount("#card-element")