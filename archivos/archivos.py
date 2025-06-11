# Archivos GUIA DE EJERCICIOS Nº 6
# 1. Se tiene un archivo con la pregunta “¿Cómo estás hoy?” llamado pregunta.txt. Se pide leerlo y mostrar
# la pregunta por pantalla para luego pedirle al usuario que ingrese una respuesta. Después, guardar la respuesta
# dada por el usuario en el archivo.
# Por ejemplo, se tiene el archivo pregunta.txt que originalmente tiene:
# ¿Cómo estás hoy?
# Y el usuario da la respuesta: “¡Bien, porque me comí una hamburguesa!”
# Entonces el archivo debería quedar de la forma:
# ¿Cómo estás hoy?
# ¡Bien, porque me comí una hamburguesa!
# 2. En un archivo llamado regalo.txt se tiene la lista de las personas que quieren participar en el regalo de
# cumpleaños de Sol (en cada línea está el nombre de una persona). El encargado de organizar el regalo
# es Ale, y quiere saber más información antes de ir a comprarle algo a Sol.
# a. Mostrar por pantalla los nombres de las personas que quieren participar en el regalo.
# b. Se sabe que quieren poner 1000 pesos por persona por regalo. Hacer una función que devuelva
# cuánto dinero tiene Ale para hacerle el regalo a Sol. Es decir si se tiene un archivo de esta forma:
# Agus
# Manu
# Santi
# Lorena
# Maria
# La función tiene que devolver 5000
# c. Tomi sabe que si participa Santi, también participa Tomi. Se pide que si Santi está en el archivo
# de los nombres, se agregue también a Tomi.
# 3. En un hogar se quieren organizar mejor con las compras, por lo que se quiere guardar en un archivo la
# lista de productos que se necesitan para la próxima vez que la familia vaya al supermercado. Se pide
# hacer un programa que cree un archivo de compras.txt (Ayuda: abrir el archivo en modo w) y le
# pregunte al usuario qué necesita comprar hasta que ingrese una X. Por ejemplo:
# > ¿Qué agrego a la lista de compras?
# > Papa
# > ¿Qué agrego a la lista de compras?
# 2
# Archivos GUIA DE EJERCICIOS Nº 6
# > Pollo
# > ¿Qué agrego a la lista de compras?
# > Fideos
# > ¿Qué agrego a la lista de compras?
# > X
# El archivo tendría que estar de la siguiente forma:
# Papa
# Pollo
# Fideos
# 4. Se tiene un archivo con el siguiente texto:
# Paco Peco, chico rico,
# insultaba como un loco
# a su tío Federico;
# y éste dijo: Poco a poco,
# Paco Peco, poco pico. Me han dicho que has dicho un dicho
# que han dicho que he dicho yo,
# el que lo ha dicho, mintió,
# y en caso que hubiese dicho
# ese dicho que tú has dicho
# que han dicho que he dicho yo,
# dicho y redicho quedó.
# y estaría muy bien dicho,
# siempre que yo hubiera dicho
# ese dicho que tú has dicho
# que han dicho que he dicho yo.
# Se pide hacer un programa que pida dos palabras: una que se quiera reemplazar y la palabra por la que
# se quiera reemplazar, cambie el texto y lo guarde en el archivo otra vez. Por ejemplo, si la función recibe
# “poco” y “mucho”, reemplaza “poco” por “mucho” todas las veces que aparezca en el texto.
# 5. Se tiene un archivo csv que contiene información sobre el stock de una librería. Se guarda por cada
# línea, el nombre del producto, el código, el precio por unidad y el stock actual, es decir:
# nombre;código;precio;stock
# Un posible ejemplo de este archivo es el siguiente:
# lapiceras;34512;50;120
# cuadernos;41611;500;130
# sacapuntas;62812;30;210
# …
# 3
# Archivos GUIA DE EJERCICIOS Nº 6
# Se pide:
# a. Leer el archivo y mostrarlo por pantalla con el siguiente formato:
# Nombre producto: lapiceras
# Código producto: 34512
# Precio por unidad: 50
# Stock: 120
# Nombre producto: cuadernos
# Código producto: 41611
# Precio por unidad: 500
# Stock: 130
# …
# b. Hacer una función que reciba un diccionario que describa una línea del archivo y lo
# agregue, es decir que si se recibe un diccionario del tipo:
# {
# “nombre”: “hojas A4”,
# “código”: 35662,
# “precio”: 600,
# “stock”: 45
# }
# 6. Una profesora tiene una lista de diccionarios para guardar las notas que sacaron sus alumnos en el
# último parcial que tomó. Cada uno de esos diccionarios tiene el nombre del alumno, su apellido, su dni
# y la nota que sacó.
# a. Hacer una función que reciba este diccionario, y guarde las notas en un archivo csv, llamados
# notas.csv
# b. Tiempo después de guardar las notas, la profesora quiso saber la cantidad de alumnos que
# aprobaron. Hacer una función que lea el archivo creado en el ejercicio anterior, y devolver la
# cantidad de alumnos aprobados (su nota es mayor a 4).
# 7. En un cine tienen dos archivos .txt, uno con salas y otro con nombres de películas. Se sabe que en la
# sala de una fila del archivo se va a transmitir la película de la misma fila del archivo de películas. Se pide
# leer los dos archivos, y crear un nuevo archivo csv que tenga el nuevo formato sala;pelicula
# Por ejemplo si se tienen los siguientes archivos:
# (salas.txt) (peliculas.txt)
# D2 Megamente
# F1 Rápidos y furiosos
# E4 El padrino
# 4
# Archivos GUIA DE EJERCICIOS Nº 6
# El nuevo archivo deberá quedar:
# (funciones.csv)
# D2;Megamente
# F1;Rápidos y furiosos
# E4;El padrino
# 8. Santi le fue mostrando colores a sus amigos y cada amigo le fue diciendo si le gusta o no. Guardó cada
# respuesta en un .csv de la siguiente manera: nombre;color;le gusta, pero se dió cuenta que no es una
# forma muy práctica de guardarlo, así que lo quiere cambiar. Hacer un programa que lea el archivo y lo
# transforme en un archivo .txt. Es decir que si se tiene un archivo csv de la siguiente forma:
# Agus;verde;si
# Tomi; violeta;no
# Manu;marrón;no
# El archivo .txt tiene que quedar así:
# A Agus sí le gusta el verde
# A Tomi no le gusta el violeta
# A Manu no le gusta el marrón