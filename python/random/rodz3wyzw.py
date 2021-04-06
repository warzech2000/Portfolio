#porównywanie liczb
""" 
liczba=int(input("wprowadz liczbe: "))
if liczba <= 10:
   print("Liczba jest mniejsza, badz rowna 10")
elif liczba > 10 and liczba <=25:
    print("twoja liczba jest w przedziale 10-25")
else:
    print("Twoja liczba jest wieksza od 25")
"""
#try except mod,dzielenie
"""
def mod(liczba1, liczba2):
     return liczba1 % liczba2
def dzi(liczba1, liczba2):
     return liczba1 / liczba2
try:
    liczba1=int(input("wprowadz liczbe: "))
    liczba2 =int(input("wprowadz druga liczbe: "))
    x= mod(liczba1,liczba2)
    y= dzi(liczba1,liczba2)
    print(x, y)
except(ValueError, ZeroDivisionError):
    print("Zle dane")
"""