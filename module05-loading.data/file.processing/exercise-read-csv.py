import csv

with open("countries.csv",mode="rt") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)