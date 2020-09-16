"""
Tuple: Immutable
List: Allows Duplicate, Sorted
Set: Does not allow duplicate
Dictionary: (Key->Value)
collections
"""

tup1 = 4, 8, 15, 16, 23, 42

print(tup1)

tup2 = (4, 8, 15, 16), (23, 42)
print(tup2)

tup3 = tuple("jack")
print(tup3[2])
print(len(tup3))

tup4 = tuple(['Jack', [4, 8], True])
print(tup4[2])
# tup4[2] = False # error
# tup4[1]= [4, 8, 15] # error
tup4[1].append(15)
tup4[1].append(16)
print(tup4[1])

tup5 = (1, 2, (3, 4))
a, b, (c, d) = tup5  # unpacking
print(f"{a},{b},{c},{d}")

tup6 = (1, 2, 3, 4, 5, 2, 5, 9, 2, 4, 7, 2)
a, b, *rest = tup6  # unpacking
print(f"{a},{b}")
print(f"rest={rest}")
print(f"tup6.count(2): {tup6.count(2)}")
