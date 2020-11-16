from tkinter import *

"""
Simulador de circuitos resistivos
Integrantes:
Werney Barajas
Santiago Palacios
Sebastián Merchán
"""

a = 0
b = 0
c = 0
# Varibles auxiliares solucion Serie
aaa = 0
impserie = 2
auxi = 0
add = []
Vser = []
operser = 0
sumares = 0
Is = 0
lbimptser = []
lbimpvalueser = []
Vimp = ['Voltaje(V) 1: ', 'Voltaje(V) 2: ', 'Voltaje(V) 3: ', 'Voltaje(V) 4: ',
        'Voltaje(V) 5: ', 'Voltaje(V) 6: ', 'Voltaje(V) 7: ']
posres = 100
entradas = [False, False, False, False, False, False, False]
Res = []
ff = 'vacio'

# Varibles auxiliares solucion Paralelo
a1 = 0
b1 = 0
c1 = 0
imparalelo = 2
auxip = 0
addp = []
Ipar = []
operapar = 0
sumarpar = 0
lbimpar = []
lbimpvaluepar = []
Iimpar = ['Corriente(A) 1: ', 'Corriente(A) 2: ', 'Corriente(A) 3: ', 'Corriente(A) 4: ',
          'Corriente(A) 5: ', 'Corriente(A) 6: ', 'Corriente(A) 7: ']
posresp = 100
Rep = []
bbb = 0
fff = 'Vacio'
entradap = [False, False, False, False, False, False, False]


def operacions(voltaje, Res1, Res2, ops, conteo):
    global impserie, auxi, add, Vser, operser, sumares, lbimptser, posres, Vimp, a, b, c, Res, aaa, entradas, ff, Is

    a = len(voltaje)
    b = len(Res1)
    c = len(Res2)
    Vser = []
    posres = 100
    operser = 0
    sumares = 0
    impserie = 2
    aaa = 0
    entradas = [False, False, False, False, False, False, False]

    if a != 0 and b != 0 and c != 0:

        for i in Res1:
            if i == 'k':
                add.insert(0, float(Res1[0:aaa]) * 1000)
                entradas[0] = True
                sumares = sumares + add[0]
            aaa += 1

        if not entradas[0]:
            add.insert(0, float(Res1))
            sumares = sumares + add[0]
        aaa = 0

        for i in Res2:
            if i == 'k':
                add.insert(1, float(Res2[0:aaa]) * 1000)
                sumares = sumares + add[1]
                entradas[1] = True
            aaa += 1

        if not entradas[1]:
            add.insert(1, float(Res2))
            sumares = sumares + add[1]

        auxi = conteo
        conteo = 0

        while conteo < auxi:
            Res.insert(conteo, ops[conteo].get())
            conteo += 1

        conteo = 0

        while conteo < auxi:
            aaa = 0
            ff = Res[conteo]
            for e in ff:
                if e == 'k':
                    add.insert(conteo + 2, float(ff[0:aaa]) * 1000)
                    entradas[conteo + 2] = True
                aaa += 1
            conteo += 1

        conteo = 0

        while conteo < auxi:
            if not entradas[conteo + 2]:
                add.insert(conteo + 2, float(Res[conteo]))
                sumares = sumares + add[conteo + 2]
            else:
                sumares = sumares + add[conteo + 2]
            conteo += 1

        print(sumares)
        operser = float(voltaje) * float(add[0]) / sumares
        Vser.insert(0, operser)
        operser = float(voltaje) * float(add[1]) / sumares
        Vser.insert(1, operser)
        conteo = 0

        Is = float(voltaje) / sumares
        while conteo < auxi:
            operser = float(voltaje) * float(add[conteo + 2]) / sumares
            Vser.insert(impserie, operser)
            conteo += 1
            impserie += 1

        Resultado = Tk()
        Resultado.title("Resultados circuito serie")
        Resultado.geometry("700x700+0+0")
        Resultado.config(bg='gray')

        # Creación del frame
        frame = Frame(Resultado, width="700", height='700')
        frame.pack()
        frame.config(bg='gray8')

        # Titulo de la ventana
        titulo = Label(frame, text='Resultados circuito serie')
        titulo.config(fg='white', bg='gray8', font=('Roman', 20))
        titulo.pack()
        titulo.place(x=180, y=0)

        # Impresion de resultados

        auxi = impserie
        impserie = 0
        while impserie < auxi:
            # Titulos
            lbimptser.insert(impserie, Label(frame, text=Vimp[impserie]))
            lbimptser[impserie].config(fg='white', bg='gray8', font=('Roman', 20))
            lbimptser[impserie].pack()
            lbimptser[impserie].place(x=180, y=posres)

            # Valores
            lbimpvalueser.insert(impserie, Label(frame, text=str(Vser[impserie])))
            lbimpvalueser[impserie].config(fg='white', bg='gray8', font=('Roman', 20))
            lbimpvalueser[impserie].pack()
            lbimpvalueser[impserie].place(x=350, y=posres)

            posres += 50
            impserie += 1

        # Corriente
        lbc = Label(frame, text="Todas las resistencias poseen la misma corriente:")
        lbc.config(fg='white', bg='gray8', font=('Roman', 20))
        lbc.pack()
        lbc.place(x=0, y=posres)

        lc = Label(frame, text=str(Is))
        lc.config(fg='white', bg='gray8', font=('Roman', 20))
        lc.pack()
        lc.place(x=350, y=posres + 70)

        l = Label(frame, text="Corriente(A)")
        l.config(fg='white', bg='gray8', font=('Roman', 20))
        l.pack()
        l.place(x=180, y=posres + 70)

        Resultado.mainloop()


