# Abode Furniture E-Commerce Store

## Milestone Project 4

  - This project aims to build a full-stack web application using Django full-stack web framework, HTML, Css3 and javascript.

  - I have built an e-commerce web application for a fictional furniture company.
  
  - My application features e-commerce functionality, payments using stripe, a blog section, user login using Facebook, a wishlist section for registered users, confirmation emails, CRUD functionality for admin to add blog posts and stock items, and an admin section, for the admin user to access database records.

  - For the assessor, I have included the admin login details in the comments section when submitting the project.

  - This website is for educational purposes and the stripe functionality is set up to accept the test card details please don't enter your personal card details. 
  
     - To use the stripe function use the following details.

        - card number : 4242 4242 4242 4242
        - Any date
        - Any CVV number.


## Live project


- [View the live project here.](https://abode-milestone-4.herokuapp.com/)

## Screenshots

  - ### Landing page Hero Section.

<div align="center"><img src="readme-images/page_images/homepage_hero.png" alt="image of the homepage hero section"></div>

  - ### Landing page Shop Our Collections.

<div align="center"><img src="readme-images/page_images/shop-collections.png" alt="image of the homepage shop by collection section"></div>

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
 
- #### Deployment to Heroku

  Once the app was ready I deployed it to Heroku by following these steps.

- **Create an app on the Heroku website.**
    - Firstly I clicked on the new button.
    - Then I clicked on the create a new app.
    - I then gave muy app a name and chose my current region.
    - I then selected create app.

- **Set up Postgres Database**
  - Heroku
    - In the app resources section I searched for Postgres
    - I then chose to add to the project and, choosing the free plan.
    - To use Postgres we need to install 2 dependencies.
        - dj_database_url
        - psycopg2

  - **In Project.**
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

  - **Gunicorn**
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

  - **Heroku in the command line.**
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

  - **Heroku Website**

    - I then connected my app to GitHub by opening the Deploy section.
    - I then searched for my repository.
    - Once found I connected and then enabled Automatic Deploys
    - This now means that any changes pushed to GitHub will be automatically pushed to Heroku as well.

- #### Amazon AWS

  - Amazon AWS was used to store both static files and media files.
  - Firstly I created an AWS account and worked through the sign-up process. Once my account was set up I was able to set my project up on AWS.

  - **Create a bucket.**

    - Create the bucket
        - First thing was to create a new bucket on the AWS S£ service.
        - From the main dashboard search for S£ and then click to get started.
        - Click on the Create bucket button.
        - Give the bucket a name and select your region.
        - Then uncheck the block public access and acknowledge that the bucket will now be public.
        - Then click create bucket.
    
    - Bucket settings.
        - Properties
            - Navigate to the bucket properties settings.
            - Turn on static website hosting.
            - In the index and error add index.html and error.html.
            - Click save.
        - Permissions
            - Click on the buckets Permissions tabs.
            - Firstly paste in the following cors config.
            - 
                ```
                [
                    {
                        "AllowedHeaders": [
                            "Authorization"
                        ],
                        "AllowedMethods": [
                            "GET"
                        ],
                        "AllowedOrigins": [
                            "*"
                        ],
                        "ExposeHeaders": []
                    }
                    ]
                ```
            - Then in the bucket policy tap, click on generate policy.
            - Policy
            - Select S3 bucket policy
            - Add * to the principal field to select all principals
            - Set the action to get object.
            - Paste in your ARN which is available on the previous page.
            - Click, add statement
            - Then click, generate policy.
            - Now copy and paste your new policy into the bucket policy.
            - Add /* onto the end of the resources key
            - Click save.
        - Access control list
        - In the access control list tab set the list objects permission to everyone.
    
   - **Create a User.**

     - To create a user for the bucket we need to use another Amazon service.
     - Back in the main dashboard search for IAM and select it.
     
     - Create a Group.
       - Firstly we need to create a group to put our user in.
       - Click create a new group and name it.
       - Click through to the end and save the group.
       - Create a policy.
         - In our group click, policy and then, create policy.
         - Select the JSON tab and then import managed policies.
         - Search S3 and select AmazonS3FullAccess and import.
         - In the resources section paste in our arn from before.
         - click through to review the policy.
         - Fill in name and description and then click generate policy.
       - Back in your group click permission and then attach the policy.
       - Find the policy you've just created and attach it.
    
     - Create the User.
       - Select Users from the sidebar and then click, add user.
       - Create a user name and select programmatic access then click next.
       - Then select your group to add your user to.
       - Click through to the end and then click create user.
       - ** Make sure to now download the CSV file as it contains the users keys needed to access from our app.**

  - **Connecting to Django**
    
    - Once our AWS has been set up we now need to connect it to Django.
    - Firstly two packages are needed.
      - boto 3
      - Django storages
    - Firstly install these packages.
    -
        ```
            pip3 install boto3
            pip3 install django-storages
        ```
    - Then add to our requirements.
    -
        ```
            pip3 freeze > requirements.txt
        ```
    - We then add storages into our installed apps in settings.py
    - We then add the following settings to our settings.py
    - We create an environmental variable to only run this code when on Heroku. "USE_AWS"
    -
        ``` python
            if "USE_AWS" in os.environ:

                # Bucket Config
                AWS_STORAGE_BUCKET_NAME = '<bucket name>'
                AWS_S3_REGION_NAME = '<your region>'
                AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
                AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
                AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

                # static and media file storage
                STATICFILES_STORAGE = 'custom_storages.StaticStorage'
                STATICFILES_LOCATION = 'static'
                DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
                MEDIAFILES_LOCATION = 'media'

                # Override static and media URLs in production
                STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
                MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
        ```
    - Then back in Heroku we click the settings and reveal config vars.
    - Then set up the environmental variables needed.
    - We then create a custom_storages.py to tell Django that in production we want to use s3 to store our static and media files.
    - We Firstly need to import S3Boto3Storage.
    - then we set up our new classes to tell Django where to store the files.
    -
        ``` python
            class StaticStorage(S3Boto3Storage):
                location = settings.STATICFILES_LOCATION


            class MediaStorage(S3Boto3Storage):
                location = settings.MEDIAFILES_LOCATION
        ```
    - Once all the settings are done we can now push to GitHub and Heroku.

  - **Add our media to AWS.**
  
    - The final step is to add our media to AWS.
    - In your bucket create a new folder called media.
    - Select upload and add your image files.
    - Then select to grant public access.
    - And then upload the files.
    