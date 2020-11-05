from tkinter import *


# -----------------------------------------Funciones----------------------------------------------------
def botones():
    b1 = Button(frame, text="Serie", width="15", height='5', command=lambda: serie("serie"))
    b1.config(font=('Bahnschrift', 10))
    b1.pack()
    b1.place(x=290, y=200)
    b2 = Button(frame, text="Paralelo", width="15", height='5',command=lambda: paralelo("paralelo"))
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

        # Titulo de la ventana
        titulo2 = Label(frame2, text='Circuito Serie')
        titulo2.config(fg='white', bg='gray8', font=('Roman', 20))
        titulo2.pack()
        titulo2.place(x=250, y=0)

        # Imagen
        cserie0 = PhotoImage(file='Serie_0.gif')
        lb = Label(frame2, imag=cserie0)
        lb.pack()
        lb.place(x=180,y=100)

        ventana2.mainloop()

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
        lb.place(x=180,y=100)

        ventana3.mainloop()
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
