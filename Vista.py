from tkinter import *
from Simulador import operacions
from Simulador import operacionp

# Vaiables globales
# Posiciones
posts = 150
postp = 150
poses = 153
posep = 153
conteo = 0
conteop = 0

# Variables circuitos serie
lis = []
Pis = []
lser = []
eser = []
ops = []
Rs = ['R3(Ω)', 'R4(Ω)', 'R5(Ω)', 'R6(Ω)', 'R7(Ω)']
Is = ['Serie_1.gif', 'Serie_2.gif', 'Serie_3.gif', 'Serie_4.gif', 'Serie_5.gif']

# Variables circuitos paralelo
lip = []
Pip = []
lpar = []
epar = []
opp = []
Rp = ['R3(Ω)', 'R4(Ω)', 'R5(Ω)', 'R6(Ω)', 'R7(Ω)']
Ip = ['Paralelo_1.gif', 'Paralelo_2.gif', 'Paralelo_3.gif', 'Paralelo_4.gif', 'Paralelo_5.gif']


# -----------------------------------------Funciones----------------------------------------------------
def botones():
    b1 = Button(frame, text="Serie", width="15", height='5', command=lambda: serie("serie"))
    b1.config(font=('Bahnschrift', 10))
    b1.pack()
    b1.place(x=290, y=200)
    b2 = Button(frame, text="Paralelo", width="15", height='5', command=lambda: paralelo("paralelo"))
    b2.config(font=('Bahnschrift', 10))
    b2.pack()
    b2.place(x=290, y=400)


def serie(condicion):
    global conteo, ops

    op = StringVar()
    op2 = StringVar()
    opv = StringVar()
    if condicion == "serie":
        # Ventana hija
        ventana2 = Toplevel()
        ventana2.title("Circuito Serie")
        ventana2.geometry("1200x1200+0+0")
        ventana2.config(bg='gray')

        # Creación del frame
        frame2 = Frame(ventana2, width="1200", height='1200')
        frame2.pack()
        frame2.config(bg='gray8')

        # Titulos
        titulo2 = Label(frame2, text='Circuito Serie')
        titulo2.config(fg='white', bg='gray8', font=('Roman', 20))
        titulo2.pack()
        titulo2.place(x=250, y=0)

        # R1
        ts1 = Label(frame2, text='R1(Ω)')
        ts1.config(fg='white', bg='gray8', font=('Roman', 15))
        ts1.pack()
        ts1.place(x=670, y=50)
        es1 = Entry(frame2, textvariable=op)
        es1.pack()
        es1.place(x=750, y=53)

        # R2
        ts2 = Label(frame2, text='R2(Ω)')
        ts2.config(fg='white', bg='gray8', font=('Roman', 15))
        ts2.pack()
        ts2.place(x=670, y=100)
        es2 = Entry(frame2, textvariable=op2)
        es2.pack()
        es2.place(x=750, y=103)

        # Volataje
        tsv = Label(frame2, text='V1(V)')
        tsv.config(fg='white', bg='gray8', font=('Roman', 15))
        tsv.pack()
        tsv.place(x=900, y=50)
        esv = Entry(frame2, textvariable=opv)
        esv.pack()
        esv.place(x=950, y=53)

        # Imagen
        cserie1 = PhotoImage(file='Serie_0.gif')
        lbs = Label(frame2, imag=cserie1)
        lbs.pack()
        lbs.place(x=0, y=50)

        # Botones
        bs1 = Button(frame2, text="+", width="3", height='1', command=lambda: auxserie("+", frame2))
        bs1.config(font=('Bahnschrift', 10))
        bs1.pack()
        bs1.place(x=0, y=410)
        bs2 = Button(frame2, text="-", width="3", height='1', command=lambda: menosseri("menos", frame2))
        bs2.config(font=('Bahnschrift', 10))
        bs2.pack()
        bs2.place(x=30, y=410)
        bs3 = Button(frame2, text="Resolver", width="7", height='1',
                     command=lambda: operacions(opv.get(), op.get(), op2.get(), ops, conteo))
        bs3.config(font=('Bahnschrift', 10))
        bs3.pack()
        bs3.place(x=60, y=410)

        ventana2.mainloop()


def auxserie(cond, frame2):
    global posts, Rs, poses, conteo, Is, lis, ops, lis, Pis

    if cond == '+' and conteo < 5:
        ops.insert(conteo, StringVar())
        lser.insert(conteo, Label(frame2, text=Rs[conteo]))
        lser[conteo].config(fg='white', bg='gray8', font=('Roman', 15))
        lser[conteo].pack()
        lser[conteo].place(x=670, y=posts)
        eser.insert(conteo, Entry(frame2, textvariable=ops[conteo]))
        eser[conteo].pack()
        eser[conteo].place(x=750, y=poses)

        Pis.insert(conteo, PhotoImage(file=Is[conteo]))
        lis.insert(conteo, Label(frame2, image=Pis[conteo]))
        lis[conteo].pack()
        lis[conteo].place(x=0, y=50)

        posts += 50
        poses += 50
        conteo += 1
        frame2.mainloop()


