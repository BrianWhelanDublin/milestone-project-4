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
 - The project was set up on GitHub using the Code Institue Gitpod Template.
  - I located the template on the Code Institute GitHub page and clicked the use template button.
  - I then named my repository and created it.
  - Once the repository was created I was able to open it with Gitpod.
  - I could then use the terminal to create files and folders and start coding the project.
  - Throughout the project, I used git to add my changes to version control in GitHub.
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

  Once the app was ready I deployed it to Heroku by following these steps.

- Create an app on the Heroku website.
    - Firstly I clicked on the new button.
    - Then I clicked on the create a new app.
    - I then gave muy app a name and chose my current region.
    - I then selected create app.

- Set up Postgres Database
  - Heroku
    - In the app resources section I searched for Postgres
    - I then chose to add to the project and, choosing the free plan.
    - To use Postgres we need to install 2 dependencies.
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

    - I then made sure to add them to the requirements.txt file
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
    - Get your database URL from your app config settings. (I haven't shown it above as its and environmental variable and shouldn't be shown in version control)

    - Once this is set up we need to migrate our models to the new database.
    - 
        ``` 
            python3 manage.py migrate
        ```

    - I then used the fixtures I had to create earlier to add the stock into the new database. 
    - 
        ```
            python3 manage.py loaddata categories
            python3 manage.py loaddata stock
        ```

    - Once this was done I then created a superuser.
    - 
        ```
            python3 manage.py createsuperuser
        ```
    
    - I then committed my changes making sure to remove my database URL beforehand so it isn't saved in version control.

    - I then created an if-else statement in the settings.py to use Postgres if the DATABASE_URL variable is available and if not use the default database

    - 
        ``` python
            if "DATABASE_URL" in os.environ:
                DATABASES = {
                    "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
                }
            else:
                DATABASES = {
                    'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': BASE_DIR / 'db.sqlite3',
                    }
                }
        ```
    
    -The Postgres database is now ready for use.

- Gunicorn
    - For our app to work we need to install Greenunicorn.
    - To install 
    - 
        ```
        pip3 install Gunicorn
        ```
    - We then need to create a Procfile to let Heroku know how to run the app.
    -
        ``` 
            touch Procfile
        ```
    - Then in our Procfile place the following code.
    -
        ```
            web: gunicorn <app name>.wsgi:application
        ```
  -Heroku in the command line.
    - I then logged into Heroku using the terminal.
    -
        ```
            heroku login -i
        ```
    - Then I temporarily disabled the static files until they have been set up on Amazon Aws.
    -
        ```
            heroku config:set DISABLE_COLLECTSTATIC=1 --app <app name>
        ```
        - Use the --app command if you have more than one Heroku app.
    - Then in settings I added Heroku into allowed hosts, and localhost so my project can still be run locally.
    -
        ``` python
            ALLOWED_HOSTS = ["<heroku app name>.herokuapp.com", "localhost"]
        ```
    - My changes were then committed to Github.
    - Then I set up pushing to Heroku
    -
        ```
            heroku git:remote -a <heroku app name>
        ```
    - Then we push the project to Heroku
    -
        ```
            git push heroku master
        ```
    
    - Heroku will now build your app.
  
  -Heroku Website
    - I then connected my app to GitHub by opening the Deploy section.
    - I then searched for my repository.
    - Once found I connected and then enabled Automatic Deploys
    - This now means that any changes pushed to GitHub will be automatically pushed to Heroku as well.


    