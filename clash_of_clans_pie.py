# https://www.kaggle.com/datasets/asaniczka/clash-of-clans-clans-dataset-2023-3-5m-clans/data
"""
Gráfico de pastel.
Finalidad: ver el porcentaje por cada tipo de ingreso (público, solo invitación, privado) a
un clan en el juego 'Clash of Clans'. He tomado los primeros 100 registros para optimizar
la ejecución del programa. Sin embargo, el dataset cuenta con más información.
"""
# importar las librerías necesarias.
import matplotlib.pyplot as plt
import pandas as pd
# función para traducir los valores de las columnas.
def Traducir(access):
    if (access == "open"):
        acceso = "Público"
    elif (access == "closed"):
        acceso = "Privado"
    elif (access == "inviteOnly"):
        acceso = "Solo invitación"
    return acceso
# obtener los 100 primeros registros del dataset.
df = pd.read_csv("clash_of_clans.csv", nrows=100)
# aplicar traducción a datos de columna 'clan_type'.
df["clan_type"] = df["clan_type"].apply(Traducir)
# asignar frecuencia.
frecuencia = df["clan_type"].value_counts()

# color de fondo.
plt.figure(facecolor='lightblue')
# lista de colores para el gráfico.
colores = ["#33FF57", "#3357FF", "#FF5733"]
# creación de gráfico de pastel con parámetros necesarios para apariencia.
plt.pie(frecuencia.values, labels=frecuencia.index, autopct="%1.0f%%"
        ,colors=colores, shadow=True, explode=[0.05,0,0], textprops={'fontsize':12})
# título del gráfico y tamaño de letra.
plt.title("Tipos de acceso a 100 clanes del juego 'Clash of Clans'.", fontsize=15)
# mostrar ventana.
plt.show()

"""
--------------------------------------------------------------------------
Análisis: gracias a la representación gráfica podemos observar que, de los
100 clanes analizados, el 70% de estos tiene un tipo de acceso público, el
25% permite acceso por medio de invitación, mientras que el 5% es privado;
es decir, no se puede acceder al clan.

Como estamos analizando 100 clanes, se puede entender que:
-70 clanes son públicos.
-25 clanes permiten el ingreso mediante invitación.
-5 clanes son privados.
--------------------------------------------------------------------------
"""