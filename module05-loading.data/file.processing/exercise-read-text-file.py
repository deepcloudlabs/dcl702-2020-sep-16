with open("countries.txt", mode="rt") as countries:
    for country in countries:
        code,name,continent,population = country.split(",")
        print(f"{code}\t{name}\t{continent}\t{population}")