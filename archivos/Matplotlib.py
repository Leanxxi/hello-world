# Matplotlib
# Los siguientes ejercicios se pueden hacer en el siguiente link de Google Colab:
# https://colab.research.google.com/drive/1mRpM5aqSVkbgOGcZnHIH9Ay2C3Men4GY?usp=sharing, en el
# cual ya se tiene cargados los datos a graficar. Se recuerda que para poder editarlo se debe crear una copia del
# mismo.
# Ejercicios de Tipos de Gráfico
# Para realizar estos ejercicio, debemos importar la información del PBI per cápita de los
# distintos países, a lo largo de un período que abarca desde 1952 y 2007.
# # Importo la información
# url =
# "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.
# csv"
# data = pd.read_csv(url)
# # Modificar el tipo de dato:
# data['year'] = data['year'].astype("int")
# data.head()
# data.info()
# 1. Elegir un año en el que desees ver la relación entre la expectativa de vida de los habitantes
# (columna `lifeExp`) y el PBI per cápita de los habitantes (columna gdpPercap).
# # Modifica este valor
# # =========== Código de alumno ===============
# year =
# # ============================================
# 2
# Matplotlib GUIA DE EJERCICIOS
# data_year = data[data["year"] == year]
# data_year.head()
# Realizar un gráfico de puntos que muestre la relación entre la expectativa de vida (columna
# lifeExp) y el PBI per cápita de los habitantes (columna gdpPercap).
# El gráfico debe tener:
# ● Título apropiado
# ● Nombre y unidades de los ejes cartesianos
# ● Marcador de tipo triangular y color "#23A763"
# ● Grilla
# fig, ax = plt.subplots()
# # =========== Código de alumno ===============
# # ============================================
# plt.show()
# 2. Creamos un nuevo DataFrame con la información de la Argentina únicamente.
# data_arg = data[data["country"] == "Argentina"]
# data_arg.head()
# Realizar un gráfico de línea que muestre el PBI per cápita de los habitantes de Argentina
# (columna gdpPercap) a lo largo del tiempo:
# El gráfico debe tener:
# ● Título apropiado
# ● Nombre y unidades de los ejes cartesianos
# ● Linea sólida, espesor 2.2 y color "#30BFDE"
# 3
# Matplotlib GUIA DE EJERCICIOS
# ● Grilla
# fig, ax = plt.subplots()
# # =========== Código de alumno ===============
# # ============================================
# plt.show()
# 3. A continuación verá todos los países de los que poseemos información. Eligir uno que no
# sea nuestro país y luego, crear un nuevo DataFrame.
# data["country"].unique()
# # =========== Código de alumno ===============
# country =
# # ============================================
# data_country = data[data["country"] == country]
# data_country.head()
# Realizar un gráfico de línea que muestre el PBI per cápita de los habitantes de Argentina
# (columna gdpPercap) a lo largo del tiempo y del país escogido anteriormente:
# El gráfico debe tener:
# ● Título apropiado
# ● Nombre y unidades de los ejes cartesianos
# ● Linea sólida, espesor 2.2 y color "#30BFDE" para la curva de nuestro país.
# ● Linea sólida, espesor 2.2 y color "#1E92E3" para la curva del nuevo país.
# ● Referencias
# ● Grilla
# 4
# Matplotlib GUIA DE EJERCICIOS
# fig, ax = plt.subplots()
# # =========== Código de alumno ===============
# # ============================================
# plt.show()
# 4. A continuación vamos a agrupar PBI per capita por continente.
# data_continent = data[['continent', 'gdpPercap']]
# data_continent = data_continent.groupby(['continent']).agg('sum')
# data_continent
# Realizar un gráfico de torta la proporción del PBI per cápita de los habitantes de cada
# continente (columna gdpPercap).
# El gráfico debe tener:
# ● Título apropiado
# ● Cada parte con el nombre del continente y el porcentaje redondeado a las décimas.
# ● El color de cada parte será:
# ○ América: "#30BFDE"
# ○ Asia: "#E31E4B"
# ○ África: "#E36F1E"
# ○ Oceanía: "#1EE39B"
# ○ Europa: "#1E92E3"
# fig, ax = plt.subplots()
# # =========== Código de alumno ===============
# 5
# Matplotlib GUIA DE EJERCICIOS
# # ============================================
# plt.show()
# 5. Elegir un continente el cual te gustaría analizar con más detalle:
# # =========== Código de alumno ===============
# continent =
# # ============================================
# data_one_continent = data[data["continent"] == continent]
# data_one_continent = data_one_continent[['country', 'gdpPercap']]
# data_one_continent = data_one_continent.groupby(['country']).agg('sum')
# data_one_continent = data_one_continent.sort_values(by=['gdpPercap'])
# data_one_continent[['gdpPercap']]
# Realizar un gráfico de barras horizontales que muestre el PBI per cápita de los habitantes del
# continente escogido (columna gdpPercap).
# El gráfico debe tener:
# ● Título apropiado
# ● Nombre y unidades de los ejes cartesianos en caso de ser necesario
# ● Nombre de los paises al lado de cada barra
# ● Grilla con líneas verticales únicamente, color "#CDD7DA" y línea discontinua.
# fig, ax = plt.subplots()
# # =========== Código de alumno ===============
# # ============================================
# plt.show()
# 6
# Matplotlib GUIA DE EJERCICIOS
# Ejercicios de Grillas
# Para estos ejercicios, vamos a crear valores aleatorios, que serán contenidos en un
# DataFrame que llamaremos df:
# np.random.seed(0)
# df = pd.DataFrame(data={'a':np.random.randint(0, 100, 50),
# 'b':np.random.randint(0, 100, 50),
# 'c':np.random.randint(0, 100, 50),
# 'd':np.random.randint(0, 100, 50)})
# df.head()
# 6. Crear una grilla de 4 gráficos de línea, en la que los ejes x va a contener los valores del
# índice df.index.values, mientras que los ejes y, los valores de las columnas a, b, c y d.
# La figura debe tener:
# ● 2 filas y 2 columas
# ● Tamaño de figura de una altura de 8 y un ancho de 15.
# ● Nombre de los ejes y referencia en cada gráfico
# ● Grilla
# ● La siguiente posición de gráficos:
# ○ Los valores A en la parte superior izquierda, color green
# ○ Los valores B en la parte superior derecha, color red
# ○ Los valores C en la parte inferior izquierda, color magenta
# ○ Los valores D en la parte inferior derecha, color blue
# # =========== Código de alumno ===============
# # ============================================
# 7. Crear una grilla de 2 gráficos: uno de línea y otro de puntos, siendo los ejes x los valores del
# índice df.index.values, mientras que los ejes y, los valores de las columnas a, b, c y d.
# La figura debe tener:
# ● 2 filas y 1 columna
# ● Tamaño de figura de una altura de 8 y un ancho de 15.
# 7
# Matplotlib GUIA DE EJERCICIOS
# ● Título de cada gráfico
# ● Referencias
# ● Grilla
# ● La siguiente posición de gráficos:
# ○ Los valores A Y B en la parte superior, en un gráfico de línea, color green y red,
# tipo de línea sólida y discontinua respectivamente.
# ○ Los valores C Y D en la parte inferior, en un gráfico de puntos, color magenta y
# blue, marcador circular y triángulo invertido respectivamente.
# # =========== Código de alumno ===============
# # ============================================