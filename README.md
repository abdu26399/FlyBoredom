# FlyBoredome

The following describes what you need to do for each module.

## Offer Module

**Path:** `/`

This is the front page of the website. The page will retrieve the latest offers from the database and display them. Each offer will be within a card. The card will contain the following information:

- Title
- Event ID
- Location
- Description
- Price per person
- Picture(s)
- Add to Cart button

Since these are the "latest" offers, the post information will be time-stamped. The time-stamp does not need to be displayed on the card, it will be used to determine which offers are the latest.

## Cart and Booking Module

**Path:** `/cart`

This page will display the items that the user has added to their cart. To do this, when the user clicks the "Add to Cart" button on the offer page, the offer ID can be stored in the user's session. The cart page will then retrieve the offer IDs from the session and display the offers title within their respective cards. (Refer to how Amazon does this)

Each card will contain the following information:

- Title
- Event ID
- A plus/minus button to increase/decrease the number of people
- Total price
- Input field for the user to enter first and last names of the people in their party
- Button to remove the offer from the cart

For each card, repeate the number of name fields as the number of people. For example, if the user has selected 3 people, then there should be 3 name fields (first and last name).

After the all the cards, there should be fields for the user to enter their first and last name, email address, and phone number. There should also be a button to submit the booking. These should also be disabled if the cart is empty.

**Path:** `/bookings`

This page will display all the bookings that the user has made. Retrieve the booking information from the database and display the booking information within their respective cards.

Each card will contain the following information:

- Title
- ID
- List of attendees

## Testimonials Module

**Path:** `/testimonials`

This page will display all the testimonials that the user has made. Retrieve the testimonial information from the database and display the testimonial information within their respective cards. Make sure only the logged in user can add a testimonial.

Add new testimonials card will contain the following information:

- Title
- Location from the list of locations
- Text area for the user to enter their testimonial
- Option to add pictures
- Submit button

All testimonials card will contain the same information as the add new testimonials card, but will retrieve the information from the database.

## Authentication Module

**Path:** `/login`

This page will allow the user to login. The user will enter their email address and password. If the user does not have an account, they can click a link to register.

**Path:** `/register`

This page will allow the user to register. The user will be required the following information:

- First name
- Last name
- Email address
- Password

## Admin Module

**Path:** `/admin`

This page will allow the admin to add new offers. And view all the bookings and testimonials. The admin will be able to delete bookings and testimonials.