import json

with open("countries.json", "rt") as file:
    countries = json.load(file)
    print(countries)
