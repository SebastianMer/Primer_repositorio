"""
Simulador de circuitos resistivos
Integrantes:
Werney Barajas
Santiago Palacios
Sebastián Merchán
"""

# Varibles auxiliares solucion Serie
impserie = 3
auxi = 0
add = []

# Varibles auxiliares solucion Paralelo
imparalelo = 3
auxip = 0
addp = []


def operacions(voltaje, Res1, Res2, ops, conteo):
    global impserie, auxi

    print("Voltaje " + str(voltaje))
    print("1: " + str(Res1))
    print("2: " + str(Res2))
    auxi = conteo
    conteo = 0

    while conteo < auxi:
        add.insert(conteo, ops[conteo].get())
        print(str(impserie) + ": " + str(add[conteo]))
        conteo += 1
        impserie += 1

    impserie = 3
def operacionp(voltaje, Rep1, Rep2, opp, conteop):
    global auxip, imparalelo

    print("Voltaje " + str(voltaje))
    print("1: " + str(Rep1))
    print("2: " + str(Rep2))
    auxip = conteop
    conteop = 0

    while conteop < auxip:
        addp.insert(conteop, opp[conteop].get())
        print(str(imparalelo) + ": " + str(addp[conteop]))
        conteop += 1
        imparalelo += 1
    imparalelo = 3