import random


def jelszo_kimentese(mihez, jelszo):
    file = open("jelszavak.txt", "a", encoding="utf-8")
    file.write(mihez + ": " + jelszo + "\n")
    file.close()


def random_jelszo(hossz, mihez):
    try:
        kimenet = ""
        karakterek = []
        file = open("karakterek.txt", "r", encoding="utf-8")
        for sor in file:
            karakterek.append(sor.strip())
        file.close()
        
        for _ in range(hossz):
            kimenet += random.choice(karakterek)
        jelszo_kimentese(mihez, kimenet)
        return kimenet
    except:
        return "Nincs meg a 'karakterek.txt'!"


def jelszo_betoltese():
    try:
        file = open("jelszavak.txt", "r", encoding="utf-8")
        for sor in file:
            print(sor)
        file.close()
    except:
        print("Nincs még jelszavad!")


futas = True
while futas:

    try:
        parancs = int(input("Add meg a parancsot (1: új jelszó, 2: eddigi jelszavak, 3: kilépés): "))
        if parancs == 1:
            print()
            hossz = int(input("Hány karakterből álljon a jelszó: "))
            mihez = input("Mihez lesz a jelszavad (pl.: Google fiók, Steam fiók): ")
            print(f" A jelszavad: {random_jelszo(hossz, mihez)}")

        elif parancs == 2:
            print("Ezek a jelszavaid:")
            print()
            jelszo_betoltese()

        elif parancs == 3:
            futas = False

    except:
        print("Nem jó, próbáld újra!")