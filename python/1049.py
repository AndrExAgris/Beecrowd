vert = input()
esp = input()
ali = input()
if vert == "invertebrado":
    if esp == "inseto":
        if ali == "hematofago":
            print("pulga")
        else:
            print("lagarta")
    else:
        if ali == "hematofago":
            print("sanguessuga")
        else:
            print("minhoca")
else:
    if esp == "ave":
        if ali == "carnivoro":
            print("aguia")
        else:
            print("pomba")
    else:
        if ali == "onivoro":
            print("homem")
        else:
            print("vaca")
