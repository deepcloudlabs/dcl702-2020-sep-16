import csv

countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "pop": 80000000},
    {"code": "gre", "name": "greece", "continent": "europe", "pop": 10000000},
    {"code": "fra", "name": "france", "continent": "europe", "pop": 70000000},
    {"code": "ger", "name": "germany", "continent": "europe", "pop": 80000000}
]
countries1 = [
    ["tur", "turkey", "asia", 80000000]
]

with open("countries.csv", mode="wt", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(list(map(lambda d: d.values(), countries)))
