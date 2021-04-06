artist = ["eminem","kali","dziarma"]
songs = {"eminem":["killa shot","rap god"],
         "kali":["sentymentalnie","yakuza"],
         "dziarma":["fajan baba","nie wiem"]}
em= songs["eminem"]
eminem=" ".join(em)
ka= songs["kali"]
kali=" ".join(ka)
dz= songs["dziarma"]
dziarma=" ".join(dz)
inp = input("wpisz nazwe raper\nWybierz z kali,dziarma,eminem\n")
if inp == str("eminem"):
    print(emienm)
if inp == str('dziarma'):
    print(dziarma)
if inp == str('kali'):
    print(kali)
#for song in songs:
#    print()