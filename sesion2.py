# Sentencias básicas y datos simples GUIA DE EJERCICIOS Nº 2
# Los ejercicios que encontrarán a continuación harán ejercitar temas de comunicación con el usuario, creación
# de funciones y manejo de texto.
# Ingreso de datos
# Imaginá el caso de una máquina expendedora, si los mensajes que se muestran no son claros, si los precios no
# están a la vista, si los números o códigos que identifican a cada producto no están claros, por más que la
# máquina funcione de manera excepcional, las personas no sabrán QUÉ tienen que hacer para usarla.
# Por lo que en cada uno de los siguientes ejercicios intentá ser lo más amigable posible con el usuario,
# mostrándole mensajes acorde a lo que espera de él. Por ejemplo si el programa espera que el usuario ingrese
# un número entero para determinar si es par o impar, sería bueno que se le muestre algo cómo:
# “Por favor, ingrese un número entero para determinar si es par o impar: ”
# Así intentamos evitar posibles errores de los usuarios.

# 1. Crear un programa que le solicite al usuario un entero y lo imprima por pantalla.
# Recordá que podés usar las funciones input (para solicitar información) y print para mostrar
# información.


# numero = input("ingrese un numero")
# print(f"numero ingresado = {numero}")

# 2. Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
# ● la suma de ambos números
# ● la resta de ambos números
# ● la multiplicación de ambos números
# ● la división entera de ambos números
# ● el resto
# Más adelante podríamos crear nuestra propia calculadora :)

# numero = input("ingrese un numero")
# otro_numero = input("ingrese otro numero")
# multiplicacion = numero * otro_numero
# division = numero / otro_numero
# suma = numero + otro_numero
# resta = numero - otro_numero
# resto = numero % otro_numero

# print("Multiplicación: ", multiplicacion)

# print("División: ", division)

# print("Suma: ", suma)

# print("Resta: ", resta)

# print("Resto: ", resto)

# 3. Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un
# mensaje que indique el resultado.
# Para determinar si un número es par o impar, se puede determinar con el uso del operador %, les
# dejamos a ustedes el cómo.

# numero = int(input("ingrese un numero entero"))
# paridad = numero % 2

# if paridad == 0:
#     print(f"el numero {numero} es par")
# else:
#     print(f"el numero {numero} es impar")


# 4. Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía
# el usuario en el año ingresado.

# anio_nacimiento = int(input("ingrese su año de nacimiento"))
# anio_otro = int(input("ingrese un año para verificar la edad"))

# edad_anio = anio_otro - anio_nacimiento

# print(f"su edad en ese año en el año{anio_otro} es: {edad_anio}")

# 5. Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
# Es muy común usar variables para acumular valores.

# def solicitar_entero():
#     entero = int(input("ingrese un entero"))
#     return entero


# numero_uno = solicitar_entero()
# numero_dos = solicitar_entero()
# numero_tres = solicitar_entero()
# numero_cuatro = solicitar_entero()
# numero_cinco = solicitar_entero()

# suma = numero_uno + numero_dos + numero_tres + numero_cuatro + numero_cinco
# promedio = suma / 5

# print(f"el promedio es = {promedio}")



# Funciones con enteros


# 6. Crear una función que reciba un número y muestre el anterior y el siguiente.

# def mostrar_ant_sig(numero: int):
#     anterior = numero - 1
#     siguiente = numero +1
#     print(f"""
# numero anterior = {anterior}
# numero siguiente = {siguiente}
#           """)
    
# numero = int(input("ingrese un numero"))

# mostrar_ant_sig(numero)

# 7. Crear una función que una un string y un entero, ambos dentro de un string.
# def unir_string_con_entero(entero : int, cadena : str):
#     texto = cadena + str(entero)
#     return texto

# entero = 21
# cadena = "Leandro"

# print(unir_string_con_entero(entero, cadena))



# 8.
# a. Crear una función que reciba dos enteros y que retorne (devuelva) el resto de la división.
# b. Crear una función que reciba dos enteros y que retorne (devuelva) el cociente.

# def devolver_resto(primer_entero : int , segundo_entero : int):
#     resto = primer_entero % segundo_entero
#     return resto

# def devolver_cociente(primer_entero : int , segundo_entero : int):
#     cociente = primer_entero / segundo_entero
#     return cociente

# primer_entero = 10
# segundo_entero = 2

# print(f"cociente = {devolver_cociente(primer_entero, segundo_entero)} resto = {devolver_resto(primer_entero,segundo_entero)}")

# # Cadenas

# # 9. Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”.
# # Este proceso se llama concatenar cadenas.

# nombre = input("Ingrese Nombre\n")
# apellido = input("Ingrese Apellido\n")

# print(f"{nombre}, {apellido}")

# 10. Obtener una palabra e imprimir la cantidad de letras.
# palabra = input("ingrese una palabra")

# cantidad_de_letras = len(palabra)

# print(f"la cantidad de letras de {palabra} es {cantidad_de_letras}")

# 11. Obtener una palabra e imprimir los primeros 5 caracteres (pista: slicear la palabra).
# palabra = input("ingrese una palabra")
# palabra_slice = palabra[0:5:2]

# print(palabra_slice)
# 12. Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla (pista: usar una función predefinida
# de Python).

palabra = input("ingrese una palabra")

palabra_sin_a = palabra.replace('a', '')  # función predefinida
print("Palabra sin 'a':", palabra_sin_a)