"""""
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!

"""

def osszegzo(szamok):
    osszeg = 0
    for szam in szamok:
        osszeg += szam
    return osszeg

print(osszegzo([1, 2, 3, 4, 5]))