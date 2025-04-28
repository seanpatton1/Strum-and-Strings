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

1. [Business Model](#business-model)
2. [User Experience (UX)](#user-experience-ux)
    - [Project Goals](#project-goals)
    - [Implementation](#implementation)
    - [Color Scheme](#color-scheme)
    - [Typography](#typography)
    - [Database Models](#database-models)
    - [Wireframes](#wireframes)
3. [Features](#features)
    - [Home Page](#home-page)
    - [Shop Page](#shop-page)
    - [Product Detail Page](#product-detail-page)
    - [Cart and Checkout](#cart-and-checkout)
    - [Profile and Order History](#profile-and-order-history)
    - [Newsletter Signup](#newsletter-signup)
4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Libraries and Programs](#libraries-and-programs)
5. [Testing](#testing)
    - [Validator Testing](#validator-testing)
    - [Manual Testing](#manual-testing)
6. [Deployment](#deployment)
7. [Credits](#credits)
8. [Acknowledgements](#acknowledgements)
9. [Future Implementations](#future-implementations)

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

## Manual Testing

Below is a summary of manual testing carried out across the site:

| Feature                          | Expected Outcome                                            | Result  |
| --------------------------------- | ----------------------------------------------------------- | ------- |
| Site loads on all major browsers | Website loads correctly on Chrome, Firefox, Safari, Edge    | Pass |
| Responsive Design                | Site adapts well on desktop, tablet, and mobile devices      | Pass |
| User Registration                | Users can register accounts and log in/out successfully      | Pass |
| Product Browsing                 | Products are listed, filterable, and searchable              | Pass |
| Product Detail View              | Full product info visible and Add to Cart works              | Pass |
| Shopping Cart                    | Cart updates correctly with quantities and prices           | Pass |
| Checkout Process                 | Stripe payment completes successfully, order confirmed       | Pass |
| Profile Page                     | Users can view past orders and edit profile info             | Pass |
| Admin Access                     | Admins can manage products, orders, and user profiles        | Pass |
| Newsletter Signup                | Email subscription form submits and shows confirmation      | Pass |
| 404 Error Handling               | 404 page displays friendly error page for bad URLs           | Pass |
| SEO Basics (Meta Descriptions)    | Meta descriptions added for all pages                       | Pass |
| Robots.txt and Sitemap.xml       | Robots.txt and sitemap.xml files exist and are valid         | Pass |

---

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
  [Strum & Strings Heroku Deployment](https://strum-and-strings-e5017bc28566.herokuapp.com//) 🚀

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
