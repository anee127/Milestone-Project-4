![homepage](readme/images/hero-image.png)

The live website can be found [here]

## Table of Contents
* [Project Summary](#project-summary)
* [User Experience Design (UX)](#user-experience-design)
  * [The Strategy Plane](#the-strategy-plane)
    * [User Stories](#user-stories) 
  * [The Scope Plane](#the-scope-plane)
  * [The Structure Plane](#the-structure-plane)
  * [The Skeleton Plane](#the-skeleton-plane)
    * [Wireframes](#wireframes)
    * [Database Design](#database-design)
    * [Security](#security)
  * [The Surface Plane](#the-surface-plane)
* [Features](#features)
   * [Existing Features](#existing-features)
   * [Future Features](#future-features)
* [Technologies](#technologies)
* [Testing](#testing)
* [Deployment](#deployment)
    * [AWS S3](#aws-s3)
    * [Heroku Deployment](#heroku)
    * [Local Deployment](#local-deployment)
* [Credits](#credits)

****

## Project Overview

This is the 4th Milestone project taken as part of Code Institute Diploma Curriculum. Vanilla & Musk allows users to book candle making workshops and purchase handmade candle products from one site. The project implements Stripe for payments and checkout of workshops or products. Most of the admin work is carried out throughout the Django admin site. 
 
## User Experience

### Strategy Plane
Vanilla and Musk is a candle making workshop site that also sells handmade candles, located in East London. Customers can purchase items or book workshops as well as review products and workshops, available to registered users.
**User stories **
Viewing navigations
Shopper – view list of products, view indiv product details, find special offers, view total of purchase in basket.
Register user account
Site user – register easy, login/out, recover password when forget, receive email confirm after register, personalised user profile.
Sorting searching
Shopper- sort list of available products/ category/multiple categories at same time, search by name/description, see search and number of results.
Purchase/checkout
Shopper – select size/quantity of product, view items in bag, adjust items in bag, enter payment info, secure payment, view order confirm, get email receipt. 
Admin 
Store owner – add product, edit update a product, delete product.

### Scope Plane
features 
-	Responsive design
-	Mobile and desktop compatibility
-	navbar with nav menu with links to each page. 
-	Homepage gives relevant information about site upon being welcomed
-	Standard e-commerce function, can sort products/workshops.
-	Products can be added to basket from product/worshop info page. 
-	Contact information provided on homepage for enquiries.
-	Customers can rate products/workshops
### Structure Plane 
Upon arriving onto the homepage of the site, users are greeted with a hero image, text and button that links to workshops. The next section down, users can link to the product page, with a small caption. Navigation, is at the top of all pages, contains the logo, linking to back to the homepage. On smaller devices there is a link in the hamburger menu. There is also a menu bar that links to each section of the website. The contact information is within the footer element for users to access from every page. 
The Products page allows users see all products for sale. Products are presented as cards with an image, name, price and rating. Users can click on the image to open a page containing details about that product and add it to their basket. When the user adds to the basket, they will see a message at the top of the page informing them that they have successfully put the product into their card along with the quantity they chose. 
The Workshops Page is similar to the Products page. The description of the workshops is given including the date, time and location. The workshops can be booked paid for together with the other candle products if those are also added to the shopping basket. 
Through the basket page, users can see all the items that were added to their basket and when they change the quantity of it, it shows instantly. Once the user is ready for checkout, they will see a form which they have to fill for the checkout to be completed. Once completed, the order will be stored in Account > Order History and user can see it anytime.
After every user input, submission, registration, login, comment, reply they are notified by a message from the website that briefly describes the action taken so that user knows their action was properly submitted.
### Skeleton Plane 
The wireframes for the project can be found in the attached pdf file ….
### Database Architecture
As Django works with SQL databases by default, I was using SQLite in development. Heroku, however, provides a PostgreSQL database for deployment. 
The User model utilized for this project is the standard one provided by  django.contrib.auth.models
Using config variables in Heroku, all SECRET access keys are stored safely to prevent unwanted connections to the database.
Django allauth was used to set up user registration and built in decorators allowed restricted access to certain features on the website that are not intended for regular users.
### surface Plane
#### Colour scheme
The website has a simple monotone colour scheme with the use of black and white as the base. A few pops of pale yellow to represent vanilla colours and pale pink to represent musk colours, and shades of grey was used to also tie in with the images. 
Typography
The main font used throughout the website is '' as it is a soft rounded font that is easy to read. The logo is ‘’ to look bold and stand out. 
Images 
-	Hero image and candle images were free images taken from unsplash.com
-	Workshop images were free images taken from pexels.com
##  Features
### Existing Features
Website features:
**Navigation bar**
Navigation bar is visible on all pages and on all sizes (on a smaller width, it toggles into "hamburger"). It contains web-site logo and a set of links for each section and subsection of site.
**Footer section**
Footer section contains three sections, the first section links to different sections of web-site, the section contains the stores location and the final section gives users the option to stay up to date with the app via links to social media profiles.
**workshop**
Standard e-commerce feed of products with the option to sort products and filter them by category name and price. Every product can be added to the cart immediately and links to a product page where the user can read more about it, including picture of product, name, description, price and an add button if they would like to add product.
**Products** 
Standard e-commerce feed of products with the option to sort products and filter them by category name and price. Every product can be added to the cart immediately and links to a product page where the user can read more about it, including picture of product, name, description, price and an add button if they would like to add product.
**User account**
Available to registered/logged in users with the purpose of tracking their order history and safely storing shipping details for a smooth checkout.
**Admin account**
Available users with admin rights with the purpose of having access to the orders, user profiles, as well as product and blog inventory. Majority of the information is stored in the Django admin site but the users can also do common tasks such as adding, editing and deleting products or blog posts through the site.
####Search functionality
A Search box is part of the top navigation and is, therefore, accessible on all pages.
On mobile and ipad the search bar is collapsed under the search symbol.
It allows customers to enter keywords associated with the products they wish to purchase.
The search results are displayed as a feed of products by using the page templates prepared for the products 
###Django app. 
####toasts
Small snippets of messages divided into 4 main categories: toast_success, toast_info, toast_warning and toast_error.
They appear on every page whenever a certain action has been done by the user.
Their purpose is to give feedback on the action a user has just performed, such as logging in, logging out, adding a product to the cart, updating the cart, editing a blog post, finishing the checkout process, etc.
####Django-allauth feature
django-allauth is a Python package. As written in the django-allauth docs, it is an "integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication."
It provides a set of features such as signup, login, logout and password change
After signing up, a verification e-mail is sent to the registered e-mail to confirm it. Once confirmed, the user can log in with their credentials and access the profiles app.
The links to these features can be found in the navigation, under the My Account dropdown menu, as well as on the pages and throughout the web app.
####Automatic e-mails
An account is working for this project and used as a sender for all verification, reset and confirmation e-mails.
For example, users receive an order confirmation e-mail after a purchase, account verification e-mail after the registration, password reset e-mail after requesting a password reset, etc.
####Home app
home Django app mainly serving as an introduction to the company and the marketplace.
Another feature on the home page is the new arrivals section, this section contains 3 pictures of the newest products that are clickable links to the full details of the products.
####Products app
products Django app is where all the logic and templates connected to the product feed and individual products are.
It can be divided into three main sections: shop, product pages and admin product management activities.
Shop is the main feed of products and this is where the majority of shopping journeys are expected to start. The shopping experience is enhanced by having a dropdown for sorting products (A-Z, Z-A, price low-high, price high-low),
By clicking on a product, user can see the full product info including pictures of product, name, description, price and an add button if they would like to add product.
Admin product management activities include adding, editing and deleting products. Users with admin rights can do that directly in the UI through forms.
####Bag app
bag Django app is a standard e-commerce functionality which aids the checkout process.
A cart is always present in the top right corner of the web app. The bag adds a number symbol beside the cart letting the user know how many items they currently have in their bag.
Users can edit quantity of items or remove them from cart and see price total amount. In order to proceed with checkout, user will be required to register on the site. When user decides to finish shopping, they will need to input their information and credit card details so that purchase can be completed.
If users try to access their empty carts, there will be a message displayed that nothing has been added yet and encourage them to go to the shop.
####Checkout app
checkout Django app is another standard e-commerce functionality which enables users to buy the products online from the shop.
In order to check out, the user is presented with a form asking for the shipping and payment details and with the overview of the order.
Users can easily go back to the cart and adjust it by clicking on the cart in the top right corner or breadcrumbs in the top left corner.
A webhook is implemented to the checkout so that the order is successfully processed in case the checkout process gets interrupted. Some reasons might be closing the browser too soon or losing internet connection.
"payments" are handled through stripe. A test purchase can be made with the following details:
credit card: 4242 4242 4242 4242
expiration date: 04 / 24
CVC: 424
ZIP: 42424
After the payment has been processed, the user is presented with the order summary on the order confirmation page.
logged in buyers can also see their order history on the profiles pages.
####Profiles app
profiles Django app is available to registered, authenticated users.
It offers 2 features: order history and saving shipping information.
Order history displays all previous orders per user account.
Saving shipping information is done through a form which can be edited anytime. This information is what populates the checkout form for the next orders and where shipping information saved during the checkout process is stored.
### Features Left to Implement
####Save for later
-	A feature that allows authenticated users to save items for later.
-	Every product in the feed and on product pages would have a heart-shaped icon which would add the product on a list. The list could be accessed on one of the profiles pages, where users can remove the items from the list as well.
#### Reviews
-	Allowing registered users to write reviews or comments on their experience with the workshops/products.

## Technologies Used

HTML - used to create the site structure.
CSS - used to create the styling throughout the site.
JavaScript - this was used for the addition/deletion of ingredients and methods buttons
jQuery - this was used to activate the Materialize functionality.
Python - used to write the logic that operates the site.
Django - web framework used to allow a modular site to be created.
Font-Awesome - icons were taken from this site for the forms, header, footer and social buttons.
Google fonts - as previously stated, the fonts used were taken from here.
Heroku - used for hosting website.
Bootstrap - used for responsive grid framework, navigation and buttons.
Stripe - ecommerce payment system.
### Languages
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) for creating the webpages
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) for designing and styling the web pages
- [javascript](https://www.javascript.com/)
- [Python](https://www.python.org/) for the backend development
### Database
- [SQLlite (in Development)](https://www.sqlite.org/index.html) and [Postgres (at deployment)](https://www.postgresql.org/) Although SQLite has been used as the backend database during development, the 
### Libraries and Frameworks
- [Font Awesome](https://fontawesome.com/) - have been used for the button icons that are used in the website
- [Google Fonts](https://fonts.google.com/) have been used to give the website a uniform look with the help of fonts provided by google
- [jQuery](https://jquery.com) - have been used to simplify DOM manipulation.
- [Django](https://www.djangoproject.com/) - web framework for creating modular websites
- [Bootstrap](https://getbootstrap.com/docs/3.4/css/) - CSS used for responsive grid framework and general styling
- [Stripe](https://stripe.com/en-dk) - used for payment with credit card
### Hosting
- [GitHub](https://github.com/) have been used for storing the application in public repositories
- [GitPod](https://gitpod.io/workspaces/) have been used as the primary development platform
- [Heroku](https://www.heroku.com/) have been used to host the website
- [AWS](https://aws.amazon.com/?nc2=h_lg) for static and media files

## Testing
## Heroku Deployment 

#### Create application:

1. Navigate to Heroku.com and login.
2. Click on the new button.
3. Select create new app.
4. Enter the app name.
5. Select region.

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

## Local Deployment

1. Navigate to the GitHub Repository.
2. Click the Code drop down menu.
3. Either Download the ZIP file, unpackage locally and open with IDE (This route ends here) OR Copy Git URL from the HTTPS dialogue box.
4. Open your development editor of choice and open a terminal window in a directory of your choice.
5. Use the git clone command in terminal followed by the copied git URL.
6. A clone of the project will be created locally on your machine.

Once the project has been loaded into an IDE of choice, run the following command in the shell to install all the required packages: pip install -r requirements.txt

# Credits

## Content
