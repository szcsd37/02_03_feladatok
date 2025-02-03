""""3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! A program tartalmazza a függvény hívását is!
"""

def harommal_oszthatok(szamok):
    db = 0
    for szam in szamok:
        if szam % 3 == 0:
            db += 1
    return db 

""""
3.2 Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! (Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!)
"""

szamok = []

while True:
    szam = int(input("Adj meg egy számot: "))
    if szam < 0:
        break
    szamok.append(szam)

print(harommal_oszthatok(szamok))