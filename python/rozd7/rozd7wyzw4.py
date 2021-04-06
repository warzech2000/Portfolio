liczby = (2,3,10)
while True:
    inp=input("wprowadz liczbe 0-20:\n")
    inp = int(inp)
    if inp == "q":
        break
    elif inp in liczby:
        print("wygrales")
        break
    else:
        print("jeszcze raz")