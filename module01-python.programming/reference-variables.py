def add_element(lst, el):
    # copied = lst.copy()
    lst.append(el)


a = [4, 8, 15, 16, 23, 42]
b = a
print(b)
add_element(a, 72)
print(a)
print(b)
