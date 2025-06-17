# Diccionarios GUIA DE EJERCICIOS Nº 5
# 1. En una escuela se quiere tener un sistema para guardar la información de sus estudiantes para tener
# mejor organizado sus datos.
# a. Crear un diccionario que sirve para representar a una persona en este contexto, pensar en las
# características que se consideren más relevantes para identificar a una persona (su nombre,
# DNI, edad, etc).
    # b. Agregar al diccionario creado, un campo que sea otro diccionario y sirva para guardar el curso
    #   del estudiante y sus características (año, división, orientación, etc).
    # c. Teniendo una lista de diccionarios de estudiantes, buscar en la lista la persona con mayor edad
    # e imprimirla por pantalla.

# estudiante = {
#     "nombre": "Juan Pérez",
#     "dni": "40123456",
#     "edad": 17,
#     "direccion": "Calle Falsa 123",
#     "telefono": "555-1234",
#     "email": "juan.perez@email.com"
# }

# estudiante["curso"] = {
#     "año": 3,
#     "division": "A",
#     "orientacion": "Ciencias Sociales",
#     "turno": "Mañana",
#     "aula": 15
# }

# estudiantes = [
#     {
#         "nombre": "Juan Pérez",
#         "edad": 17,
#         "curso": {"año": 3, "division": "A"}
#     },
#     {
#         "nombre": "María Gómez",
#         "edad": 18,
#         "curso": {"año": 5, "division": "B"}
#     },
#     {
#         "nombre": "Carlos López",
#         "edad": 16,
#         "curso": {"año": 2, "division": "C"}
#     }
# ]
# first = True

# for estudiante in estudiantes:
#     if first or estudiante["edad"] > mayor["edad"]:
#         mayor = estudiante
#         first = False

# print(f"El o la estudiante mayor es: {mayor["nombre"]} y su edad es {mayor["edad"]}")

# 2. En un vivero se guardan las plantas en una lista de diccionario con la siguiente información: especie, si
# necesita luz solar o no, y el precio. (OBSERVACIÓN: ¿Qué tipo de dato nos permitía guardar si algo es
# verdad o no?). Ahora se necesita un sistema que guarde las plantas a medida que van llegando. Se pide
# hacer una función que reciba la lista de diccionarios de plantas, y los datos de la planta nueva y agregue
# esa planta a la lista de diccionarios.
# plantas_vivero = [
#     {"especie": "Rosa", "necesita_luz_solar": True, "precio": 250.50},
#     {"especie": "Helecho", "necesita_luz_solar": False, "precio": 180.75}
# ]


# def obtener_planta(lista_plantas : list):
#     diccionario_planta = {
#         "especie" : "",
#         "luz solar" : False ,
#         "precio" : 0,
#     }
    
#     especie = input("ingrese especie de planta")
#     diccionario_planta["especie"] = especie

#     while True:
#         luz_solar = input("ingrese si necesita luz solar si/no")
#         if luz_solar == "si":
#             luz_solar = True
#             break
#         elif luz_solar == "no":
#             luz_solar = False
#             break
#         else:
#             print("ingrese si necesita luz solar [SI/NO] ")
#             continue

#     diccionario_planta["luz solar"] = luz_solar

#     diccionario_planta["precio"] = float(input("ingrese el precio de la planta"))

#     lista_plantas.append(diccionario_planta)
#     return lista_plantas

# obtener_planta(plantas_vivero)


# print((plantas_vivero))

# 3. Se representa un ticket de supermercado como una lista de diccionarios, donde cada diccionario tiene
# la siguiente información:
# ● Nombre del producto
# ● Precio por unidad
# ● Cantidad
# Se pide hacer una función que reciba el ticket y devuelva el monto total a pagar.

# ticket = [
#     {"nombre": "Leche", "precio": 120.50, "cantidad": 2},
#     {"nombre": "Pan", "precio": 80.00, "cantidad": 3},
#     {"nombre": "Manzanas", "precio": 95.75, "cantidad": 1.5}  # Cantidad puede ser decimal para productos vendidos por peso
# ]

# def cobrar_monto(ticket : list):
#     monto_total = 0
#     for producto in ticket:
#         precio_producto = producto["precio"] * producto["cantidad"]
#         monto_total += precio_producto
    
