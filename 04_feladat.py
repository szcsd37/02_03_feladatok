""""4. Feladat
Írj egy programot, amelyben van egy 'kerulet' nevű függvény, amely az egyetlen kötelező paramétere mellett fogadhat több paramétert is! Az opcionális paraméterek száma alapján döntse el milyen síkidomról van szó, és számolja ki a kerületét (0 tetszőleges paraméter: négyzet, 1 tetszőleges paraméter: téglalap, 2 tetszőleges paraméter: háromszőg, 3 vagy több tetszőleges paraméter: sokszög)!

A program tartalmazzon mindegyik síkidom típusra egy-egy függvényhívást!"""


def kerulet(*args):
    if len(args) == 0:
        return 0
    elif len(args) == 1:
        return args[0] * 4
    elif len(args) == 2:
        return args[0] * 2 + args[1] * 2
    else:
        return sum(args)


print(kerulet(1, 3, 6, 14, 15))