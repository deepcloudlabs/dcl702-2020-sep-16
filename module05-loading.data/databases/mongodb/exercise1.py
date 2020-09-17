from pymongo import MongoClient
from pprint import pprint as pp

# http://binkurt.blogspot.com/2015/02/mongodb-ile-calsmak.html

client = MongoClient("mongodb://localhost:27017")
world = client['world']
countries = world.countries1
for country in countries.find({"continent": "Asia"}).sort("population", -1):
    pp(country)
