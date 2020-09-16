names = ["jack", "ben", "kate", "james", "jin", "sun"]

for name in names:
    print(name)

for i in range(10):
    print(i)

area_codes = {"ankara": 312, "istanbul-anadolu": 216, "istanbul-avrupa": 212}
for city in area_codes.keys():
    print(f"{city}: \t{area_codes[city]}")
for code in area_codes.values():
    print(code)
for city, code in area_codes.items():
    print(f"{city}: \t{code}")
area_codes["key"] = 1
print(area_codes["ankara"])

n = 7
while n > 1:
    print(f"n:{n}")
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
