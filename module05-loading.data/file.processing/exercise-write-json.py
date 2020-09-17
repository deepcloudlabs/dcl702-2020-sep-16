import json

countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "pop": 80000000},
    {"code": "gre", "name": "greece", "continent": "europe", "pop": 10000000},
    {"code": "fra", "name": "france", "continent": "europe", "pop": 70000000},
    {"code": "ger", "name": "germany", "continent": "europe", "pop": 80000000}
]

with open("countries.json", "wt") as file:
    json.dump(countries,file)