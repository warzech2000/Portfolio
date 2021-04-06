# do kwadratu
"""
x=int(input("wprowadz liczbe: "))
def sqr(x):
    return x**2
print(sqr(x))
"""
# lancuch znakow
"""
x=str(input("insert>>"))
print(x)
"""
#wiele parametrow
x=int(input("podaj liczbe: "))
y=int(input("razy ile mnozymy: "))
z=int(input("do jakiej potegi: "))

def dzialanie(x,y=10,z=2):
    d = (x*y)**z
    print(d)
dzialanie(x,y,z)
