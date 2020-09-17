import pandas as pd

countries = pd.DataFrame([
    ["tur", "turkey", "asia", 80000000],
    ["fra", "france", "europe", 70000000],
    ["gre", "greece", "europe", 10000000]
], columns=["code", "name", "continent", "population"])

countries.to_csv("countries-panda.csv")
