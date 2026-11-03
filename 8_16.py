def city_country(city, country):
    return f"{city}, {country}"

# Cara 1
import renai

print(renai.city_country("Surakarta", "Indonesia"))
 
# Cara 2
from renai import city_country

print(renai("Tokyo", "Jepang"))

# Cara 3
from renai import city_country as fn

print(fn("Paris", "Prancis"))

# Cara 4
import renai as mn

print(mn.city_country("London", "Inggris"))

# Cara 5
from renai import *

print(city_country("Seoul", "Korea Selatan"))