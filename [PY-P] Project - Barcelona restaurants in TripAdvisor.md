# [PY-P] Project - Barcelona restaurants in TripAdvisor

## Introduction

**TripAdvisor** is a US travel and restaurant website company that shows hotel and restaurant reviews, accommodation bookings and other travel-related content. Headquartered in Needham, Massachusetts, TripAdvisor is the largest "social travel website" in the world, with about 315 million reviewers (active and inactive) and about 500 million reviews of hotels, restaurants, attractions and other travel-related businesses. TripAdvisor was an early adopter of user-generated content. The website services are free to users, who provide most of the content, and the website is supported by a hotel booking facility and an advertising business model.

TripAdvisor proposals are grouped in different categories, such as *Hotels*, *Things to do*, *Restaurants*, *Flights*, etc. The data for this project have been scraped from the webpages devoted to Restaurants in Barcelona. The starting URL is `tripadvisor.com/Restaurants-g187497-Barcelona_Catalonia.html`. Note that `g187497` identifies Barcelona. Replacing `.com` by `.es`, we get the Spanish version. The information is about the same, but `tripadvisor.es` shows reviews on Spanish (some of them are automatic translations from English), while `tripadvisor.com` shows reviews in English.

The data for this example have been captured in April, 2023. At that time, 8,662 restaurants from Barcelona were posted at `tripAdvisor.com`. For this example, only the 450 top ranked restaurants have been selected.

## The data set

In the data set, every row corresponds to a restaurant. The columns are:

* `rank`, the current rank of the restaurant in TripAdvisor.

* `name`, the name of the restaurant as it appears in the TripAdvisor's URL's. Example: 'BelleBuon'.

* `id`, a unique identifier for the restaurant. This ID is expected to be found as part of the link to the restaurant, in the same way that the ID of Barcelona ('g187497') is found as part of the URL of the restaurants in Barcelona. Example: 'd12207253'.

* `bubble`, the number of bubbles that approximate the average rating of the restaurant. It comes as a multiple of 0.5.

* `reviewCount`, the total number of reviews for that restaurant.

* `priceRange`, with values 'Fine Dining', 'Mid-range' y 'Cheap Eats'. In the webpage, these categories are indicated with dollar symbols ('\$\$\$\$', '\$\$ - \$\$\$' and '\$', respectively).

* `claimed`, a True/False column indicating whether the restaurant's page displays the message "Claimed" on the right side of the restaurant's name. This message tells us that somebody from the business manages the listing.

* `travelers`, a True/False column indicating whether the restaurant has a Traveler's Choice Award.

* `photos`, the number of photos of that restaurant available at its website. It is shown in a link 'See all (# photos)'.

* `thefork`, a True/False column indicating whether the restaurant has an option for reserving a table through TheFork.

* `justeat`, a True/False column indicating whether the restaurant has an option for ordering online to get food delivered by Just Eat.

* `cuisines`, a collection of culinary options placed in the *Details* section of the page, under the heading *CUISINES*. It may be missing. Example: 'Italian, Mediterranean, European, Northern-Italian, Southern-Italian'.

* `diets`, a collection of dietary options placed in the *Details* section, under the heading *SPECIAL DIETS*. It may be missing. Example: 'Vegetarian Friendly, Vegan Options, Gluten Free Options'.

* `meals`, a collection of meal's options placed in the *Details* section, under the heading *MEALS*. It may be missing. Example: 'Lunch, Dinner, Drinks'.

* `features`, a collection of features placed in the *Details* section, under the heading *FEATURES*. It may be missing. Example: 'Reservations, Outdoor Seating, Seating, Serves Alcohol, Full Bar, Free Wifi, Accepts Credit Cards, Table Service, Wine and Beer, Dog Friendly, Gift Cards Available'.

* `neigh`, the neighborhood where the restaurant is. It is placed in the *Location and contact* section. Example: 'El Baix Guinardo'.

* `excellent`, the number of reviews in English with rating 5.

* `verygood`, the number of reviews in English with rating 4.

* `average`, the number of reviews in English with rating 3.

* `poor`, the number of reviews in English with rating 2.

* `terrible`, the number of reviews in English with rating 1.

* `revEnglish`, the number of reviews in English.

* `revSpanish`, the number of reviews in Spanish.

## Questions

Q1. Import the data to a Pandas data frame, with the restaurant ID as the index. Check the content.

Q2. How is the distribution of the number of reviews? And the number of photos? Are they related?

Q3. The proportion of reviews in English can be used as an indicator of how "touristic" is a restaurant. Examine the distribution of this proportion.

Q4. Have more expensive restaurants a higher proportion of reviews in English?
 
