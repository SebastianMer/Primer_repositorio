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
# Varibles auxiliares solucion Paralelo
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
def operacions(voltaje, Res1, Res2, ops, conteo):
    global impserie, auxi, add, Vser, operser, sumares, lbimptser, posres, Vimp, a, b, c

    a = len(voltaje)
    b = len(Res1)
    c = len(Res2)

    if a != 0 and b !=0 and c != 0:
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

        Is = float(voltaje) / sumares
        while conteo < auxi:
            operser = float(voltaje) * float(add[conteo]) / sumares
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

            #Valores
            lbimpvalueser.insert(impserie, Label(frame, text=str(Vser[impserie])))
            lbimpvalueser[impserie].config(fg='white', bg='gray8', font=('Roman', 20))
            lbimpvalueser[impserie].pack()
            lbimpvalueser[impserie].place(x=350, y=posres)

            posres += 50
            impserie += 1

        #Corriente
        lbc = Label(frame, text="Todas las resistencias poseen la misma corriente:")
        lbc.config(fg='white', bg='gray8', font=('Roman', 20))
        lbc.pack()
        lbc.place(x=0, y=posres)

        lc = Label(frame, text=str(Is))
        lc.config(fg='white', bg='gray8', font=('Roman', 20))
        lc.pack()
        lc.place(x=350, y=posres+70)

        l = Label(frame, text="Corriente(A)")
        l.config(fg='white', bg='gray8', font=('Roman', 20))
        l.pack()
        l.place(x=180, y=posres+70)

        Resultado.mainloop()

        print(str(Vser))

def operacionp(voltaje, Rep1, Rep2, opp, conteop):
    global auxip, imparalelo, sumatotalpar, operapar, lbimpar, posresp

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
    lv.place(x=180, y=posresp+70)

    lvalue = Label(frame1, text=str(voltaje))
    lvalue.config(fg='white', bg='gray8', font=('Roman', 20))
    lvalue.pack()
    lvalue.place(x=350, y=posresp+70)

    Resultado1.mainloop()

    print(str(Ipar))

