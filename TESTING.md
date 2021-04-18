## User Stories.

- Customers
  - Website experience
    - As a customer, I would like to see what the website is selling.
        - The website has numerous reference to being a furniture store.
        - The home page has a link in its main hero section to shop the companies collection.
        - The homepage also has a new items slider to show the user what's new.
        - The user can also select different categories from the navigation.

    - As a customer, I would like to be able to navigate the website easily.
        - The main navigation has items for, the cart, account and wishlist on show at all times.
        - The main navigation is then accessed by clicking the burger menu.
        - This shows the main navigation items.
        - At different points on the site, there are buttons that link back to shopping or the checkout, etc for the user's convenience.


    - As a customer, I would like to see some information about the company.
        - The homepage contains a small snippet of information about the company.
        - The hero image contains a link to our story page which then contains more detailed information about the company.


    - As a customer, I would like to be able to contact the company.
        - In the footer that is throughout the site there are the main contact details.
        - The user can also click on the contact us here link to be brought to the contact form.

  
  - Searching for items.
    - As a customer, I would like to see all the products the company sells.
        - On the homepage, there are shop collection buttons linking to the all items page.
        - There is also a shop collection navigation link.

    - As a customer, I would like to be able to search by category.
        - The navigation menu contains a link for each category, and for the subcategories in the furniture section.
        - The user can click on these to shop for items in a particular category.

    - As a customer, I would like to be able to search through the items.
        - The navigation menu has a search form that the user can use to search through the sites stock.

    - As a customer, I would like to sort the items by price.
        - The all items page has a select input to allow the items to be sorted by price.

  - Shopping.
    - As a customer, I would like to see the product price and description.
        - Upon clicking on an item image the user is brought to the item page where the items price and description are shown.

    - As a customer, I would like to be able to add products to my shopping cart.
        - From the item page the user can click the add to cart button which will then add the item to the user's cart.

    - As a customer, I would like to be notified when I complete interactions with the site.
        - The user is notified with a popup message whenever they act on the site. 
        - The messages confirm actions as well as warnings and alerts.

    - As a customer, I would like to be able to edit my shopping cart.
        - From the cart page the user can alter the quantity or a particular item in their cart.
        - They can also delete an item if they wish to.

    - As a customer, I would like to be able to checkout easily.
        - Once the customer has an item in their cart they can then click on the checkout button to be taken to the checkout screen.
        - Once in the checkout the user then fills out a simple form and enters their card details.
        - Once this form is valid the checkout process will then be complete.

    - As a customer, I would like to receive confirmation of my order.
        - Once the user submits an order and it has been confirmed they will then be sent a confirmation email containing the order details.

  - Account.
    - As a customer, I would like to save my details to an account.
        - The user can click the save details button when checking out to save their details.
        - When the user signs up they can also save their details on the user profile page for future shopping.

    - As a customer, I would like to see my previous order details.
        - On the user's profile page there is a list of the user's previous orders.
        - When the user clicks on an order number they will be brought to the previous order page with its details.
    - As a customer, I would like to leave a review of the company.
        - The user can navigate to the review page from the review section on the homepage
        - Here they can see all the user reviews and if they are logged in a review form.
        - Once they submit the review form and it's valid their review will appear in the list.

- Website owner.

  - As the business owner, I would like to be able to edit and add products easily.
    - The superuser can add products from the admin section of the site.
    - They also have access to the stock control page on the front end of the site.
    - The items page will also show buttons for them to edit or delete an item.

  - As the business owner, I would like to be able to delete products.
    - The items section will show buttons for the superuser to delete products.
    - A modal will ask them to confirm the deletion to prevent accidental deletion.

  - As the business owner, I would like to have access to an admin section. 
     - The admin superuser has access to the admin section where they can edit and add details to the database.
     - They also will receive customer messages here.

  - As the business owner, I would like my customers to be able to shop on the site easily.
    - The site has been built with the user in mind to allow ease of flow for shopping and navigating the site.

## Unit Testing

- ### Django Unit Testing   

    - Each app was tested using Django unit testing.
    - Tests were written to test the URLs, Models, Forms, and the Views.
    - To run the tests in the terminal you can type the following command
    -
        ```
            python3 manage.py test
        ```
    - To show how much of the app has been covered by the testing I used coverage.
    - Coverage generates a report to show how much of the code has been tested and how much is yet to be tested.
    - You can then run coverage HTML to show the report on the screen.
    - To open the report you can run 
        - ```
            python3 -m http.server
          ```

    - I've included the reports for each app below.

        - 
            <div align="center"><img src="readme-images/testing/coverage-1.png" alt="image of the homepage hero section"  height="500px" width="400px"/></div>
            <div align="center"><img src="readme-images/testing/coverage-2.png" alt="image of the homepage hero section"  height="400px" width="400px"/></div>
            <div align="center"><img src="readme-images/testing/coverage-3.png" alt="image of the homepage hero section"  height="400px" width="400px"/></div>


