from tkinter import *

# Vaiables globales
# Posiciones
posts = 150
postp = 150
poses = 153
posep = 153
conteo=0
conteop=0
Rs = ['R3(Ω)', 'R4(Ω)', 'R5(Ω)', 'R6(Ω)', 'R7(Ω)']
Rp = ['R3(Ω)', 'R4(Ω)', 'R5(Ω)', 'R6(Ω)', 'R7(Ω)']

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
    if condicion == "serie":
        # Ventana hija
        ventana2 = Toplevel()
        ventana2.title("Circuito Serie")
        ventana2.geometry("700x700+0+0")
        ventana2.config(bg='gray')

        # Creación del frame
        frame2 = Frame(ventana2, width="700", height='700')
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
        ts1.place(x=350, y=50)
        es1 = Entry(frame2)
        es1.pack()
        es1.place(x=410, y=53)

        # R2
        ts2 = Label(frame2, text='R2(Ω)')
        ts2.config(fg='white', bg='gray8', font=('Roman', 15))
        ts2.pack()
        ts2.place(x=350, y=100)
        es2 = Entry(frame2)
        es2.pack()
        es2.place(x=410, y=103)

        # Imagen
        cserie0 = PhotoImage(file='Serie_0.gif')
        lb = Label(frame2, imag=cserie0)
        lb.pack()
        lb.place(x=0, y=50)

        # Botones
        bs1 = Button(frame2, text="+", width="5", height='5', command=lambda: auxserie("+", frame2))
        bs1.config(font=('Bahnschrift', 10))
        bs1.pack()
        bs1.place(x=0, y=350)
        bs2 = Button(frame2, text="-", width="5", height='5')
        bs2.config(font=('Bahnschrift', 10))
        bs2.pack()
        bs2.place(x=45, y=350)

        ventana2.mainloop()


def auxserie(cond, frame2):
    global posts, Rs, poses, conteo
    if cond == '+' and conteo<5:
        ts = Label(frame2, text=Rs[conteo])
        ts.config(fg='white', bg='gray8', font=('Roman', 15))
        ts.pack()
        ts.place(x=350, y=posts)
        es = Entry(frame2)
        es.pack()
        es.place(x=410, y=poses)
        posts+=50
        poses+=50
        conteo+=1


def paralelo(condicion):
    if condicion == "paralelo":
        # Ventana hija 2
        ventana3 = Toplevel()
        ventana3.title("Circuito Paralelo")
        ventana3.geometry("700x700+0+0")
        ventana3.config(bg='gray')

        # Creación del frame
        frame3 = Frame(ventana3, width="700", height='700')
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

        # Botones
        bp1 = Button(frame3, text="+", width="5", height='5', command=lambda: auxparalelo("+", frame3))
        bp1.config(font=('Bahnschrift', 10))
        bp1.pack()
        bp1.place(x=0, y=350)
        bp2 = Button(frame3, text="-", width="5", height='5')
        bp2.config(font=('Bahnschrift', 10))
        bp2.pack()
        bp2.place(x=45, y=350)

        # R1
        tp1 = Label(frame3, text='R1(Ω)')
        tp1.config(fg='white', bg='gray8', font=('Roman', 15))
        tp1.pack()
        tp1.place(x=350, y=50)
        ep1 = Entry(frame3)
        ep1.pack()
        ep1.place(x=410, y=53)

        # R2
        tp2 = Label(frame3, text='R2(Ω)')
        tp2.config(fg='white', bg='gray8', font=('Roman', 15))
        tp2.pack()
        tp2.place(x=350, y=100)
        ep2 = Entry(frame3)
        ep2.pack()
        ep2.place(x=410, y=103)
        ventana3.mainloop()

def auxparalelo(condi, frame3):
    global Rp, posep, postp, conteop
    if condi == '+' and conteop<5:
        ts = Label(frame3, text=Rp[conteop])
        ts.config(fg='white', bg='gray8', font=('Roman', 15))
        ts.pack()
        ts.place(x=350, y=postp)
        es = Entry(frame3)
        es.pack()
        es.place(x=410, y=posep)
        postp+=50
        posep+=50
        conteop+=1

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


