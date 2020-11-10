from tkinter import *
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

def operacions(voltaje, Res1, Res2, ops, conteo):
    global impserie, auxi, add, Vser, operser, sumares, lbimptser, posres, Vimp

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

