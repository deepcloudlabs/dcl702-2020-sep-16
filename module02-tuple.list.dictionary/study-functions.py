def fn(n=7):
    while n > 1:
        print(f"fn() is yielding {n}")
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1


def sq(numbers):
    for n in numbers:
        print(f"sq() is yielding {n*n}")
        yield n * n


# print(fn())
# print(fn(11))
for num in sq(fn(11)): # pipeline
    print(f"for loop: {num}")
