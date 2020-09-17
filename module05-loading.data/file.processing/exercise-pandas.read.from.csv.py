import pandas as pd

countries = pd.read_csv("countries-panda.csv")
print(countries.info())
print(countries.describe())
print(countries.index)
print(countries.columns)
print(countries)
