"""
Simulador de circuitos resistivos
Integrantes:
Werney Barajas
Santiago Palacios
Sebastián Merchán
"""

# Varibles auxiliares solucion Serie
impserie = 2
auxi = 0
add = []
Vser = []
operser = 0
sumares = 0

# Varibles auxiliares solucion Paralelo
imparalelo = 2
auxip = 0
addp = []
Ipar = []
operapar = 0

def operacions(voltaje, Res1, Res2, ops, conteo):
    global impserie, auxi, add, Vser, operser, sumares

    auxi = conteo
    conteo = 0

    sumares = float(Res1) + float(Res2)
    while conteo < auxi:
        add.insert(conteo, ops[conteo].get())
        sumares = sumares + float(add[conteo])
        conteo += 1

    operser = float(voltaje) * float(Res1) / sumares
    Vser.insert(0, operser)
    operser = float(voltaje) * float(Res2) / sumares
    Vser.insert(1, operser)
    conteo = 0

    while conteo < auxi:
        operser = float(voltaje) * float(add[conteo]) / sumares
        Vser.insert(impserie, operser)
        conteo += 1
        impserie += 1

    print(str(Vser))

def operacionp(voltaje, Rep1, Rep2, opp, conteop):
    global auxip, imparalelo, sumatotalpar, operapar

    auxip = conteop
    conteop = 0
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

