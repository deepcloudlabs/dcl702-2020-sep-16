x = 42
print(type(x))
x = (0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3)
print(type(x))
print(x)
y = (0.1 + 0.2) + 0.3
print(type(y))
print(y)
x = 2 ** 100
print(x)
x = 3 / 2
print(x)
x = "2"
y = 1
# z = x + y
print(isinstance(x, (int, float, str)))
y = None
print(y is not None)
x = """
   This is 
   an 
            example
"""
print(f"x={x}")
print("x: %-s, y: %12.2f" % (x,y))