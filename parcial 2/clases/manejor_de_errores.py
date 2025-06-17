
def ingresar_entero() -> int:
    """Pide un entero, lo valida y devuelve un entero
        si falla, lo vuelve a pedir
    Returns:
        int : entero
    """
    while True:
        print("ingrese su edad: ")
        try:
            edad = int(input())
            break
        except:
            print("No ingresaste un entero!")

    return edad

edad = ingresar_entero()
print(f"la edad ingresada por el usuario es: {edad}")
print(type(edad))

# Archivos GUIA DE EJERCICIOS Nº 7
# 1. Se quiere hacer un programa para pedirle al usuario que ingrese un número entero, y en caso de que el
# valor ingresado no sea un número entero, mostrarle un mensaje apropiado.
# a. Realizarlo utilizando isnumeric(). ¿Qué limitaciones encuentra?
# b. Realizarlo utilizando try/ except.
# 2. Crear una función, utilizando el punto anterior, que le pida al usuario un número entero. Utilizarla para
# calcular el producto entre dos números enteros ingresados.
# 3. Se quiere hacer un programa que le solicite al usuario un número divisor y un dividendo, y calcule el
# cociente entre ellos.
# AYUDA: Considerar que el usuario podría brindar un valor no numérico o un divisor nulo.
# 4. Crear un programa para abrir un archivo llamado “file.txt” en modo lectura y en caso de que este
# archivo no exista, mostrar el mensaje “No se pudo encontrar el archivo file.txt”.
# 5. Crear una función cuyos parámetros sean una lista y un índice de posición para mostrar el valor de la
# lista en esa ubicación.
# a. ¿Qué ocurre si ingreso un índice que se encuentra fuera del rango?
# b. Si el valor del índice ingresado se encuentra dentro del rango, mostrar el valor. En caso
# contrario, mostrar un mensaje apropiado para dicho error.
# 6. Para jugar al chinchón con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
# tres o cuatro. Crear una función que pida al usuario informar el número de jugadores, considerando
# que este puede ingresar:
# ● un valor no válido, por ejemplo, una palabra.
# ● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
# ● un valor mayor a 4, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 4
# jugadores."
# ● un valor válido, en cuyo caso, mostrarlo.
# 7. Para jugar al truco con un único mazo de cartas españolas, el número de jugadores puede ser: dos,
# cuatro o seis. Crear una función que pida al usuario informar el número de jugadores, considerando
# que este puede ingresar:
# ● un valor no válido, por ejemplo, una palabra.
# ● un valor menor a 2, en en cuyo caso, mostrar el mensaje "Debe haber al menos 2 jugadores."
# ● un valor mayor a 6, en cuyo caso, mostrar el mensaje "Se puede jugar con un máximo de 6
# jugadores.".
# ● un valor impar, como 3 y 5, en cuyo caso, mostrar el mensaje "Debe haber un número par de
# jugadores.".
# ● un valor válido, en cuyo caso, mostrarlo.
# 2
# Archivos GUIA DE EJERCICIOS Nº 7
# 8. El kiosko de la facultad quiere automatizar un letrero que tome datos de un programa y le cobre al
# estudiante.
# Se tienen dos diccionarios, uno con un código y el producto, y otro con el código y el precio de cada
# producto.
# Ejemplo:
# opciones = {
# 1: "hamburguesas",
# 2: "milanesas",
# 3: "gaseosa",
# 4: "alfajor",
# 5: "papas fritas",
# 6: "agua"
# }
# valores = {
# 1:1000,
# 2:1500,
# 3:500,
# 4:300,
# 5:600,
# 6:350
# }
# Se quiere hacer un programa que muestre la información de la siguiente forma en la pantalla:
# 1: hamburguesas -> 1000
# 2: milanesas -> 1500
# 3: gaseosa -> 500
# 4: alfajor -> 300
# 5: papas fritas -> 600
# 6: agua -> 350
# Y le pida al usuario una opción y una cantidad. Luego, debe imprimir el total a pagar.
# Se debe considerar que el usuario podría ingresar una opción que no está en el diccionario, o ingresar
# una opción que no sea un número. El usuario debe en esos casos imprimir un mensaje de error que sea
# descriptivo y volver a pedirle al usuario que ingrese una opcion