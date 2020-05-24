# 1. Pedirpor tecladodos números y decir si son iguales o no.
numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ahora otro número: "))
if numero1 == numero2:
    print("Son iguales")
else:
    print("No son iguales")

# 2. Pedir por teclado 10 números. Mostrar la media de los números positivos, la media de los números negativos y la cantidad de ceros
cantidad = 10
positivos = 0; positivos_suma = 0
negativos = 0; negativos_suma = 0
ceros = 0
print("Ingrese 10 números")
for x in range (cantidad):
    numero = input()
    if numero > str(0):
        positivos_suma += int(numero)
        positivos += 1
    elif numero < str(0):
        negativos_suma += int(numero)
        negativos += 1
    else:
        ceros += 1
print("La media de los números positivos es: ", positivos_suma/positivos, " donde la fórmula es: ", positivos_suma, "/", positivos)
print("La media de los números negativos es: ", negativos_suma/negativos, " donde la fórmula es: ", negativos_suma, "/", negativos)
print("La cantidad de ceros es: ", ceros)

# 3. Escribir un programa que detecte si un número es primo o no. Un número es primo si sólo es divisible por sí mismo y por la unidad
numero= int(input("Ingrese un número: "))
valor= range(2,numero)
contador = 0
for n in valor:
    if numero % n == 0:
        contador +=1
        print("No es primo, divisor", contador, "= ", n)
if contador > 0:
    print("El número no es primo" )
else:
    print("El número es primo")

# 4. Escribir un programa que visualice en pantalla los números pares entre 1 y 25
print("Números pares entre 1 y 25")
for x in range (1, 26):
    if x%2 == 0:
        print(x, end=", ")

#5. Leer un número y mostrar su cuadrado, repetir el proceso hasta que se introduzca un número negativo
contador = 0
while contador >= 0:
    numero = int(input("\nIngrese un número: ")) 
    if numero >= 0:
        numero *=numero
        print("El cuadrado del número ingresado es", numero)
        contador +=1
    else: contador = 0; print("Fin, se introdujo un número negativo"); break

#6. Dadas 6 notas, escribir la cantidad de alumnos aprobados y los no aprobados.(Aprobados mayores a 1)(No aprobados menor o igual a 1).
cantidad = 6
aprobados = 0; aprobados_suma = 0
no_aprobados = 0; no_aprobados_suma = 0
print("Ingrese", cantidad, "notas")
for x in range (cantidad):
    numero = input()
    if numero > str(1):
        aprobados_suma += int(numero)
        aprobados += 1
    elif numero <= str(1):
        no_aprobados_suma += int(numero)
        no_aprobados += 1
print("Aprobados: ", aprobados)
print("Reprobados: ", no_aprobados)