#     return monto_total

# print(f"el precio total es {cobrar_monto(ticket)}")



# 4. Sol tiene una lista de diccionarios donde guarda todas las películas que vió. La información que tiene
# para cada una es: el nombre de la serie, año en que salió, y la puntuación que le puso del 1 al 10. Hace
# mucho que quiere que Tomás empiece a ver las películas que ella considera que son las mejores que
# vio.
# Hacer una función que reciba el diccionario de las películas que vió Sol, y que devuelva una nueva lista
# de diccionarios donde sólo estén las películas que tienen puntaje mayor a 7.

# peliculas_sol = [
#     {"nombre": "El Padrino", "año": 1972, "puntuacion": 10},
#     {"nombre": "Interestelar", "año": 2014, "puntuacion": 4},
#     {"nombre": "Avatar", "año": 2009, "puntuacion": 7},
#     {"nombre": "Titanic", "año": 1997, "puntuacion": 8},
#     {"nombre": "Transformers", "año": 2007, "puntuacion": 5}
# ]

# def filtrar_aprobados(lista_pelis : list):
#     lista_aprobados = []
#     for pelicula in lista_pelis:
#         if pelicula["puntuacion"] > 7:
#             lista_aprobados.append(pelicula)
#     return lista_aprobados

# lista_pelis = filtrar_aprobados(peliculas_sol)

# print(lista_pelis)

# 5. Un profesor guarda las notas del primer parcial de sus alumnos en una lista de diccionarios que guarda
# la siguiente información:
# ● Nombre
# ● Apellido
# ● Intento
# ● Nota
# Donde ”intento” es la instancia que está rindiendo, 1 si es la primera vez que rinde el parcial, 2 si es el
# primer recuperatorio y 3 si es el segundo recuperatorio.
# Se pide hacer una función que, dado esta lista de diccionarios, devuelva el promedio de las notas en la
# primera oportunidad que rindieron los alumnos.
# ¿Cómo harían para generalizar la función y que el intento sea parametrizable? Es decir, que no
# solamente sirve para el intento 1, sino que también pueda servir para los demás.

# Datos de ejemplo
# alumnos = [
#     {"nombre": "Juan", "apellido": "Pérez", "intento": 1, "nota": 8},
#     {"nombre": "María", "apellido": "Gómez", "intento": 1, "nota": 6},
#     {"nombre": "Carlos", "apellido": "López", "intento": 2, "nota": 4},
#     {"nombre": "Ana", "apellido": "Martínez", "intento": 1, "nota": 9},
#     {"nombre": "Pedro", "apellido": "Sánchez", "intento": 3, "nota": 7}
# ]

# def promediar_evaluaciones(alumnos : list, intento = 3):
#     suma_notas = 0
#     contador = 0
#     for alumno in alumnos:
#         if alumno["intento"] == intento:
#             suma_notas += alumno["nota"]
#             contador += 1
#     promedio = suma_notas / contador
#     return promedio

# print(f"el promedio de notas es {promediar_evaluaciones(alumnos)}")

# 6. En una fábrica, se hace un chequeo de calidad a los productos antes de cada entrega. El resultado del
# chequeo de la entrega se guarda en una lista de diccionarios, donde cada diccionario tiene la siguiente
# información de cada producto:
# ● Código del producto
# ● Fecha de vencimiento
# ● Si pasó el chequeo de calidad o no
# Se pide hacer una función que reciba esta lista de diccionarios y elimine todos los productos que no
# pasaron el chequeo de calidad. Devolver en una tupla el diccionario con los elementos eliminados y la
# cantidad de elementos que quedaron en el diccionario.
# Dado que la tupla es inmutable y nosotros no podemos ir agregando elementos a una tupla, ¿En qué
# momento deberíamos crear la tupla?

def mostrar_unidad(lista : list):
    for unidad in lista:
        print(f"{unidad}")

# productos = [
#     {"codigo": "A001", "fecha_vencimiento": "2023-12-31", "paso_calidad": True},
#     {"codigo": "A002", "fecha_vencimiento": "2024-01-15", "paso_calidad": False},
#     {"codigo": "A003", "fecha_vencimiento": "2023-11-30", "paso_calidad": True},
#     {"codigo": "A004", "fecha_vencimiento": "2024-02-28", "paso_calidad": False},
#     {"codigo": "A005", "fecha_vencimiento": "2023-10-31", "paso_calidad": True}
# ]

