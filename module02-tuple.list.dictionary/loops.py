numbers = [3, 7, 9, 11, 6, 0, 8]
i = 0
for num in numbers:
    print(f"{i}: {num}")
    i = i + 1

for k, num in enumerate(numbers):
    print(f"{k}: {num}")

names = ["jack", "kate", "james"]
people = {}  # dictionary
for order, name in enumerate(names):
    people[name] = order + 1
print(people)
