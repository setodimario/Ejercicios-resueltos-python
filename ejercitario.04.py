# 1. Escriba un programa que pida un año y que muestre en pantalla si es bisiesto o no
print("»» 1. AÑO BISIESTO")
def anho_bisiesto(anho):
    if anho % 4 == 0:
        if anho % 100 == 0:
            if anho % 400 == 0:
                txt = 'es'
            else:
                txt = 'no es'
        else:
            txt = 'es'
    else:
        txt = 'no es'    
    return txt

anho = int(input('Ingresa un año: '))
print(anho, anho_bisiesto(anho), 'bisiesto')

# 2. Escriba un programa que pida un número entero mayor que cero y que muestre en pantalla sus divisores(agregar los divisores en una lista para luego imprimir en pantalla)
print("»» 2. DIVISORES")
def divisores(numero):
    rango = range(1, numero + 1)
    lista = []
    for divisor in rango:
        if numero % divisor == 0:
            lista.append(divisor)
    return lista
while True:
    numero = int(input("Escriba un número entero mayor que cero: "))
    if not numero > 0:
        print("Debe ser mayor a 0. Intentelo de nuevo")
    else:
        print(f"Los divisores de {numero} son: ",divisores(numero))
        break

# 3. Escribir una función que calcule el factorial de un número
print("»» 3. FACTORIAL")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
while True:
    numero = int(input("Escriba un número entero mayor que cero: "))
    if numero < 0:
        print("No se puede calcular el factorial de un número negativo. Intentelo de nuevo")
    elif numero == 0:
        print(f"El factorial de {numero} es: ", 1)
        break
    else:
        print(f"El factorial de {numero} es: ", factorial(numero))
        break

#4. Los empleados de una fábrica trabajan en dos turnos: diurno y nocturno. Calcular su jornal diario
print("»» 4. CALCULAR JORNAL DIARIO")
selecciones = [] # Se guardará las selecciones una lista
while True:
    print("» TURNOS: [1. Diurno][2. Nocturno]", end=" ")
    turno = int(input("| Selecciona turno: "))
    if turno == 1 or turno == 2:
        selecciones.insert(0, turno)
        break
while True:
    horas_trabajo = int(input("» HORAS TRABAJADAS: "))
    if horas_trabajo <= 24:
        selecciones.insert(1,horas_trabajo)
        break
print("» DIA DE LA SEMANA: ", end="")
dias_semana = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
contador = 0
for element in dias_semana:
    contador +=1
    print("[",contador,".", element, end="]")
while True:
    dia_semana = int(input(" Selecciona día de la semana: "))
    if dia_semana > 0 and dia_semana < 8:
        selecciones.insert(2,dia_semana)
        break
#print(selecciones)
if selecciones[0] == 1: # Diurno
    if selecciones[2] > 1: # Días que no son domingo
        jornal = 5 * selecciones[1]
    else: # Domingo
        jornal = (5+2) * selecciones[1]
else: # Nocturno
    if selecciones[2] > 1: # Días que no son domingo
        jornal = 8 * selecciones[1]
    else: # Domingo
        jornal = (8+3) * selecciones[1]
txt = "Tu jornal diario es {} €"
print(txt.format(jornal))

# 5. Cargar una lista de 20 números enteros. Mostrar la lista en pantalla. Calcular el número mayor y la posición que ocupa dentro de la lista
print("»» 5. LISTADO DE NÚMEROS ENTEROS")
import random
cantidad_lista = 20
lista = []
for n in range(cantidad_lista):
    lista.append(random.randrange(1, 100))
print("El listado de números random es:", lista)
mayor = max(lista); posicion = lista.index(mayor)
txt = "El número mayor de la lista es: {}, y ocupa la posición {} de la lista"
print(txt.format(mayor, posicion))