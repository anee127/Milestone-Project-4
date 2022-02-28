![Vanilla and Musk](readme-files/images/vanilla-musk.jpg)

**The live website can be found at:** [https://anee127-vanilla-musk.herokuapp.com/]

## Table of Contents
* [Project Overview](#project-overview)
* [User Experience (UX) ](#user-experience)
  * [The Strategy Plane](#the-strategy-plane)
    * [User Stories](#user-stories) 
  * [The Scope Plane](#the-scope-plane)
  * [The Structure Plane](#the-structure-plane)
  * [The Skeleton Plane](#the-skeleton-plane)
    + [Wireframes](#wireframes)
    + [Database Design](#database-design)
    + [Security](#security)
  * [The Surface Plane](#the-surface-plane)
* [Features](#features)
   + [Existing Features](#existing-features)
   + [Future Features](#future-features)
* [Technologies](#technologies)
   + [Languages](#languages)
   + [Database](#database)
   + [Libraries and Framework](#libraries-and-framework)
* [Testing](#testing)
* [Deployment](#deployment)
    + [AWS S3](#aws-s3)
    + [Deploy To Heroku](#deploy-to-heroku)
    + [Deploy to GitHub](#ldeploy-to-github)
* [Credits](#credits)
* [Acknowledgements](#acknowledgements)

****

## Project Overview

This is the 4th Milestone project taken as part of Code Institute Diploma Curriculum. Vanilla & Musk is a website that allows users to book candle making workshops and purchase handmade candle products. The project implements Stripe for payments and checkout of the products. Most of the admin work is carried out throughout the Django admin site but simple CRUD tasks can also be carried out by the site owner. 
 
## User Experience

### Strategy Plane
Vanilla and Musk is an e-commerce webs-shop that provides bookings to candle making workshops and sells handmade candles, located in East London. Customers can purchase products or book workshops which will be delivered to them by post.
**User stories **
As the site user I want to:
-	view a list of products
-	view individual product details 
-	view total purchase of items in my basket
-	view the order history after purchase
-	search for all products on the site
-	be able to sort products by name or price
-	be able to choose the quantity of a product to add to basket
-	adjust items in the basket before checkout
-	enter payment, billing and shipping information at checkout
-	trust that the payment is secure
-	view the order confirmation
-	register or login/out easily
-	be able to recover password if I forget
-	receive a verification email to confirm registration
-	edit details to my profile
As the site admin I want to:
-	provide a website with easy navigation and simple design.
-	Provide simple and straight forward information for users to purchase products.
-	Be able to add, edit and delete products directly from the webpage rather than through Django admin.
### Scope Plane
**Features**
-	Responsive design
-	Mobile and desktop compatibility
-	Navbar - nav menu with links to each page. 
-	Homepage gives relevant information about site upon being welcomed
-	Standard e-commerce function - can sort products by name or price.
-	Products can be added to basket from details page. 
-	Contact email and workshop location listed within footer, available on all pages.
### Structure Plane 
+ Upon arriving onto the homepage of the site, users are greeted with a hero image, text and button that links to workshops. Navigation, is at the top of all pages, contains the logo, linking to back to the homepage. There is also a menu bar that links to each section of the website. On smaller devices the links are in the hamburger menu. The contact, location and social information is within the footer element for users to access from every page. 
+ The Candles page allows users see all candle products for sale. The Candles are presented as cards with an image, name and price. Users can click on the image to open a page containing details about that product and add it to their basket. When the user adds to the basket, they will see a toast message at the top of the page informing them that they have successfully put the product into their basket along with the quantity they chose. 
+ The Workshops Page is similar to the Candles page. The description of the workshops is given including the date and time. The workshops can be paid for together with the other candle products if those are also added to the shopping basket. 
+ Through the basket page, users can see all the items that were added to their basket and when they change the quantity of it, it shows instantly. Once the user is ready for checkout, they will see a form which they have to fill for the checkout to be completed. Once completed, the order will be stored in Account > Order History and user can see it anytime.
+ After every user input, submission, registration, login, comment, reply they are notified by toast messages from the website that briefly describes the action taken so that user knows their action was properly submitted.
### Skeleton Plane 
#### Wireframes
The wireframes for the project can be found in the attached pdf file:
 [Wireframes link](readme-files/pdf/MS4-wireframes.pdf)
#### Database Design
-	As Django works with SQL databases by default, I was using SQLite in development. Heroku, however, provides a PostgreSQL database for deployment. 
-	The User model utilized for this project is the standard one provided by  django.contrib.auth.models
-	An image of the database scheme is shown below:
[MS4-schema](readme-files/pdf/ms4-schema.pdf)

#### Security
-	Using config variables in heroku, all access keys are stored safely to prevent unwanted connections to the database, including secret keys.
-	Django allauth was used to set up user registration and built-in decorators allowed restricted access to certain features on the website that are not intended for regular users.
### The Surface Plane
#### Colour scheme
The website has a simple monotone colour scheme with the use of black and white as the base. A few pops of pale yellow to represent vanilla colours, and shades of grey was used to also tie in with the images. 
![colour palette](readme-files/images/colour-scheme-4.png)
#### Typography
The main font used throughout the website is 'Cabin' as it is a soft rounded font that is easy to read. The’ Vanilla’ part of the logo is italicised and yellow to stand out and contrast from the rest of the logo.
#### Images 
-	Hero image and candle images were free images taken from [Unsplash.com](https://unsplash.com/)
-	Workshop images were free images taken from [Pexels.com](https://pexels.com/)
##  Features
### Existing Features
Website features:
- **Navigation Bar**
The navigation bar is visible on all pages and on all sizes (on a smaller width, it toggles into "hamburger"). It contains the web-site logo and a set of links for each section and subsection of site. On mobile devices the logo will not be visible to allow space for other nav items.
- **Homepage**
The homepage is simply an image of a candle with a brief introduction to the site and a button to link to the workshops as that is the main purpose of the site. 
- **Footer Section**
The footer field contains three sections, the first section provides contact information the second section contains the location for the workshops and the final section gives users the option to stay up to date with the app via links to social media profiles.
- **Workshop Page**
Workshops are listed for users to choose from and find out more information by clicking on the images. They are navigated to the workshop details page where a picture relevant to the workshop, type of workshop, description, price and an ‘book now’ button if they would like to purchase a ticket.
- **Products** 
Standard e-commerce feed of products with the option to sort the candle products and filter them by name and price. The images links to a product page where the user can read more about it, including picture of the product, name, description, price and add to basket button if they would like to add product.
- **User account**
User and profile information is available to registered/logged in users with the purpose of tracking their order history and safely storing shipping details for a smooth checkout. 
- **Admin account**
Available users with admin rights with the purpose of having access to the orders, user profiles, as well as product and inventory. Majority of the information is stored in the Django admin site but the users can also do common tasks such as adding, editing and deleting products/workshops directly through the website.
- **Search functionality**
A Search box is part of the top navigation and is, therefore, accessible on all pages. On mobile and ipad the search bar is collapsed under the search symbol. It allows customers to enter keywords associated with the products/workshops they wish to purchase
- **Toast Messages**
Small snippets of messages divided into 4 main categories: toast_success, toast_info, toast_warning and toast_error.
They appear on every page whenever a certain action has been done by the user.
Their purpose is to give feedback on the action a user has just performed, such as logging in, logging out, adding a product to the basket, updating the basket, and finishing the checkout process, etc.
- **Django-allauth feature**
django-allauth is a Python package. As written in the django-allauth docs, it is an "integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication."
It provides a set of features such as signup, login, logout and password change
After signing up, a verification e-mail is sent to the registered e-mail to confirm it. Once confirmed, the user can log in with their credentials and access the profiles app.
The links to these features can be found in the navigation, under the My Account dropdown menu, as well as on the pages and throughout the web app.
- **Automatic e-mails**
An account is working for this project and used as a sender for all verification, reset and confirmation e-mails.
For example, users receive an order confirmation e-mail after a purchase, account verification e-mail after the registration, password reset e-mail after requesting a password reset, etc.

### Features Left to Implement
***Save for later**
-	A feature that allows authenticated users to save items for later.
-	Every product in the feed and on product pages would have a heart-shaped icon which would add the product on a list. The list could be accessed on one of the profiles pages, where users can remove the items from the list as well.
***Reviews**
-	Allowing registered users to write reviews or comments on their experience with the workshops/products, as well as rate the products.

## Technologies Used
### Languages
+ [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) for creating the webpages
+ [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) for designing and styling the web pages
+ [javascript](https://www.javascript.com/) for some website functions
+ [Python](https://www.python.org/) for the backend development
### Database
+ [SQLlite (in Development)](https://www.sqlite.org/index.html)
+ [Postgres (at deployment)](https://www.postgresql.org/)
### Libraries and Frameworks
+ [Font Awesome](https://fontawesome.com/) used for the all icons on the website
+ [Google Fonts](https://fonts.google.com/) used to give the website fonts that are easy to read
+ [jQuery](https://jquery.com) used to simplify DOM manipulation.
+ [Django](https://www.djangoproject.com/) used to create framework of code for website
+ [Bootstrap](https://getbootstrap.com/docs/3.4/css/) used for responsive design and general styling
+ [Stripe](https://stripe.com/en-dk) used to generate online payments
### Hosting
+ [GitHub](https://github.com/) used to store the application in public repositories
+ [GitPod](https://gitpod.io/workspaces/) used as the primary development platform
+ [Heroku](https://www.heroku.com/) used to host the website
+ [AWS](https://aws.amazon.com/?nc2=h_lg) cloud used to hold static and media files 

## Testing
Separate testing file found [here](TESTING.md)

## Deployment
### AWS S3
AWS is a cloud based storage service, used to store static files and images:

1.	After creating an AWS account (using the free version will be sufficient), access the AWS management console in your account.
2.	Find s3 by searching for this in services.
3.	Open s3 and create a new bucket.
4.	Enter a name for your bucket/select your closest region.
5.	Uncheck the block public access box, and create the bucket.
6.	Once created, click on the bucket and enter the following settings:
	-	Under Properties, turn on static website hosting
	- 	Under Permissions, paste in the CORS configuration:

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
    -	Go to the bucket policy tab and select, policy generator so we can create a security policy for this bucket.
    -	The policy type is going to be s3 bucket policy, allow all principals by using a star, and the action will be, get object
    -	Copy the ARN which stands for Amazon resource name from bucket policy tab and paste it into the ARN box here at the bottom, then click Add Statement, then click Generate Policy then copy this policy into the bucket policy editor.
    -	Before clicking Save, because we want to allow access to all resources in this bucket, add a slash star onto the end of the resource key
    -	Go to the access control list tab, and set the list objects permission for everyone under the Public Access section
7.	With our s3 bucket ready to go. Now we need to create a user to access it. do this through another service called ‘I am’ which stands for Identity and Access Management.
8.	Go back to the services menu and open ‘I am’
9.	Click groups then create a new group (keep clicking through to Create Group)
10.	Create the policy used to access our bucket by clicking policies and then create policy
11.	Go to the JSON tab and then select import managed policy, then search for s3 and then import the s3 full access policy
12.	Get the bucket ARN from the bucket policy page in s3, and paste that in the JSON section
13.	Now click review policy, give it a name and a description, and then click create policy
14.	Now attach the policy to the group we created, go to groups, click manage my group, click attach policy, search for the policy we just created and select it, and click attach policy

15.	Create a user to put in the group. On the user's page, I'll click add user, create a user, give them programmatic access, then select next
16.	Now add user to your group. Important: Now download the CSV file which will contain this users access key and secret access key which we'll use to authenticate them from our Django app (cannot access this again so do this now)
17.	To Connect Django to s3 bucket, Install 2 new packages:
    -	```pip3 install boto3```
    -	```pip3 install django-storages```
18.	Then freeze requirements:
    -	```pip3 freeze > requirements.txt```
19.	Add ‘storages’ to installed apps on settings.py
20.	To connect Django to s3 we need to add some settings in settings.py to tell it which bucket it should be communicating with:
21.	Go to Heroku and add our AWS keys to the config variables, as well as adding that key called USE_AWS which I'll set to true
22.	Also remove the disable collect static variable
23.	In our settings file, we need to tell django where our static files will be coming from in production.
24.	Create a file called custom storages
25.	Go to settings.py, tell it that for static file storage we want to use our storage class we just created, and that the location it should save static files is a folder called static. Do the same thing for media files by using the default file storage and media files location settings.
26.	Add/commit changes in github.

### Deploy To Heroku
#### Create application:
1. Navigate to Heroku.com and login.
2. Click on the new button.
3. Select create new app.
4. Enter the app name.
5. Select region
#### Set up connection to Github Repository:
1. Click the deploy tab and select GitHub - Connect to GitHub.
2. A prompt to find a GitHub repository to connect to will then be displayed.
3. Enter the repository name for the project and click search.
4. Once the repo has been found, click the connect button.
#### Add PostgreSQL Database:
1. Click the resources tab.
2. Under Add-ons search for Heroku Postgres and then click on it when it appears.
3. Select Plan name Hobby Dev - Free and then click Submit Order Form.
#### Set environment variables:
1. Click on the settings tab and then click reveal config vars.
2. Variables added: 
    * AWS_ACCESS_KEY_ID 
    * AWS_SECRET_ACCESS_KEY 
    * DATABASE_URL 
    * EMAIL_HOST_PASS 
    * EMAIL_HOST_USER
    * SECRET_KEY 
    * STRIPE_PRICE_ID 
    * STRIPE_PUBLIC_KEY 
    * STRIPE_SECRET_KEY 
    * STRIPE_WH_SECRET 
    * USE_AWS 
#### Enable automatic deployment:
1. Click the Deploy tab
1. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

### Deploy To GitHub
1. Navigate to the GitHub Repository.
2. Click the Code drop down menu.
3. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
4. Open your development editor of choice and open a terminal window in a directory of your choice.
5. Use the git clone command in terminal followed by the copied git URL.
6. A clone of the project will be created locally on your machine.
Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages: pip install -r requirements.txt

## Credits
### Tutorials
I used the Code Institute Boutique Ado Mini-Project by [Chris Zielinski](https://code-institute-room.slack.com/team/U9QSX6HCG) as the main basis of my own project.
### Slack Community
I was able to resolve many issues, in particular with deployment to Heroku and using AWS services, after searching on Slack in the Code Institute community. 	
### Images
-	Hero image and candle images were free images taken from [Unsplash.com](https://unsplash.com/)
-	Workshop images were free images taken from [Pexels.com](https://pexels.com/)
### Text 
-	Workshop descriptions were inspired by [Hand Made Workshops](https://handmadeworkshops.co.uk/).
-	The candle descriptions, mainly the candle scents were found through google searches. 
## Acknowledgement
- My Mentor for continuous help and support throughout the project.
- The [Code Institute](https://codeinstitute.net/) Slack Community.
- A friend who has given me continuous help and advice throughout the project.
