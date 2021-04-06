pi = 3.14159

def addTwo (x):
    return x + 2

def subTwo (number):
    return number - 2

def sphere (radius):
    v=4/3 * pi * radius**3
    return v

def multi (v):
    m=sphere(v)**v
    return m

newNumber = addTwo(7)
newx = subTwo(10)
print(newNumber, newx, sphere(2))
print (multi(2))