# def filtrar_lista(lista : list):
#     lista_eliminados = []
#     for producto in lista:
#         if producto["paso_calidad"] == False:
#             lista_eliminados.append(producto)
#             lista.remove(producto)
#     tupla_eliminados = tuple(lista_eliminados)
#     return tupla_eliminados

# tupla_eliminados = filtrar_lista(productos)

# mostrar_unidad(tupla_eliminados)
# 7. Se quiere guardar la información de un grupo de maratonistas. Se necesita guardar su nombre, DNI, y
# todas las maratones que corrió, de la cual a su vez se quiere tener el nombre de cada una, el año, el
# puesto en que salió el maratonista, y el tiempo que tardó en terminarla.
# a. Crear el diccionario que represente esta situación.
# AYUDA: Queremos guardar muchos maratonistas, y a su vez, muchas maratones para cada
# maratonista, entonces ¿Qué tipo de dato debería ser el campo que guarda todas las
# maratones? ¿Y qué tipo de dato es la maratón en sí?
#     b. Teniendo una lista de diccionarios de maratonistas, ordenarlos alfabéticamente.
#     c. Ordenar las maratones de cada maratonista según el tiempo que tardó en completar cada una de forma ascendente

maratonistas = [
    {
        "nombre": "Carlos López",
        "dni": "30123456",
        "maratones": [
            {
                "nombre": "Maratón de Buenos Aires",
                "año": 2022,
                "puesto": 15,
                "tiempo": "3:45:22"
            },
            {
                "nombre": "Maratón de Nueva York",
                "año": 2021,
                "puesto": 42,
                "tiempo": "4:12:10"
            }
        ]
    },
    {
        "nombre": "Ana Martínez",
        "dni": "28987654",
        "maratones": [
            {
                "nombre": "Maratón de Berlín",
                "año": 2023,
                "puesto": 8,
                "tiempo": "3:30:05"
            },
            {
                "nombre": "Maratón de Boston",
                "año": 2022,
                "puesto": 12,
                "tiempo": "3:28:17"
            }
        ]
    },
    {
        "nombre": "Luisa Fernández",
        "dni": "35123456",
        "maratones": [
            {
                "nombre": "Maratón de Chicago",
                "año": 2023,
                "puesto": 5,
                "tiempo": "2:58:43"
            },
            {
                "nombre": "Maratón de Tokio",
                "año": 2022,
                "puesto": 9,
                "tiempo": "3:05:22"
            },
            {
                "nombre": "Maratón de Londres",
                "año": 2021,
                "puesto": 15,
                "tiempo": "3:12:39"
            }
        ]
    },
    {
        "nombre": "Jorge Rodríguez",
        "dni": "33456789",
        "maratones": [
            {
                "nombre": "Maratón de Madrid",
                "año": 2023,
                "puesto": 21,
                "tiempo": "3:40:15"
            }
        ]
    },
    {
        "nombre": "María González",
        "dni": "29876543",
        "maratones": [
            {
                "nombre": "Maratón de París",
                "año": 2022,
                "puesto": 3,
                "tiempo": "2:55:10"
            },
            {
                "nombre": "Maratón de Berlín",
                "año": 2023,
                "puesto": 7,
                "tiempo": "2:57:45"
            },
            {
                "nombre": "Maratón de Boston",
                "año": 2021,
                "puesto": 10,
                "tiempo": "3:01:22"
            }
        ]
    }
]

def ordenar_alfabeticamente(lista_nombres):
    n = len(lista_nombres)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_nombres[j]["nombre"] > lista_nombres[j+1]["nombre"]:
                # Intercambiar elementos
                lista_nombres[j] = lista_nombres[j+1]
                lista_nombres[j+1] =  lista_nombres[j]
                
    
        
    

ordenar_alfabeticamente(maratonistas)
print(maratonistas)


        
# first = True

# for estudiante in estudiantes:
#     if first or estudiante["edad"] > mayor["edad"]:
#         mayor = estudiante
#         first = False