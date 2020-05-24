# 1. Longitud de cadena
cadena = "Este es un curso de Python"
print("La cadena ", cadena, "tiene una longitud de ", len(cadena.replace(' ', '')))

# 2. Pedir al usuario que escriba su nombre, y saludarlo por su nombre
# 3. Nombre en mayúsucula
nombre = input("Ingrese su nombre: ")
print("Hola ", nombre.upper())

# 4. Mostrar saludo, nombre y edad con la función format()
anho_nacimiento = int(input("Introduce tu año de nacimiento: "))
edad = 2020 - anho_nacimiento
txt = "Hola {}, tienes {} años"
print(txt.format(nombre, int(edad)))

# Rango de 0 a 10
import random
print("Número random es igual a:", random.randrange(0, 10))

# 6. Mostrar función de operadores aritméticos de 2 números
a = random.randrange(1, 10)
b = random.randrange(1, 10)
print("Operaciones aritméticas entre", a, " y ", b)
print("La suma es: ", a + b)
print("La resta es: ", a - b)
print("La división es: ", a / b)
print("La multiplicación es: ", a * b)
print("El resto es: ", a % b)

# 7. Precio de IVA de un producto. IVA 30%
porcentaje_IVA = 30
precio_inicial = int(input("Ingrese precio inicial: "))
iva = precio_inicial * (porcentaje_IVA / 100)
precio_con_iva = precio_inicial + iva
print("IVA del producto: G.{}".format(int(iva)), 
"\nPrecio Inicial: G.{}".format(precio_inicial), 
"\nPrecio Final: G.{}".format(int(precio_con_iva)))

# 8. Calcular perímetro y área a través del radio de un circulo
radio = int(input("Ingrese el radio del círculo: "))
import math
print("El perímetro es:", 2*math.pi*radio, "cm") # Fórmula: 2 x pi x radio
print("El área es:", math.pi*radio*2, "cm2") # Fórmula: pi x radio x 2

# 9. Promedio de 4 notas ingresadas por el usuario
a, b, c, d = int(input("Nota 1: ")), int(input("Nota 2: ")), int(input("Nota 3: ")), int(input("Nota 4: "))
print("El promedio es: ", (a+b+c+d)/4)

# 10. Convertir de centímetros a pulgadas. Una pulgada es igual a 2.54 centímetros
centimetros = int(input("Ingrese centímetro: "))
pulgada = 2.54
print(centimetros, "cm equivale a ", float(centimetros/pulgada), "pulgadas")