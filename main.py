import requests

API_URL = 'https://fakerapi.it/api/v1/'

# Task 1: Make GET call to get some companies:

api_call = 'companies?_quantity=3'
r = requests.get(API_URL + api_call)
for company in r.json()["data"]:
    print(
        str(company["id"]),
        company["name"],
        company["country"],
        company["website"],
        sep = ", "
        )
    
print("\n")

# Task 2: Make GET call to get 50 persons with English names who were born after 1994:

api_call = 'persons?_quantity=50&_locale=en_EN&_birthday_start=1994-01-01'
r = requests.get(API_URL + api_call)
for person in r.json()["data"]:
    print(
        str(person["id"]),
        f'{person["firstname"]} {person["lastname"]}' ,
        person["birthday"],
        sep = ", ",
        end = " - "
        )

print("\n")

# Task 3: Make GET call to get 5 German companies:

api_call = 'companies?_quantity=5&_locale=de_DE'
r = requests.get(API_URL + api_call)
for company in r.json()["data"]:
    print(
        str(company["id"]),
        company["name"],
        company["country"],
        sep = ", ",
        end = " - "
        )

print("\n")

# Task 4: Make GET call to retrieve 60 credit cards of Spanish people:

api_call = 'credit_cards?_quantity=60&_locale=es_ES'
r = requests.get(API_URL + api_call)
for card in r.json()["data"]:
    print(
        card["type"],
        card["owner"],
        sep = ", ",
        end = " - "
        )

print("\n")

# Task 5: Make GET call to retrieve 47 products that cost higher than 50€:



# Task 6: Make GET call to retrieve 10 Custom objects with "pokemon", "website", and "name" fields:


