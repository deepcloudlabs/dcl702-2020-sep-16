import collections

lst1 = [4, 8, 15, 16, 23, 42, True, "Jack", None]
print(len(lst1))
tup1 = ('jack', 'kate', 'james')
lst2 = list(tup1)
print(lst2)
# tup1[0] = "Jack"
lst2[0] = "Jack"
print(lst2)
lst3 = range(10)
for v in lst3:
    print(v)
print(lst2)
lst2.append("ben")
lst2.insert(0, "jin")  # high cost
deq1 = collections.deque(lst2)
print(lst2.pop(0))
print(lst2)
lst2.remove('ben')
print(lst2)
print("Jack" in lst2)
print("Jack" not in lst2)

lst4 = [1, 2, 3, "four"]
lst4.extend([5, "six", 7])
print(lst4)

lst5 = ["ben", "jack", "James", "jin", "kate", "ben", "sun"]
print(lst5)
lst5.sort(reverse=True)
print(lst5)
sort_ignore_case = lambda _: _.lower()
print(type(sort_ignore_case))
lst5.sort(key=sort_ignore_case)
print(lst5)
lst5.sort(key=lambda x: len(x))
print(lst5)
lst5.sort(key=len)
print(lst5)

