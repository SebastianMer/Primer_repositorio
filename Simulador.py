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
imparalelo = 2
auxip = 0
addp = []
Ipar = []
sumatotalpar = 0
operapar = 0

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
    global auxip, imparalelo, sumatotalpar, operapar

    auxip = conteop
    conteop = 0
    sumatotalpar = int(Rep1) + int(Rep2)
    while conteop < auxip:
        addp.insert(conteop, opp[conteop].get())
        conteop += 1


    operapar = float(voltaje) / float(Rep1)
    Ipar.insert(0, operapar)
    operapar = float(voltaje) / float(Rep2)
    Ipar.insert(1, operapar)
    conteop = 0

    while conteop < auxip:
        operapar = float(voltaje) / float(addp[conteop])
        Ipar.insert(imparalelo, operapar)
        conteop += 1
        imparalelo += 1
    print(str(Ipar))