def operacionp(voltaje, Rep1, Rep2, opp, conteop):
    global auxip, imparalelo, operapar, lbimpar, posresp, a1, b1, c1, fff, bbb, Rep, entradap

    auxip = conteop
    conteop = 0

    a1 = len(voltaje)
    b1 = len(Rep1)
    c1 = len(Rep2)
    imparalelo = 2
    operapar = 0
    posresp = 100
    bbb = 0
    entradap = [False, False, False, False, False, False, False]

    if a1 != 0 and b1 != 0 and c1 != 0:

        for i in Rep1:
            if i == 'k':
                addp.insert(0, float(Rep1[0:bbb]) * 1000)
                entradap[0] = True
            bbb += 1

        if not entradap[0]:
            addp.insert(0, float(Rep1))

        bbb = 0

        for i in Rep2:
            if i == 'k':
                addp.insert(1, float(Rep2[0:bbb]) * 1000)
                entradap[1] = True
            bbb += 1

        if not entradap[1]:
            addp.insert(1, float(Rep2))

        while conteop < auxip:
            Rep.insert(conteop, opp[conteop].get())
            conteop += 1

        conteop = 0

        while conteop < auxip:
            fff = Rep[conteop]
            bbb = 0
            for i in fff:
                if i == 'k':
                    addp.insert(conteop + 2, float(fff[0:bbb]) * 1000)
                    entradap[conteop + 2] = True
                bbb += 1

            conteop += 1

        conteop = 0

        while conteop < auxip:
            if not entradap[conteop + 2]:
                addp.insert(conteop + 2, float(Rep[conteop]))
            conteop += 1

        operapar = float(voltaje) / float(addp[0])
        Ipar.insert(0, operapar)
        operapar = float(voltaje) / float(addp[1])
        Ipar.insert(1, operapar)

        conteop = 0

        while conteop < auxip:
            operapar = float(voltaje) / float(addp[conteop + 2])
            Ipar.insert(imparalelo, operapar)
            conteop += 1
            imparalelo += 1

        # Impresion de resultados Paralelo
        Resultado1 = Tk()
        Resultado1.title("Resultados circuito serie")
        Resultado1.geometry("700x700+0+0")
        Resultado1.config(bg='gray')

        # Creación del frame
        frame1 = Frame(Resultado1, width="700", height='700')
        frame1.pack()
        frame1.config(bg='gray8')

        # Titulo de la ventana
        titulo = Label(frame1, text='Resultados circuito paralelo')
        titulo.config(fg='white', bg='gray8', font=('Roman', 20))
        titulo.pack()
        titulo.place(x=180, y=0)

        # Imprimir en ventana

        auxip = imparalelo
        imparalelo = 0

        while imparalelo < auxip:
            lbimpar.insert(imparalelo, Label(frame1, text=Iimpar[imparalelo]))
            lbimpar[imparalelo].config(fg='white', bg='gray8', font=('Roman', 20))
            lbimpar[imparalelo].pack()
            lbimpar[imparalelo].place(x=180, y=posresp)

            # Valores
            lbimpvaluepar.insert(imparalelo, Label(frame1, text=str(Ipar[imparalelo])))
            lbimpvaluepar[imparalelo].config(fg='white', bg='gray8', font=('Roman', 20))
            lbimpvaluepar[imparalelo].pack()
            lbimpvaluepar[imparalelo].place(x=350, y=posresp)

            conteop += 1
            imparalelo += 1
            posresp += 50

        lbe = Label(frame1, text="Todas las resistencias poseen el mismo voltaje: ")
        lbe.config(fg='white', bg='gray8', font=('Roman', 20))
        lbe.pack()
        lbe.place(x=0, y=posresp)

        lv = Label(frame1, text="Voltaje(V): ")
        lv.config(fg='white', bg='gray8', font=('Roman', 20))
        lv.pack()
        lv.place(x=180, y=posresp + 70)

        lvalue = Label(frame1, text=str(voltaje))
        lvalue.config(fg='white', bg='gray8', font=('Roman', 20))
        lvalue.pack()
        lvalue.place(x=350, y=posresp + 70)

        Resultado1.mainloop()
