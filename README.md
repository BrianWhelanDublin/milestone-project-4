# Abode Furniture E-Commerce Store

## Milestone Project 4



## Live project



## Screenshots



## Table of Contents.

## User experience

### User Stories

- Customers
  - Website experience
    - As a customer, I would like to see what the website is selling.
    - As a customer, I would like to be able to navigate the website easily.
    - As a customer, I would like to see some information about the company.
    - As a customer, I would like to be able to contact the company.
  
  - Searching for items.
    - As a customer, I would like to see all the products the company sells.
    - As a customer, I would like to be able to search by category.
    - As a customer, I would like to be able to search through the items.
    - As a customer, I would like to sort the items by price.

  - Shopping.
    - As a customer, I would like to see the product price and description.
    - As a customer, I would like to be able to add products to my shopping cart.
    - As a customer, I would like to be notified when I complete interactions with the site.
    - As a customer, I would like to be able to edit my shopping cart.
    - As a customer, I would like to be able to checkout easily.
    - As a customer, I would like to receive confirmation of my order.

  - Account.
    - As a customer, I would like to save my details to an account.
    - As a customer, I would like to see my previous order details.
    - As a customer, I would like leave a review of the company.

- Website owner.
  - As the business owner, I would like to be able to edit and add products easily.
  - As the business owner, I would like to be able to delete products.
  - As the business owner, I would like to have access to an admin section. 
  - As the business owner, I would like my customers to be able to shop on the site easily.


### WireFrames

- I've created WireFrames using Balsamiq and have included the links to access them in pdf form.

  - Phone
    - [Wireframes for phones.](readme-images/wireframes/milestone4-mobile-wireframes.pdf)
  - Tablet
    - [Wireframes for tablets.](readme-images/wireframes/milestone4-tablet-wireframes.pdf)
  - Desktop
    - [Wireframes for desktops.](readme-images/wireframes/milestone4-desktop-wireframes.pdf)


### Deployment.

#### Github, Gitpod, Git, Heroku, and Amazon AWS.

- #### Project setup.
  - The project was set up on github using the Code Institue Gitpod Template.
  - I located the template on the Code Institute github page and clicked the use template button.
  - I then named my repository and created it.
  - Once the repository was created I was able to open it with gitpod.
  - I coulfd then use the terminal to create files and folders and start coding the project.
  - Throughout the project I used git to add my changes to version control in github.
  - To commit I added the file to the staging area with the 
    ```
        git add <filename>
    ```
    ```
        git commit -m "<commit message>"
    ```
    ```
        git push
    ```
 
 ### Deployment to Heroku

  Once the app was ready I deployed to heroku by following these steps.

- Create an app on the Heroku website.
    - Firstly I clicked on the new button.
    - Then I clicked on the create new app.
    - I then gave muy app a name and chosse my current region.
    - I then selected create app.

- Set up Postgres Database
  - Heroku
    - In the app resources section i searched for Postgres
    - I then chose add to project chossing the free plan.
    - To use postgress we need two install 2 dependencies.
        - dj_database_url
        - psycopg2

  - In Project.
    - I first installed the two packages needed 

    - 
        ``` 
            pip3 install dj_database_url
        ```
    -
        ```
            pip3 install psycopg2_binary
        ```

    - I then made sure to add then to the requirements.txt file
    -
        ```
        pip3 freeze > requirements.txt
        ```
    - Then in settings.py I imported dj_database_url
    - 
        ``` python
        import dj_database_url
        ```
    - I then commented out the current database settings.
    - I then replaced it with the settings for the Postgres database.
    -
    ``` python
        DATABASES = {
            'default': dj_database_url.parse('DATABASE_URL')
        }
    ```
    - Get your database url from your app convig settings. (I haven't shown it above as its and eviornmental variable and shouldn't be shown in version control)

    - Once this is set up we need to migrate our models to the new database.
    - 
    ``` 
        python3 manage.py migrate
    ```

    - I then used the fixtures I had create earlier to add the stock into the new database. 
    - ```
        python3 manage.py loaddata categories
        python3 manage.py loaddata stock
    ```
    - Once this was done I then created a superuser.
    -```
        python3 manage.py createsuperuser
    ```


    