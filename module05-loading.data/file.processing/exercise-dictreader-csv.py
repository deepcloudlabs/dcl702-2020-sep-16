import csv

with open("countries.csv",mode="rt") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(dict(row))