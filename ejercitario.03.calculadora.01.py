'''Escribir un programa que simule una calculadora y que contenga las siguientes funciones.
1º) Muestre un menú con 5 opciones:
1. Sumar dos números. ( Función Suma)
2. Restar dos números. (Función Resta)
3. Multiplicar dos números. (Función Multiplicación)
4. Dividir dos números.(Función División)
5. Salir.
'''
from tkinter import *
# Definición de ventana
vtn = Tk()
vtn.title("Calculadora")
vtn.geometry("235x150")
vtn.configure(background="black")
# Funciones
def Suma():
    Suma = int(txt1.get())+int(txt2.get())
    return resultado.set(Suma)
def Resta():
    Resta = int(txt1.get())-int(txt2.get())
    return resultado.set(Resta)
def Multi():
    Multi = int(txt1.get())*int(txt2.get())
    return resultado.set(Multi)
def Divi():
    Divi = int(txt1.get())/int(txt2.get())
    return resultado.set(Divi)
def Cerrar():
    vtn.destroy
resultado = StringVar()

# Se crea label e input para el númer 1
lbl1 = Label(vtn,text="Primer número",bg="black",fg="white")
lbl1.grid(row=1,column=1) # Se dibuja
txt1 = Entry(vtn) # Entrada 1
txt1.grid(row=1,column=2) # Se dibuja
# Se crea label e input para el número 2
lbl2 = Label(vtn,text="Segundo número",bg="black",fg="white")
lbl2.grid(row=2,column=1) # Se dibuja
txt2 = Entry(vtn) # Entrada 1
txt2.grid(row=2,column=2) # Se dibuja

# Botones
btnSuma = Button(vtn,text="+",bg="yellow",fg="black",width=11,command=Suma)
btnSuma.grid(row=3,column=1)
btnResta = Button(vtn,text="-",bg="yellow",fg="black",width=11,command=Resta)
btnResta.grid(row=3,column=2)
btnMulti = Button(vtn,text="*",bg="yellow",fg="black",width=11,command=Multi)
btnMulti.grid(row=4,column=1)
btnDivi = Button(vtn,text="/",bg="yellow",fg="black",width=11,command=Divi)
btnDivi.grid(row=4,column=2)
# Cerrar
btnCerrar = Button(vtn,text="Cerrar",bg="red",fg="white",width=30,command=Cerrar)
btnCerrar.grid(row=5,column=1,columnspan=2)
# Mostrar resultado
lblRes = Label(vtn,bg="white",width=30,textvariable=resultado)
lblRes.grid(row=6,column=1,columnspan=2)

vtn.mainloop()