## Test and Bugs During Development

- #### Posting Data in the Cart App.
    - During Development I had an issue sending the post data while using stripe as I had decided to use vanilla javascript instead of jQuery.
    - When I was sending the data the CSRF token wasn't working.
    - I researched the issue and on stack overflow found the following solution which fixed the issue by placing 
    - By using the Headers key with X-CSRFTToken 
    -
        ``` javascript
            fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken
                },
        ```

- #### Moving Fetch function into its own file.
    - I had an issue when I moved my javascript into its own file when it was using the fetch function with the csrfToken.
    - I then found that declaring the csrfToken variable in a script tag on the HTML page before importing the javascript file fixed the issue
    - 
        ``` html
            <script>
                let csrfToken = "{{ csrf_token }}";
            </script>
            <script src="{% static 'cart/js/cart.js' %}"></script>
        ```


- #### Post Data in the Strip js
    - During developing the javascript for skype I had an issue with posting the data.
    - When I declared my data into a dictionary and tried to post it, it would work properly.
    - Through researching the issue I found that using the FormData constructor fixed the issue.
    - Once this was done the code then sent the data to the cache_checkout_data view.
    - 
        ``` javascript
                let csrfToken = document.querySelector('[name="csrfmiddlewaretoken"]').value
                let postData = new FormData()
                postData.set("csrfmiddlewaretoken", csrfToken)
                postData.set("client_secret", clientSecret)
                postData.set("save_info", saveInfo)
                let url = "/checkout/cache_checkout_data/";
            // stack overflow  code to help with the fetch and CSRF tokens
                fetch(url, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": csrfToken,
                    },
                    body: postData
                }).then(() => {
                    // rest of code 
        ```
    
- #### Blue background in forms on google chrome.
    - When I was testing my forms I noticed on google chrome they had a blue background colour that didn't sit well with the website design.
    - To fix this issue I researched and found it was styling that google chrome was applying to the forms.
    - I found code on StackOverflow to fix this.
    - By placing the following into my base CSS.
    - 
        ``` css
            /* code from stack overflow to stop my inputs 
            turning a light blue when filled in */
            input:-webkit-autofill,
            input:-webkit-autofill:hover,
            input:-webkit-autofill:focus textarea:-webkit-autofill,
            textarea:-webkit-autofill:hover textarea:-webkit-autofill:focus,
            select:-webkit-autofill,
            select:-webkit-autofill:hover,
            select:-webkit-autofill:focus {
                -webkit-box-shadow: 0 0 0px 1000px #EDEDE9 inset !important;
                box-shadow: 0 0 0px 1000px #EDEDE9 inset !important;
            }
                input:-webkit-autofill {
                    -webkit-text-fill-color: #153243 !important;
                }
        ```

- #### Error With Decimal Fields.
    - During the Development I noticed an issue with some of my items during the checkout.
    - I researched the issue and then figured out I had set my decimal fields too low in the models and as It was a furniture store and prices were higher they were causing an error.
    - I used the following page from stack overflow to fix this issue.
        - [Django Error class decimal](https://stackoverflow.com/questions/56458774/django-error-class-decimal-invalidoperation)


## Defensive Programming and Security

- Security
    - Environmental variables
        - For security reasons I have followed standard practices and used os to declare the environmental variables for any sensitive information.
        - For Development, these variables are declared in the settings section of gitpod.
        - In doing this it means that sensitive information such as passwords and secret keys aren't put in a public place.
        - To deploy on Heroku these environmental variables are also placed into the settings, config variables section.

    - Users passwords.
        - I have used Django all auth to handle the user's login and signup.
        - This stores the users pass as a hashed key for security.
        - It also makes the users confirm their emails as an extra security step.
    
    - ### Defensive Programming.
        
        - I have used code in my project to make sure actions cannot occur by placing URLs into the browser. 

        - If for instance the user types in the URL to delete a post the application has been programmed to redirect the user elsewhere and show an error message. 

        - I have tested this by typing the URLs into the browser it has worked as expected

        - I have also placed a confirmation modal to check if a user is sure they want to delete anything on the site such as, deleting the entire wishlist, or deleting a stock item for the superusers.
        
        - This will minimize the user deleting things by mistake.

## Manual Testing

## Validators

## Responsiveness and Browsers

## Accessibility

## Known Bugs