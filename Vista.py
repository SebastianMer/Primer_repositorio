from tkinter import *
from Simulador import serie

def botones():
    b1 = Button(frame, text="Serie", width="15", height='5', command=lambda:serie("7"))
    b1.config(font=('Bahnschrift', 10))
    b1.pack()
    b1.place(x=200, y=200)
    b2 = Button(frame, text="Paralelo", width="15", height='5')
    b2.config(font=('Bahnschrift', 10))
    b2.pack()
    b2.place(x=200, y=400)
# Creación de ventana
ventana = Tk()
ventana.config(bg='gray')

# Creación del frame
frame = Frame(ventana, width="600", height='1200')
frame.pack()
frame.config(bg='gray8')

# Titulo de la ventana
titulo = Label(frame, text='Simulador circuitos resistivos')
titulo.config(fg='white', bg='gray8', font=('Roman', 20))
titulo.pack()
titulo.place(x=100, y=0)

# Botones
botones()
ventana.mainloop()