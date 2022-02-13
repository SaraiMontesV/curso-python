from datetime import date

# Un programa Python

sum = 1 + 2
print('Sum:', sum)

# La función print()
print('¡Hola desde la consola!')

# Variables
sum = 1 + 2  # 3
product = sum * 2
print('product:', product)

# Tipos de datos
# int, plutón era considerado un planeta pero ya es muy pequeño
planetas_en_el_sistema_solar = 8
distancia_a_alfa_centauri = 4.367  # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11"  # string

# Descubrimos su tipo de dato
type(distancia_a_alfa_centauri)
print('Tipo de dato:', type(distancia_a_alfa_centauri))

# Operadores
left_side = 10
right_side = 5
result = left_side / right_side  # 2
print('result:', result)

# Operadores de asignación
x = 2
print(x)
x += 2
print(x)
x -= 2
print(x)
x *= 2
print(x)
x /= 2
print(x)

# Fechas
date.today()
print(date.today())

# Conversión de tipos de datos
print("Today's date is: " + str(date.today()))

# Recopilar información
# Entrada del usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

# Trabajar con números
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)
print(int(first_number) + int(second_number))
