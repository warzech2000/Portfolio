import os
os.system('cls' if os.name == 'nt' else 'clear')

ja={"wiek":"19",
    "wzrost":"176",
    "telefon":"696969",
    "zamieszkanie":"brodla",}
wiek=ja["wiek"]
wzrost=ja["wzrost"]
telefon=ja["telefon"]
zamieszkanie=ja["zamieszkanie"]

x=0

def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

os.system('clear')
print("Możesz zapytac o to ile mam lat,wzorstu,telefon,mieszkam \n")
print("wpisz wiek,wzrost,telefon,zamieszkanie\n")

while x < 30 :
    inp=input()    
    if inp == str("wiek"):
        os.system('clear')
        print("Mam " +wiek+" lat""\nw grudniu "+str(int(wiek)+1)+" lat")

    elif inp == str("wzrost"):
        os.system('clear')
        print("Mam " +wzrost+"cm""\nw parowie "+str(int(wzrost)-159)+"cm") 

    elif inp == str("telefon"):
        os.system('clear')
        print("Mój nr telefonu to: " +telefon) 

    elif inp == str("zamieszkanie"):
        os.system('clear')
        print("Mieszkam w " +zamieszkanie+"ch""\nza poltora roku juz krk") 
    elif len(inp)==0:
        x+=1
        os.system('clear')
        print("Wpisz wiek,wzrost,telefon lub zamieszkanie")
    elif len(inp) > 0 and str(inp) != "wiek" or "wzrost" or "telefon" or "zamieszkanie":
        x+=1
        os.system('clear')
        print("cos chyba zle wpisales")
    else:
        print("oj chyba mamy blad ;c")
        

        