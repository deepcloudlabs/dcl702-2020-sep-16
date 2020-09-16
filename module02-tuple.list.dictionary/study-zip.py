names = ["jack", "kate", "james"]
ages = [47, 36, 42]
professions = ["doctor", "manager", "engineer"]
people = zip(names, ages, professions)
for name_age in people:
    name, age, profession = name_age  # unpacking
    print(f"{name}, {age}, {profession}")
