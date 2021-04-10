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

### Database models and schema

- #### Models
- Users
  - User
    - From Django Allauth containing the username, email, and password.
  - Userprofile
    - Model containing the user's details for future orders.
  - Wishlist
    - Contains a list of items that the user has liked.

- Stock 
  - Items
    - Contains the stock information for each stock item.
  - Categories
    - The categoriesfor the stock items.

- Customer details.
  - Newsletter Subscribers
    - Contains the email of users who have signed up for the newsletter.
  - Messages.
    - Contains the details of the messages from the contact form.

- Shop
  - Order
    - Contains details of the customer's orders, their details, and the items they've ordered.
  - Orderline item
    - Items for the customer order the quantity and total.

- Blog
  - Post
    - Contains the blog post and details of its author and title.
  - Comments
    - Contains the comments for each post.


- Database Diagram

  - The database diagram shows a list of items in each object and relationships between each object.

    <div align="center"><img src="readme-images/page_images/database-diagram.png" alt="image of the database diagram"></div>

### Design

- #### Colour scheme

  - My Colour scheme was inspired by my main hero image matching the navy background within the image to be used for the navigation and text colour.
  - I then pick two complimentary grey colours for the main background throughout the site, alternating between them in places to clearly define sections.
  - Throughout the site I used different opacities of these colours to create a softer pallet.

    - <p align="center"><img src="readme-images/design/colors.png" alt="Image of colour scheme" height="200px" width="350px"/></p>

- #### Typography

  - I've chosen the Roboto font from google fonts for my site.
  - I've used the one font throughout the website to keep the design consistent.
  - I then used different font weights to add more emphasis to some text, such as headings. 
    - <p align="center"><img src="readme-images/design/fonts.png" alt="Image of google font" height="200px" width="300px"/></p>

- #### Images 

  - Images are a key part of this site. 
  - All the images I have used were obtained from Unsplash.
  - I've used two main hero images on the landing page to give the site a dramatic appearance upon opening.
  - I then found images of furniture items and lighting items which I used to create my stock items for the e-commerce part of the site.

- Icons 
  - I've used icons in this project for the navigation on mobile sites and the social media links in the footer.
  - All icons have been optained from Line Awsome.



## Technologies used.

- The application was built on the Django full stack framework.
- For each section of the site a Django app was created.
- Each app then has a views.py, urls.py file to create the pages it needs.
- Then to create the database models a models.py file is used.
- If there are any forms needed they are then created in the forms.py file.
- Stripe has been used for the payment function of the e-commerce shop.
- Heroku was used to deploy the application.
- Amazon AWS was used to store. the static files and the image files.

### Languages Used.

