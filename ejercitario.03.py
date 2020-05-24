# 1. Escribir un programa que simule una calculadora y que contenga las siguientes funciones.
def Calculadora():
    print("<< CALCULADORA >>\nQue operación desea realizar?")
    print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir")
    opcion = int(input("Selecciona una de las opciones: "))
    while (opcion >= 0 and opcion < 5):
        x = int(input("Ingrese primer número: "))
        y = int(input("Ingrese segundo número: "))
        if (opcion==1):
            print ("La suma es:",x, "+", y, "=", x+y)
            opcion = int(input("Selecciona una de las opciones: "))
        elif(opcion==2):
            print ("La resta es:",x, "-", y, "=", x-y)
            opcion = int(input("Selecciona una de las opciones: "))
        elif(opcion==3):
            print ("La multiplicación es:",x, "*", y, "=", x*y)
            opcion = int(input("Selecciona una de las opciones: "))
        elif(opcion==4):
            try:
              print ("La división es:",x, "/", y, "=", x/y)
              opcion = int(input("Selecciona una de las opciones: "))
            except ZeroDivisionError:
              print ("No se permite división entre cero")
              opcion = int(input("Selecciona una de las opciones: "))
    else: print("Gracias por usar la calculadora!!!\n")

Calculadora()

# 2. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua, Castellano, Geología, Educación Física, etc.) en una lista.
cantidad_asignatura = int(input("Cuantas materias deseas agregar?: "))
listaAsignatura = []
for x in range (cantidad_asignatura):
    #- Las materias deben insertarse por el método append o insert mediante un input. 
    listaAsignatura.insert(x, str(input("Nombre de materia: ")))
print("Las asignaturas agregadas son: ",listaAsignatura)
#-Demostrar el método pop() o remove() eliminando un elemento de la lista.
listaAsignatura.pop()
print("Se ha eliminado el último ítem, la lista queda de la siguiente manera ", listaAsignatura)
#- Recorrer la lista y mostrar en pantalla todos los elementos de la lista (“Asignatura:”,listaAsignatura[i]) por cada asignatura de la lista
print("Listado de asignaturas")
for i in listaAsignatura:
    print("Asignatura:", i)