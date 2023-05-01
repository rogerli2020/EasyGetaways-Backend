# EasyGetaways-Backend
 Backend Django application for the Easy Getaways application for Design Project (CS-UY 4523).

## Install Directions
- Set up a Python virtual environment
- Install all dependencies listed in requirements.txt by running pip install -r requirements.txt.

## Reminder:
- Change the SECRET_KEY before production deployment. 
- Don't use real username/password during development process...

## Endpoints (SUBJECT TO CHANGE):
Subject to change.
- dj-rest-auth/ login/
    - Method: POST
    - Request Fields Required:
        - username
        - password
    - Response (if credentials are valid):
        - access_token
        - refresh_token
- dj-rest-auth/ registration/
    - Method: POST
    - Request Fields Required:
        - username
        - password1
        - password2
    - Response (if credentials are valid):
        - access_token
        - refresh_token
- itineraries/ get_all_user_itin/ 
    - Returns all of the itineraries created by the logged in user.
    - Method: GET
    - Request Fields Required:
        - uid
        - access_token
- itineraries/ insert_new_itin/ 
    - Given an itinerary and user id, insert the itinerary into table.
    - Method: POST
    - Request Fields Required:
        - uid
        - itinerary (the JSON file containing the actual itinerary)
    - Optional Fields:
        - archived (a boolean value that determines if the itinerary is archived.)
        - private (a boolean value that determines if the itinerary is private.)    
        - city (string, the city in which the itinerary is relevant.)
        - state (string, the state of the relevant city.)
        - country (string, the country of the relevant state.)
        - title (string, title of the itinerary.)
        - est_budget_up (int, upper limit of budget estimate.)
        - est_budget_down (int, lower limit of budget estimate.)
- itineraries/ edit_itin/ 
    - Edit the information of a given itinerary in the database.
    - TODO.
- itineraries/ get_public_itin/
    - TODO: what if there's a lot of public itineraries? The server can't just return all of them.
    - Returns all public itineraries by all users.
    - Method: POST
    - Does not require a request body.
- itineraries/ get_itin/
    - Get the itinerary information of a given database.
    - Required Fields:
        - tid (t stands for itinerary... which I know doesn't make sense)
        - uid (relevant if the itinerary is private, but it's required anyway)
        - jwt (relevant if the itinerary is private, but it's required anyway)
- ... Look at view.py for more detail.