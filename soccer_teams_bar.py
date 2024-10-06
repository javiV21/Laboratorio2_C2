# https://www.kaggle.com/datasets/santiagovolpi/los-100-clubes-de-futbol-mejor-valuados-del-mundo
"""
Gráfico de barras.
Finalidad: ver cuáles son los 10 equipos españoles más caros respecto a su plantilla
(jugadores que componen el equipo). El dataset tiene más información, pero se ha limitado
a los 10 más caros que compiten en LaLiga (España) para el ejemplo, y a su vez, optimizar
la ejecución del progrma. La notación '1e8' en la parte superior del eje y significa
que es 1*10^8, equivalente a tener valores de longitud: 100,000,000.
"""
# importar las librerías necesarias.
import matplotlib.pyplot as plt
import pandas as pd
# obtener los registros del dataset.
df = pd.read_csv("soccer_teams.csv")
# obtener los registros del dataset donde 'Competition' contiene el valor 'LaLiga'.
laLiga = df[df["Competition"] == "LaLiga"]
# eliminar caracteres imcompatibles con datos tipo 'float'.
laLiga["Market_value"] = laLiga["Market_value"].str.replace("€", "", regex=False)
laLiga["Market_value"] = laLiga["Market_value"].str.replace("m", "", regex=False)
# convertir a 'float'.
laLiga["Market_value"] = laLiga["Market_value"].astype(float)
# obtener los 10 equipos más caros de LaLiga.
top10 = laLiga.sort_values("Market_value", ascending=False).head(10)
laLiga = top10.sort_values("Club")
# asignar valores al eje x.
x = laLiga["Club"]
# asignar valores al eje y.
y = laLiga["Market_value"]*1000000

# lista de colores para las barras.
colores = ['red', 'blue', 'black', 'yellow', 'green', 
            'grey', 'blue', 'red', 'orange', 'yellow']

# color de fondo.
plt.figure(facecolor='#E6E6FA')
# creación de gráfico de líneas con parámetros necesarios para apariencia.
plt.bar(x, y, color=colores)
# título del gráfico y tamaño de letra.
plt.title("Precio de las 10 plantillas más caras de los\nequipos que compiten en LaLiga, España (2020).", fontsize=15)
# etiqueta eje x.
plt.xlabel("Equipo", fontsize=14)
# etiqueta eje y.
plt.ylabel("Precio (millones)", fontsize=14)
# rotar etiquetas de eje x.
plt.xticks(rotation=45, ha='right')
# marcar líneas horizontales dentro del gráfico.
plt.grid(axis='y', linestyle='--', alpha=0.8)
# evitar colapso de elementos.
plt.tight_layout()
# mostrar ventana.
plt.show()

"""
----------------------------------------------------------------------------
Análisis: se puede observar que de las 10 plantillas más caras de equipos
españoles, hay una gran difrencia entre la más cara y la que, en comparación
con el resto, es más barata. El órden de mayor a menor quedaría de la
siguiente manera:
1-Real Madrid.
2-FC Barcelona.
3-Atlético de Madrid.
4-Sevilla FC.
5-Real Sociedad.
6-Villareal FC.
7-Valencia FC.
8-Real Betis Balompié.
9-Athletic Bilbao.
10-Getafe FC.

Cabe recordar que estos datos son en base a las plantillas que tenían en el
año 2020. De la información graficada se puede concluir lo siguiente:
-El equipo con la plantilla más cara es el Real Madrid (€793.50m).
-El equipo con la plantilla más barata es el Getafe FC (€159.45m).
----------------------------------------------------------------------------
"""