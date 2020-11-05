from tkinter import *


# -----------------------------------------Funciones----------------------------------------------------
def botones():
    b1 = Button(frame, text="Serie", width="15", height='5', command=lambda: serie("serie"))
    b1.config(font=('Bahnschrift', 10))
    b1.pack()
    b1.place(x=290, y=200)
    b2 = Button(frame, text="Paralelo", width="15", height='5')
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
        titulo2.place(x=230, y=0)

        # Imagen
        cserie0 = PhotoImage(file='Serie_0.gif')
        lb = Label(frame, imag=cserie0)
        lb.pack()
        lb.place(x=100,y=100)

        ventana2.mainloop()


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
