from os import system

archivo = open("hello-world\parcial 2\Archivos 2\persona.csv")
personas_crudo = archivo.readlines()
archivo.close()

#print(personas_crudo)
system("cls")
def transformar(persona):
    persona = persona.strip("\n")
    persona = persona.split(";")
    return persona

personas = list(map(transformar, personas_crudo))
print(personas)

suma_edades = 0
for [nombre, edad] in personas:
    suma_edades += int(edad)

print(f" el promedio de edad es {suma_edades / len(personas)}")