from os import system


# archivo = open("hello-world\parcial 2\Carpeta archivos\pregunta.txt", "r+")
# lineas = archivo.readlines()
# texto = input("ingrese un texto\n")
# system("cls")
# archivo.write("\n" + texto)
# archivo.close()





# archivo = open("hello-world\parcial 2\Carpeta archivos\pregunta.txt", "r+")
# lineas = archivo.readlines()
# archivo.close()

# for linea in lineas:
#     print(linea, end = "")


# Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que
# se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función recibe
# “poco” y “mucho”, reemplaza “poco” por “mucho” todas las veces que aparezca en el texto.

palabra_reemplazar = input("¿que palabras queres reemplazar?\n")

palabra_nueva = input("¿por cual palabra queres reemplazar?\n")

with open("hello-world/parcial 2/Carpeta archivos/nuevo-archivo.txt") as archivo:
    texto = archivo.readlines()

with open("hello-world/parcial 2/Carpeta archivos/nuevo-archivo.txt", "w") as archivo_escritura:
    for linea in texto:
        archivo_escritura.write(linea.replace(palabra_reemplazar, palabra_nueva))