- [HTML5](https://en.wikipedia.org/wiki/HTML5)

  - HTML5 was used to create the content and base of each page.

- [CSS3](https://en.wikipedia.org/wiki/CSS)

  - CSS3 was used to then style the page and make it responsive through media queries, and interactive through using CSS transitions.

- [javaScript](https://en.wikipedia.org/wiki/JavaScript)
  - javaScript was used throughout the website to make the site interactive.

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
  - Python was used to build the backend functionality of the web app.

### Django, and Django extensions used

- [Django](https://www.djangoproject.com/)
  - Django was used to create the project.

- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
  - Django allauth was used to create the user sign-in function for the site.

- [Django Allauth Social Login](https://django-allauth.readthedocs.io/en/latest/providers.html/)
  - Django allauth Social login function was used to allow the user to sign up, or login with Facebook.

- [Django Countries](https://pypi.org/project/django-countries/)
  - Django Countries was used for the countries select field in the order form.

- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  - Django Crispy Forms were used to utilise the bootstrap form classes.

- [Django Coverage](https://pypi.org/project/django-coverage/)

  - Django Coverage was used when testing to form a testing report.


### Frameworks Libraries and Programs.

- [Stripe](https://stripe.com/ie)

  - CStripe has been used for the payment section of the site.

- [Heroku](https://signup.heroku.com/)

  - Heroku was used to deploy the wesite.

- [Amazon AWS](https://aws.amazon.com/)

  - Amazon AWS was used to store the static files and the images for the site.

- [Facebook](https://developers.facebook.com/)

  - Facebook ws used for allauth social sign-up and login.


- [Gunicorn](https://gunicorn.org/)

  - Gunicorn was used for deploying the project to heroku.

- [Google Fonts](https://fonts.google.com/)

  - I imported the Mulish font from google fonts and used it consistently across the site.

- [Line awesome](https://icons8.com/line-awesome)

  - I used different icons from Line awesome for icons in the application.

- [Bootstrap 5](https://getbootstrap.com/)

  - Bootstrap 5 was used for its grid system and it's form inputs and it's helper classes.

- [Quick Database Diagrams](https://www.quickdatabasediagrams.com/)

  - I used quick database diagrams to make a digram of my database schema.

- [Git](https://git-scm.com/)

  - Git was used as a version control in the terminal.

- [Github](https://github.com/)

  - Github was used to create and store the project repository.

- [Gitpod](https://gitpod.io/)

  - Gitpod was used to create my files and code the project.

- [Balsamiq](https://balsamiq.com/)

  - Balsamiq was used to create Wireframes for the project during the initial planning stage.

- [Am I responsive](http://ami.responsivedesign.is/)

  - Am I responsive was used to taking screenshots of the page at different screen sizes.

- [Markdown toc](http://ecotrust-canada.github.io/markdown-toc/)

  - Markdown toc was used to create my table of contents.


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

#### Setting up locally

  - To set the project up locally you can follow these steps.
    
    - Download a copy of the repository from Github using the Download Zip option in the code dropdown.

      - <p align="center"><img src="readme-images/deployment/download-zip.png" alt="Image of colour scheme" height="200px" width="350px"/></p>
    
    - Then extract the zip file to your repository.

    - Alternatively, you can clone it into your repository using the following command.

      - ```
            git clone https://github.com/BrianWhelanDublin/milestone-project-4.git
        ```
    
    - Once you have created the repository you can now download the requirements by running the following command.

      - 
      ```
            pip3 install -r requirements.txt
      ```
    
    - You must then set up the following environment variables to use the full functionality of the site.

      - DANGO_SECRET_KEY = your secret key.
      - STRIPE_PUBLIC_KEY = your stripe public key.
      - STRIPE_SECRET_KEY = your stripe secret key.
      - STRIPE_WEBHOOK_SECRET = your stripe webhook secret.
      - IN_DEVELOPMENT = True

      - Your stripe variables can be found on your stripe dashboard.
      - You can generate a Django secret key here. [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)
    
    - You will then need to migrate the database models to set up your database.
    - 
      - Check first
        ```
            python3 manage.py makemigrations --dry-run
        ```
       -  Then make migrations.
            ```
                python3 manage.py makemigrations
            ```
       - Check the migration plan
            ```
                python3 manage.py migrate --plan
            ```
       - Then finally migrate
            ```
                python3 manage.py migrate
            ```

     - Then create your superuser to access the admin section.
      -
        ```
            python3 manage.py createsuperuser
        ```

        - Following the prompts.

    - Once these steps have been followed you can then run the project by using the following command.

        - 
            ```
                python3 manage.py runserver
            ```

## Credits.

### Code.

- #### Kevin Powell Youtube video.
  - This youtube walkthrough help me to design and animate my navigation menu. I've adapted the code to suit my site.
  - [Fade + slide in nav list items one at a time](https://www.youtube.com/watch?v=xkKjrH3pRfg&list=WL&index=3&t=1028s)

- #### Stack Overflow 

  - [Sending POST data with fetch](https://stackoverflow.com/questions/6396101/pure-javascript-send-post-data-without-a-form)
  - I used code from the above StackOverflow article to help with sending post data using fetch in javascript.

  - [Django CSRF](https://stackoverflow.com/questions/43606056/proper-django-csrf-validation-using-fetch-post-request)
    - I used code from this stack overflow article to help with the Django CSRF validation when using fetch and post. 

 - [Removing Blue Background in forms](https://stackoverflow.com/questions/55131944/how-to-remove-blue-background-on-chrome-autocomplete)
   - I used code from the above article to remove the light blue background that chrome was putting on my forms. 

 - [Error with the decimal fields](https://stackoverflow.com/questions/56458774/django-error-class-decimal-invalidoperation)
   - I used code from the above article to help with a bug during development with my decimal fields.

 - [Messages extra tags](https://stackoverflow.com/questions/15017706/how-to-display-multiple-django-messages-in-one-page)

 - [Test image input in Django forms](https://gist.github.com/drillbits/5432699)
   - I used this code to help with my Django testing of the forms image input.

- [Django allauth Facebook](https://dev.to/gajesh/the-complete-django-allauth-guide-la3)
  - I used this article to help set up the allauth Facebook signup.
  

### Content

- All Text for the website was written by myself.

### Media

- [Unsplash](https://unsplash.com/)
  - All images for the website were obtained from Unsplash.

### Acknowledgements

- Code Institute for getting me to this point

- My Mentor Spencer for his help with this project.