def menosseri(cod, frame2):
    global conteo, posts, Rs, poses, conteo, Is, lis, ops, lis, Pis

    if cod == 'menos' and conteo > 0:
        conteo -= 1
        lser[conteo].destroy()
        eser[conteo].destroy()

        if conteo == 0:
            Pis.insert(conteo, PhotoImage(file='Serie_0.GIF'))
            lis.insert(conteo, Label(frame2, image=Pis[conteo]))
            lis[conteo].pack()
            lis[conteo].place(x=0, y=50)
        else:
            Pis.insert(conteo, PhotoImage(file=Is[conteo - 1]))
            lis.insert(conteo, Label(frame2, image=Pis[conteo]))
            lis[conteo].pack()
            lis[conteo].place(x=0, y=50)

        posts -= 50
        poses -= 50
        frame2.mainloop()


def paralelo(condicion):
    global opp, conteop
    if condicion == "paralelo":
        ope = StringVar()
        ope2 = StringVar()
        opev = StringVar()
        # Ventana hija 2
        ventana3 = Toplevel()
        ventana3.title("Circuito Paralelo")
        ventana3.geometry("1200x1200+0+0")
        ventana3.config(bg='gray')

        # Creación del frame
        frame3 = Frame(ventana3, width="1200", height='1200')
        frame3.pack()
        frame3.config(bg='gray8')

        # Titulo de la ventana
        titulo3 = Label(frame3, text='Circuito Paralelo')
        titulo3.config(fg='white', bg='gray8', font=('Roman', 20))
        titulo3.pack()
        titulo3.place(x=250, y=0)

        # Imagen
        cparalelo0 = PhotoImage(file='Paralelo_0.gif')
        lb = Label(frame3, imag=cparalelo0)
        lb.pack()
        lb.place(x=0, y=50)

        # R1
        tp1 = Label(frame3, text='R1(Ω)')
        tp1.config(fg='white', bg='gray8', font=('Roman', 15))
        tp1.pack()
        tp1.place(x=450, y=50)
        ep1 = Entry(frame3, textvariable=ope)
        ep1.pack()
        ep1.place(x=505, y=53)

        # R2
        tp2 = Label(frame3, text='R2(Ω)')
        tp2.config(fg='white', bg='gray8', font=('Roman', 15))
        tp2.pack()
        tp2.place(x=450, y=100)
        ep2 = Entry(frame3, textvariable=ope2)
        ep2.pack()
        ep2.place(x=505, y=103)

        # Voltaje
        tpv = Label(frame3, text='V1(V)')
        tpv.config(fg='white', bg='gray8', font=('Roman', 15))
        tpv.pack()
        tpv.place(x=850, y=50)
        epv = Entry(frame3, textvariable=opev)
        epv.pack()
        epv.place(x=900, y=53)

        # Botones
        bp1 = Button(frame3, text="+", width="3", height='1', command=lambda: auxparalelo("+", frame3))
        bp1.config(font=('Bahnschrift', 10))
        bp1.pack()
        bp1.place(x=0, y=405)
        bp2 = Button(frame3, text="-", width="3", height='1', command=lambda: menespar("menos", frame3))
        bp2.config(font=('Bahnschrift', 10))
        bp2.pack()
        bp2.place(x=30, y=405)
        bp3 = Button(frame3, text='Resolver', width='7', height='1',
                     command=lambda: operacionp(opev.get(), ope.get(), ope2.get(), opp, conteop))
        bp3.config(font=('Bahnschrift', 10))
        bp3.pack()
        bp3.place(x=60, y=405)

        ventana3.mainloop()


def auxparalelo(condi, frame3):
    global Rp, posep, postp, conteop, Ip, lip, Pip, epar, opp

    if condi == '+' and conteop < 5:
        opp.insert(conteop, StringVar())
        lpar.insert(conteop, Label(frame3, text=Rp[conteop]))
        lpar[conteop].config(fg='white', bg='gray8', font=('Roman', 15))
        lpar[conteop].pack()
        lpar[conteop].place(x=450, y=postp)
        epar.insert(conteop, Entry(frame3, textvariable=opp[conteop]))
        epar[conteop].pack()
        epar[conteop].place(x=505, y=posep)

        Pip.insert(conteop, PhotoImage(file=Ip[conteop]))
        lip.insert(conteop, Label(frame3, image=Pip[conteop]))
        lip[conteop].pack()
        lip[conteop].place(x=0, y=50)
        postp += 50
        posep += 50
        conteop += 1
        frame3.mainloop()


def menespar(cond, frame3):
    global Rp, posep, postp, conteop, Ip, lip, Pip, epar, opp

    if cond == "menos" and conteop > 0:
        conteop -= 1
        lpar[conteop].destroy()
        epar[conteop].destroy()

        if conteop == 0:
            Pip.insert(conteop, PhotoImage(file='Paralelo_0.GIF'))
            lip.insert(conteop, Label(frame3, image=Pip[conteop]))
            lip[conteop].pack()
            lip[conteop].place(x=0, y=50)
        else:
            Pip.insert(conteop, PhotoImage(file=Ip[conteop - 1]))
            lip.insert(conteop, Label(frame3, image=Pip[conteop]))
            lip[conteop].pack()
            lip[conteop].place(x=0, y=50)

        postp -= 50
        posep -= 50
        frame3.mainloop()


# Creación de ventana principal
ventana = Tk()
ventana.title("Simulador circuitos resistivos")
ventana.geometry("700x700+0+0")
ventana.config(bg='gray')

# Creación del frame
frame = Frame(ventana, width="700", height='700')
frame.pack()
frame.config(bg='gray8')

# Titulo de la ventana
titulo = Label(frame, text='Simulador circuitos resistivos')
titulo.config(fg='white', bg='gray8', font=('Roman', 20))
titulo.pack()
titulo.place(x=180, y=0)

# Botones
botones()
ventana.mainloop()
