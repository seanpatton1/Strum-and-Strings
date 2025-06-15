# Strum & Strings

![Website responsive image](static/images/responsive_collage.png)

Welcome to Strum & Strings – Your Ultimate Guitar Destination

Strum & Strings is a full-stack Django-based e-commerce platform offering a seamless online shopping experience for guitar enthusiasts.  
Customers can browse a curated selection of premium guitars and accessories add them to their shopping basket, and complete secure purchases through Stripe integration.

With a responsive, intuitive, and mobile-first design, Strum & Strings ensures a smooth shopping journey across all devices.  
From browsing products to checkout, the site provides a clean, elegant interface that mirrors the passion of true guitar lovers.

Your perfect sound is just a few clicks away!

Visit the deployed website [here](https://strum-and-strings-e5017bc28566.herokuapp.com//)

## Table of Contents

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Project Goals](#project-goals)
    2. [Implementation](#implementation)
    3. [Color Scheme](#color-scheme)
    4. [Typography](#typography)
    5. [Database Model](#database-model)
    6. [Wireframes](#wireframes)
2. [Features](#features)
    1. [Home Page](#home-page)
    2. [About Us](#about-us)
    3. [Product Listings](#product-listings)
    4. [Product Details](#product-details)
    5. [Cart and Checkout](#cart-and-checkout)
    6. [Profile Management](#profile-management)
    7. [Newsletter Signup](#newsletter-signup)
    8. [Admin Panel](#admin-panel)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Finished Product](#finished-product)
6. [Deployment](#deployment)
7. [Marketing Strategies](#marketing-strategies)
8. [Credits](#credits)
9. [Acknowledgements](#acknowledgements)

# Business Model

## Business Overview

Strum & Strings is an e-commerce platform specializing in the sale of guitars and related accessories. The website caters to a diverse audience, including individual musicians, hobbyists, students, and educational institutions.

---

## Target Audience

- **Musicians**: Hobbyists, professionals, and performers seeking high-quality guitars and accessories.
- **Students**: Aspiring musicians and beginners in need of affordable starter kits or beginner-friendly bundles.
- **Educational Institutions**: Schools, colleges, and universities seeking bulk orders or specialized packages for music programs.

---

## Product Offering

- **Individual Products**:
  - Guitars: Acoustic, electric, bass, classical, and specialty guitars.
  - Accessories: Strings, picks, amplifiers, tuners, straps, cases, cleaning kits.

- **Bundles**:
  - Starter Kits: Beginner packages with a guitar, strap, tuner, and strings.
  - Advanced Kits: Professional bundles including a high-end guitar, amplifier, and accessories.
  - Institutional Packages: Customized bulk packages designed for educational institutions.

---

## Revenue Model

- **Product Sales**:
  - Competitive pricing on individual products and bundle deals.
- **Upselling and Cross-Selling**:
  - Complementary products suggested at checkout (e.g., picks, straps, tuners).
- **Institutional Discounts**:
  - Bulk pricing for schools and colleges.
- **Subscription Add-On (Future Expansion)**:
  - Optional premium subscription for tutorials, guitar maintenance guides, and exclusive previews.

---

## Unique Selling Points

- **Specialization**: Focus solely on guitars and accessories for expert curation.
- **Customization**: Tailored bundles for students and institutions.
- **Educational Focus**: Collaborations with schools to enhance music learning experiences.
- **Convenience**: A streamlined online shopping experience with intuitive navigation.

---

## Marketing Strategies

- **Digital Advertising**: Targeted ads on Facebook, Instagram, and Google.
- **Social Media Engagement**: Content creation (tips, tutorials, success stories) to build community.
- **Email Campaigns**: Regular newsletters with promotions and new product announcements.
- **Affiliate Partnerships**: Collaborations with music influencers, teachers, and institutions.

# User Experience (UX)

## Project Goals

- Create a clean and responsive online store focused on guitars and accessories.
- Allow users to browse, search, and filter products easily.
- Enable users to add products to a shopping cart, checkout securely, and track their orders.
- Provide an easy-to-use profile area for managing personal details and order history.
- Allow users to subscribe to a newsletter for product updates and promotions.
- Ensure the website is mobile-friendly and fast across all devices.
- Build trust with users through professional design, clear calls to action, and simple navigation.

---

## Implementation

- The website is built using Django, leveraging powerful models for products, orders, and user profiles.
- Bootstrap 5 is used to ensure responsive layouts across mobile, tablet, and desktop.
- Cloudinary is used for external image hosting to optimize media delivery.
- Stripe integration allows secure checkout with real payment gateway support.
- Django-Allauth is used for authentication, including secure signup and login functionality.
- Marketing features like a Mailchimp newsletter signup are integrated to engage users.

---

## Color Scheme

- The color scheme reflects an earthy and natural tone, matching the feel of traditional and modern guitars.
- Primary Color: Deep brown (#4B3621) — used for headers, navbar, and footer.
- Accent Color: Soft tan (#D4A373) — used for buttons and highlights.
- Background Color: Warm off-white (#FAF7F2) — for the main page background.
- Forms and modals are displayed with white backgrounds for contrast and accessibility.

---

## Typography

- Font Family: Open Sans and Arial (sans-serif fallback).
- Headings use bold Open Sans for clarity.
- Body text uses standard sans-serif for easy readability across devices.

---

## Database Models

The site uses PostgreSQL for the production database. Key Django models:

- **Product**: Name, brand, category, model, image, image URL (Cloudinary), description, price.
- **Category**: Guitar type categories (Acoustic, Electric, Bass, etc.).
- **Order**: Customer order with status tracking.
- **CartItem**: Temporary cart items tied to users.
- **UserProfile**: Extended user info (address, etc.).
- **NewsletterSignup**: Email subscription form tied to Mailchimp API.

---

## Wireframes

Wireframes were designed using Balsamiq to plan layouts for desktop and mobile views:

- **Home Page Wireframe**: Hero section with featured products.
- **Shop Page Wireframe**: Product listings with filters and search.
- **Product Detail Wireframe**: Image gallery and add-to-cart form.
- **Cart and Checkout Wireframes**: Clean step-by-step purchase flow.
- **Profile and Order History Wireframe**: User dashboard for order management.

---

### Wireframe Images

- **Home Page Wireframe**

  ![Home Page Wireframe](static/images/Landing-Page.png)

- **Shop Page Wireframe**

  ![Shop Page Wireframe](static/images/All-Products.png)

- **Categories Wireframe**

  ![Product Detail Wireframe](static/images/Categories.png)

- **Cart Page Wireframe**

  ![Cart Page Wireframe](static/images/cart.png)

- **Log-In Wireframe**

  ![Checkout Page Wireframe](static/images/login.png)

- **Signup Wireframe**

  ![Profile Wireframe](static/images/sign-up.png)

- **Profile Wireframe**

  ![Profile Wireframe](static/images/Profile.png)

---

### Wireframe Evolution

The wireframes served as the initial visual guide for the project's structure and core user flows.  
However, as development progressed, additional design improvements were made to enhance user experience and align more closely with the brand identity of Strum & Strings.

These improvements included:

- Enhanced visual styling using Bootstrap 5 components.
- Better spacing, typography, and mobile responsiveness adjustments.
- Refinement of the product detail layout to showcase guitars more clearly.
- Streamlining of the checkout flow for a faster, simpler purchasing experience.

While the final website closely follows the original wireframes in structure, certain stylistic and functional improvements were intentionally made during development to deliver a more polished, user-friendly platform.

---

# Features

## Home Page

- Displays a clean hero banner introducing the brand.
- Includes a clear navigation menu with links to shop, profile, cart, and newsletter signup.

## Shop Page

- Displays all available guitars and accessories in a grid layout.
- Users can filter products by category (Acoustic, Electric, etc.).
- Responsive search functionality to find products easily.

## Categories Page

- Displays all 3 categories to give the user the option to search by type.
- Users can filter products by category (Acoustic, Electric, etc.).
- Responsive search functionality to find products easily.

## Product Detail Page

- Displays detailed information for each product:
  - Name, brand, model, price, description.
  - Product images served securely through Cloudinary.
- Includes an “Add to Cart” button and quantity selector.
- Displays related products

## Cart and Checkout

- **Cart Page**:
  - Users can view, edit, or remove products in their shopping cart.
  - Displays a running total and delivery costs.
- **Checkout Page**:
  - Secure Stripe payment redirect
  - Users enter delivery details and complete purchase.
  - Form validation ensures all required fields are correctly completed.
  - Order confirmation page shows the order summary after successful payment.

## Profile and Order History

- Registered users have access to a Profile page.
- Users can:
  - View past orders.
  - Update saved shipping details.

## Newsletter Signup

- User can signup for newsletter with email confirmation.
- Users can submit their email address to receive newsletters about new products and promotions.
- Confirmation message shown after successful signup.

## Admin Panel

- Django Admin interface customized for efficient management:
  - Products, categories, orders, and newsletter subscriptions can be added, edited, or deleted.
- Admins can view all customer orders and manage order statuses.
- Cloudinary images can be edited directly via product admin forms.

---

# Technologies Used

## Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5) – For structuring content.
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) – For styling and layout.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) – For dynamic frontend behaviors.
- [Python 3](https://www.python.org/) – For backend development with Django.
- [SQL (PostgreSQL)](https://www.postgresql.org/) – For the relational database in production.

---

## Frameworks and Platforms

- [Django](https://www.djangoproject.com/) – Backend web framework.
- [Bootstrap 5](https://getbootstrap.com/) – Frontend framework for responsive design.
- [Django-Allauth](https://django-allauth.readthedocs.io/en/latest/) – For user authentication and account management.
- [Gunicorn](https://gunicorn.org/) – WSGI HTTP server for deployment.

---

## Libraries and Tools

- [Stripe](https://stripe.com/) – For secure online payments.
- [Cloudinary](https://cloudinary.com/) – For hosting product images externally.
- [Mailchimp](https://mailchimp.com/) – For newsletter email marketing integration.
- [Balsamiq](https://balsamiq.com/) – For wireframe creation.
- [Git](https://git-scm.com/) – For version control.
- [GitHub](https://github.com/) – For repository hosting and collaboration.
- [Heroku](https://www.heroku.com/) – For live deployment of the Django project.
- [Crispy Forms (Bootstrap5)](https://django-crispy-forms.readthedocs.io/en/latest/) – To improve form styling.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) – To serve static files on Heroku.

---

## Development Tools

- [VS Code](https://code.visualstudio.com/) – Code editor.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/) – Browser tools for debugging.
- [W3C Markup Validator](https://validator.w3.org/) – HTML validation.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) – CSS validation.
- [JSHint](https://jshint.com/) – JavaScript validation.
- [CI Python Linter](https://pep8ci.herokuapp.com/) – Python code validation.

---

# Testing

## Validator Testing

- **HTML**:  
  - All HTML pages were tested using the [W3C Markup Validator](https://validator.w3.org/).
  - Minor warnings were addressed (such as empty `alt` attributes where needed for accessibility).
- **CSS**:  
  - The CSS was tested using the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).
  - No critical errors detected.
- **Python**:  
  - Code was tested with the [CI Python Linter](https://pep8ci.herokuapp.com/).
  - All Python scripts pass with no major PEP8 style issues.
- **JavaScript**:  
  - Custom scripts were tested using [JSHint](https://jshint.com/).
  - No major warnings or errors reported.

---

## Testing Strategy

This section outlines the comprehensive testing approach used for the Strum & Strings e-commerce site. The goal was to ensure all core functionality works as expected across multiple scenarios and devices. Testing includes:

- **Manual Testing**: Performed throughout the development process to verify user flows, business logic, and design responsiveness.
- **Form Validation Testing**: Ensures all forms handle valid and invalid input correctly, including field-level and model-level validation.
- **Authentication Testing**: Covers registration, login/logout, and profile management.
- **Checkout & Payment Testing**: Simulates full order flow using Stripe in test mode.
- **Admin Panel Testing**: Verifies functionality for managing products, orders, and users.
- **Error Handling**: Confirms that friendly 404 pages and validation errors are properly handled.
- **Browser & Device Compatibility Testing**: Ensures the app is usable and responsive on major browsers and screen sizes.

Each testing section below contains specific cases and results.

### Manual Testing Summary

The table below outlines key user flows and whether they performed as expected during testing.

| Category        | Feature                                 | Expected Outcome                                                                | Result |
|-----------------|-----------------------------------------|---------------------------------------------------------------------------------|--------|
| User            | Homepage loads                          | Homepage displays shop now button and background image                          | Pass   |
| User            | User Registration                       | New user can register with valid info and is redirected confirmation page       | Pass   |
| User            | Login/Logout                            | Users can log in and log out successfully                                       | Pass   |
| User            | Profile View                            | Logged-in users can view their details and past orders                          | Pass   |
| User            | Profile Edit                            | Users can update basic details like name and email                              | Pass   |
| User            | Product Listing                         | Products display with image, title, price, and sorting/filtering works          | Pass   |
| User            | Product Detail View                     | Clicking a product shows full detail with image, price, and add-to-cart button  | Pass   |
| User            | Add to Cart                             | Cart updates and displays product, quantity, and total correctly                | Pass   |
| User            | Update Cart Quantity                    | User can adjust quantity in cart and total updates accordingly                  | Pass   |
| User            | Remove from Cart                        | Items can be removed from cart                                                  | Pass   |
| User            | Checkout Process                        | Stripe checkout redirects, payment completes, order is saved                    | Pass   |
| User            | Order Confirmation                      | Confirmation page displays summary after payment                                | Pass   |
| User            | Newsletter Signup                       | Email is submitted, and confirmation message is shown                           | Pass   |
| Admin           | Admin Login                             | Admins can access the Django admin panel using correct credentials              | Pass   |
| Admin           | Access Django Admin Panel               | Full admin panel is visible with models for products, orders, users, etc.       | Pass   |
| Admin           | Manage Products                         | Admins can add, edit, or delete products from both the admin and custom panel   | Pass   |
| Admin           | View Order List                         | Admin dashboard lists all orders with product, quantity, and status             | Pass   |
| Admin           | Edit Order Info                         | Admin can update user details and status of individual orders                   | Pass   |
| Admin           | Manage Newsletter Subscribers           | Admin can view and manage newsletter email signups in the admin panel           | Pass   |
| System/UX       | Responsive Design                       | Site is fully responsive on mobile, tablet, and desktop                         | Pass   |
| System/UX       | 404 Error Page                          | Invalid URL shows friendly custom 404 page                                      | Pass   |
| System/UX       | SEO Tags                                | Meta descriptions and titles set for all pages                                  | Pass   |
| System/UX       | robots.txt and sitemap.xml              | Both files exist and are valid                                                  | Pass   |
| System/UX       | Site Loads on All Major Browsers        | Tested successfully on Chrome, Firefox, Safari, Edge                            | Pass   |

### Responsive Design Testing

Responsiveness was tested across all major pages and screen sizes to ensure a consistent and accessible user experience.

| Device Type | Screen Size (px) | Tested Pages     | Expected Behavior                                               | Result |
|-------------|------------------|------------------|-----------------------------------------------------------------|--------|
| Mobile      | 375×667          | All key pages    | Elements stack vertically, navigation collapses, forms readable | Pass   |
| Tablet      | 768×1024         | All key pages    | Grid layout maintained, cards and inputs scale correctly        | Pass   |
| Desktop     | 1440×900+        | All key pages    | Full layout displays, navigation, carousels and tables align    | Pass   |

### User Registration

| Feature Tested       | Expected Outcome                                          | Actual Result  | Notes                        |
|----------------------|-----------------------------------------------------------|----------------|------------------------------|
| Registration Page    | Registration page loads correctly                         | Pass           |                              |
| Form Submission      | User can register with valid data                         | Pass           |                              |
| Redirect             | User is redirected to email confirmation page             | Pass           |                              |
| Email Confirmation   | Confirmation email is received                            | Pass           |                              |
| Account Activation   | Clicking the confirmation link activates the account      | Pass           | Tested with test email inbox |

### Login Functionality

| Feature Tested         | Expected Outcome                             | Actual Result | Notes |
|------------------------|----------------------------------------------|----------------|-------|
| Login Page             | Login form is displayed                      | Pass           |       |
| Form Submission        | User is logged in with valid credentials     | Pass           |       |
| Redirect After Login   | User is redirected to homepage               | Pass           |       |

### Logout Functionality

| Feature Tested          | Expected Outcome                                              | Actual Result  | Notes |
|-------------------------|---------------------------------------------------------------|----------------|-------|
| Logout Action           | User is logged out and redirected to homepage                 | Pass           |       |
| Access to Protected Page| User cannot view previous pages open to logged in users       | Pass           |       |


### View Product Catalog

| Feature Tested         | Expected Outcome                                                        | Actual Result  | Notes |
|------------------------|-------------------------------------------------------------------------|----------------|-------|
| Shop Button            | Redirects user to All Products page                                     | Pass           |       |
| Product Listings       | All products are displayed and accessible                               | Pass           |       |
| View Details Button    | Clicking shows full product details on a dedicated product page         | Pass           |       |

### Profile View

| Feature Tested     | Expected Outcome                                                      | Actual Result  | Notes                                       |
|--------------------|-----------------------------------------------------------------------|----------------|---------------------------------------------|
| Access Profile Page| Logged-in user can access the profile page                            | Pass           |                                             |
| View Info          | User sees basic info (name, address, email, etc.)                     | Pass           |                                             |
| View Past Orders   | User can view a list of all previous orders                           | Pass           |                                             |
| View Order Details | User can view detailed info for each past order                       | Pass           | Includes product info, prices, and status   |
| Cancel Order       | User can cancel an order directly from the detail view                | Pass           | Status updates accordingly                  |

### Profile Edit Functionality

| Feature Tested   | Expected Outcome                                     | Actual Result  | Notes                                         |
|------------------|------------------------------------------------------|----------------|-----------------------------------------------|
| View Profile     | User sees a form with current profile data prefilled | Pass           |                                               |
| Edit Info        | User updates name, email, address, and other details | Pass           | First name, last name, and email are required |
| Submit Changes   | Updated info is saved and shown on next visit        | Pass           |                                               |

### Product Listing Page

| Feature Tested          | Expected Outcome                                                       | Actual Result | Notes                                  |
|-------------------------|------------------------------------------------------------------------|---------------|----------------------------------------|
| Product Grid            | Products are displayed in a clean, readable grid layout                | Pass          | Grid layout is responsive              |
| Product Details Preview | Each product shows name, price, image, and short description           | Pass          | "View Details" button present          |
| Category Filtering      | Sidebar filters by category                                            | Pass          | Filters update product listings        |
| Brand Filtering         | Sidebar filters by brand                                               | Pass          | Works for all listed brands            |
| Price Filtering         | Sidebar filters by price                                               | Pass          | Prices filter correctly                |

### Product Detail Page

| Feature Tested          | Expected Outcome                                                          | Actual Result  | Notes                                   |
|-------------------------|---------------------------------------------------------------------------|----------------|-----------------------------------------|
| Product Detail Display  | Product name, image, description, and price are shown                     | Pass           |                                         |
| Add to Cart Button      | Button to add product to cart is visible                                  | Pass           |                                         |
| Related Products        | Section displays additional/related products                              | Pass           | Related products shown beneath main     |
| Responsive Layout       | Page displays correctly across screen sizes                               | Pass           | Tested on desktop and mobile            |

### Add to Cart Functionality

| Feature Tested     | Expected Outcome                                                   | Actual Result  | Notes                        |
|--------------------|--------------------------------------------------------------------|----------------|------------------------------|
| Add to Cart Button | Clicking "Add to Cart" adds the product to the cart                | Pass           | Product added successfully   |
| Cart Updates       | Cart icon or count updates to reflect number of items              | Pass           | Visible update confirmed     |
| Cart Page Display  | Product appears in cart with correct name, quantity, and subtotal  | Pass           | Quantity set to 1 by default |

### Update Cart Quantity

| Feature Tested        | Expected Outcome                                                                    | Actual Result  | Notes                                      |
|-----------------------|-------------------------------------------------------------------------------------|----------------|--------------------------------------------|
| Increase Quantity     | Quantity increases and total updates correctly                                      | Pass           |                                            |
| Decrease Quantity     | Quantity decreases and total updates correctly                                      | Pass           |                                            |
| Set Quantity to Zero  | Displays error or prevents submission; does not allow quantity less than 1          | Pass           | Shows validation message for minimum value |
| Invalid Input         | Letters/symbols not accepted in quantity field                                      | Pass           | Validated and restricted to numbers only   |
| Remove from Cart      | User can remove items from cart completely                                          | Pass           |                                            |

### Checkout Process with Stripe

| Feature Tested            | Expected Outcome                                                              | Actual Result | Notes |
|---------------------------|-------------------------------------------------------------------------------|---------------|-------|
| View Cart Page            | Cart shows correct items, quantities, and totals                              | Pass          |       |
| Access Checkout Page      | Checkout form loads with pre-filled user profile info                         | Pass          |       |
| Form Submission           | User completes required fields and continues to payment                       | Pass          |       |
| Stripe Checkout Redirect  | User is taken to Stripe checkout with correct order total                     | Pass          |       |
| Stripe Payment Completion | Payment is processed and user is redirected to success page on live domain    | Pass          |       |
| Order Creation            | Order is saved and visible in admin dashboard and user profile order history  | Pass          |       |

### Order Confirmation Page

| Feature Tested         | Expected Outcome                                                                | Actual Result | Notes |
|------------------------|---------------------------------------------------------------------------------|---------------|-------|
| Payment Completion     | After successful Stripe payment, user is redirected to confirmation page        | Pass          |       |
| Order Summary Display  | Page shows order number, product(s), quantity, prices, and grand total          | Pass          |       |

### Newsletter Signup – Email Validation & Confirmation

| Feature Tested             | Expected Outcome                                                                 | Actual Result | Notes                                    |
|----------------------------|----------------------------------------------------------------------------------|---------------|------------------------------------------|
| Invalid Email Submission   | Form does not submit and shows a validation error                                | Pass          | Validation blocks malformed emails       |
| Valid Email Submission     | Email is sent to user for confirmation                                           | Pass          | Tested using temporary email address     |
| Email Confirmation Flow    | Clicking confirmation link redirects user back to homepage                       | Pass          | Confirms subscription and redirects user |

### Newsletter Signup Functionality

| Feature Tested                       | Expected Outcome                                                                 | Actual Result | Notes                                     |
|--------------------------------------|----------------------------------------------------------------------------------|----------------|--------------------------------------------|
| Valid Email Input                    | User enters a valid email and is redirected to Mailchimp for confirmation        | Pass           | JS validation in place                     |
| Invalid Email Format                 | User enters an invalid email and is blocked from submitting                      | Pass           | Custom validity message shown              |
| Duplicate Email Check (Existing)     | If email is already in database, user is shown a message and not redirected      | Pass           | No duplicate stored                        |
| New Email Submission                 | New emails are stored in the database and passed to Mailchimp                    | Pass           | Data stored via `/save-email/` endpoint    |
| Email Confirmation Link              | After subscribing via Mailchimp, user receives a confirmation email              | Pass           | Tested with temp email                     |
| Confirmation Redirect                | After clicking Mailchimp confirmation, user is returned to the success page      | Pass           | Link redirects to `newsletter_success.html`|
| Success Page Styling                 | Page matches site design and thanks the user                                     | Pass           | Custom CSS implemented                     |

### Contact Us Form Functionality

| Step | Action                          | Expected Outcome                                                                 | Result |
|------|---------------------------------|----------------------------------------------------------------------------------|--------|
| 1    | Navigate to the Contact Us page | Page loads with styled form and fields for name, email, subject, and message     | Pass   |
| 2    | Submit empty form               | Validation errors appear; form is not submitted                                  | Pass   |
| 3    | Submit form with invalid email  | Validation error shown for email field                                           | Pass   |
| 4    | Submit form with valid data     | Form submits, user sees confirmation message that message has been sent          | Pass   |

### Contact Message Admin View Test

| Step | Action                                  | Expected Outcome                                                                 | Result |
|------|-----------------------------------------|----------------------------------------------------------------------------------|--------|
| 1    | Log in to the Django admin panel        | Admin dashboard loads successfully                                               | Pass   |
| 2    | Navigate to the "Contact messages" tab  | List of all submitted contact messages is visible with names, email, etc.        | Pass   |
| 3    | Click on a message to view details      | Full details (name, email, subject, message, timestamp) are displayed clearly    | Pass   |
| 4    | Confirm no duplicate entries            | Each message appears only once                                                   | Pass   |

### Admin Access Control Test

| Step | Action                                                             | Expected Outcome                                                     | Result |
|------|--------------------------------------------------------------------|----------------------------------------------------------------------|--------|
| 1    | Log in as a non-staff user                                         | Redirected to Django admin login page when accessing restricted URLs | Pass   |
| 2    | Log in as a staff/admin user                                       | Can access all admin-specific sections of the site                   | Pass   |
| 3    | Try accessing `/accounts/admin-dashboard/` as non-staff            | Redirected to Django admin login page                                | Pass   |
| 4    | Try accessing `/accounts/admin-dashboard/newsletter/` as non-staff | Redirected to Django admin login page                                | Pass   |
| 5    | Try accessing `/admin/` as staff                                   | Admin panel loads successfully                                       | Pass   |


## Bugs Encountered

- **Media Storage During Deployment**:  
  - Issue: Images did not appear after deployment to Heroku initially.  
  - Fix: Implemented Cloudinary storage for all media files.

- **Cart Quantity Updating**:  
  - Issue: Minor bug with cart quantities not updating immediately on small screens.  
  - Fix: Adjusted JavaScript event listeners and now updates instantly.

- **Stripe Webhook Connection**:  
  - Issue: Stripe webhook was not connecting properly in local testing.  
  - Fix: Configured Stripe CLI to forward events to localhost and corrected webhook handler.

---

## Overall Testing Results

- Every feature and flow was manually tested.
- Validation errors were corrected during development.
- Final deployed site behaves as expected across different screen sizes and devices.

# Deployment

This project was deployed using **Heroku** with the following process:

---

## Initial Setup

- The codebase was pushed to [GitHub](https://github.com/).
- The project uses a PostgreSQL database in production, configured through Heroku add-ons.
- Static files are managed using **Whitenoise**.
- Media files (product images) are managed and delivered through **Cloudinary**.

---

## Deployment Steps

1. Created a new app on [Heroku](https://dashboard.heroku.com/).
2. Set up environment variables on Heroku:
    - `DATABASE_URL` (Heroku Postgres)
    - `SECRET_KEY`
    - `CLOUDINARY_URL`
    - `STRIPE_PUBLIC_KEY`
    - `STRIPE_SECRET_KEY`
    - `STRIPE_WH_SECRET`
3. Added required Buildpacks:
    - Python
    - NodeJS
4. Connected the GitHub repository to the Heroku app.
5. Enabled **automatic deployments** from the `main` branch.
6. Pushed the code to GitHub, triggering the first deployment build on Heroku.
7. Ran the following commands:
    - `python manage.py collectstatic`
    - `python manage.py migrate`
8. Verified static and media files were properly collected and accessible.
9. Performed a full end-to-end functionality test on the live Heroku URL.

---

## Cloudinary Integration

- Set up a free Cloudinary account.
- Uploaded all product images manually.
- Updated product records in the Django Admin panel with Cloudinary URLs.
- Integrated Cloudinary storage into Django settings for secure media hosting.

---

## Stripe Payment Integration

- Configured Stripe account settings.
- Created a webhook endpoint to listen for payment confirmation events.
- Used **Stripe CLI** during local testing to simulate webhook events.
- Confirmed through CLI local testing however no real payments processed due to test card not being functional.

---

## Final Live Application

- The website is live and fully functional at:  
  [Strum & Strings Heroku Deployment](https://strum-and-strings-e5017bc28566.herokuapp.com//)

## Marketing Strategies

### Facebook Business Page

To strengthen brand visibility and engage directly with the target audience, I created a dedicated **Facebook Business Page** for **Strum & Strings**.  
This page is used to:

- Promote new products, bundle deals, and seasonal sales.
- Share guitar-related tips, tutorials, and engaging content.
- Build a community of musicians, students, and institutions.
- Enhance credibility and increase organic brand reach via social media.

The Facebook page also provides a direct channel for customer inquiries, helping to improve the overall user experience and support service.  
This step fulfills the project’s marketing requirement of establishing a real-world online presence for the business.


![Strum and strings FB business page](static/images/FB_business_page.jpg)
---

### Newsletter Integration

To further enhance customer engagement and brand loyalty, I integrated a **newsletter signup form** on the website using **Mailchimp**.  
This signup form allows visitors to:

- Subscribe for exclusive offers, product updates, and musical tips.
- Stay informed about new arrivals, limited-time bundles, and promotions.

The newsletter strategy is designed to build a growing customer mailing list, supporting future email marketing campaigns and personalized offers.

Both the Facebook page and the newsletter system work together to maximize reach, engagement, and retention of the Strum & Strings customer base.


# Credits

## Content and Resources

- **Wireframes** created using [Balsamiq](https://balsamiq.com/).
- **Hero Images and Product Images** hosted via [Cloudinary](https://cloudinary.com/).
- **Payment Processing** implemented using [Stripe](https://stripe.com/).
- **Newsletter Signup** handled using [Mailchimp](https://mailchimp.com/).
- **Static and Media Files** managed using [Whitenoise](http://whitenoise.evans.io/en/stable/) and Cloudinary.
- **Django Documentation** provided guidance for backend setup and deployment.
- **Bootstrap Documentation** helped design responsive, mobile-first layouts.
- **Boutique Ado** I refered to the previous project to help structure my approach.
- **Slack** Used for help when coming across probelms from felow students


---

# Acknowledgements

- Thanks to [Code Institute](https://codeinstitute.net/) for providing excellent support over the last 3 months through some personal issues.
- Despite the challenges of taking a three-month leave of absence, the ongoing encouragement—and especially my partner’s support over the past two weeks—has been instrumental in helping me complete this project

---

# Final Project Feelings

- Returning to this project after a three-month break was challenging and slow at first. Since then, I’ve worked around the clock—revisiting fundamentals when needed—to bring it to its current state. While I’m proud of what I’ve achieved so far, there’s still plenty of room for growth, and I plan to keep developing it both to sharpen my coding skills and to showcase on my résumé.

# Future Implementations

While the current version of Strum & Strings achieves all primary goals, there are potential enhancements planned for future versions:

- Implement product review and rating functionality.
- Create a loyalty program or rewards system for repeat customers.
- Offer premium subscriptions with access to exclusive online guitar tutorials.
- Expand the product catalog to include more accessories and merchandise.
- Add a "Wishlist" feature to allow users to save products for later.

---
