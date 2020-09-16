from functools import reduce

numbers = [4, 8, 15, 16, 23, 42]

sum = 0
for number in numbers:
    if number % 2 == 0:
        sum = sum + number * number
print(f"sum: {sum}")
is_even = lambda n: n % 2 == 0
squared = lambda n: n * n
add = lambda acc, n: acc + n
print(reduce(add, map(squared, filter(is_even, numbers)), 0)) # pipeline
