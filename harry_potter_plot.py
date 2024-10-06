# https://www.kaggle.com/datasets/maricinnamon/harry-potter-movies-dataset
"""
Gráfico de líneas.
Finalidad: ver cuánto dinero se recaudó en taquilla por cada película de la
saga 'Harry Potter'. La notación '1e9' en la parte superior del eje y significa
que es 1*10^9, equivalente a tener valores de longitud: 1,000,000,000. El
motivo de la notación es para representar la 'frecuencia' de una forma corta.
"""
# importar las librerías necesarias.
import matplotlib.pyplot as plt
import pandas as pd
# obtener los registros del dataset.
df = pd.read_csv("harry_potter.csv")
# asignar valores del eje x.
x = df["Movie Title"]
# eliminar caracteres imcompatibles con datos tipo 'int'.
df["Box Office"] = df["Box Office"].str.replace("$", "", regex=False)
df["Box Office"] = df["Box Office"].str.replace(",", "", regex=False)
# convertir a 'int'.
df["Box Office"] = df["Box Office"].astype(int)
# asignar valores al eje y.
y = df["Box Office"]

# color de fondo.
plt.figure(facecolor='#cac5cd')
# creación de gráfico de líneas con parámetros necesarios para apariencia.
plt.plot(x, y, color='red', marker=".")
# título del gráfico y tamaño de letra.
plt.title("Millones ($) recaudados en taquilla\nde la saga de 'Harry Potter'.", fontsize=15)
# etiqueta eje x.
plt.xlabel("Película", fontsize=14)
# etiqueta eje y.
plt.ylabel("Recaudado (millones)", fontsize=14)
# rotar etiquetas de eje x.
plt.xticks(rotation=45, ha='right')
# evitar colapso de elementos.
plt.tight_layout()
# marcar cuadrícula dentro del gráfico.
plt.grid()
# mostrar ventana.
plt.show()

"""
----------------------------------------------------------------------
Análisis: con el gráfico de líneas se puede observar que cada película
de Harry Potter tuvo diferente impacto en cuanto a ventas en taquilla.
La primer película generó $1,002,000,000 en taquilla. Las siguientes 2
no fueron tan exitosas en comparación a la 1; sin embargo, generaron
ingresos de $880,300,000 (la 2) y $796,700,000 (la 3). Fue a partir de
la 4 que tuvo un crecimiento sin interrupción, pues de la 4 a la 7 los
ingresos aumentaron dentro del rango de ochocientos cincuenta a mil
millones de dólares. La 6 generó $1,200,000 más que la 5, pero no es
tan apreciable en la gráfica por sus rangos de valores en el eje y. La
última película (8) tuvo un ingreso mayor al resto, con un ingreso de
$1,342,000,000, convirtiéndose así en la película (de la saga) que más
ventas en taquilla generó.

Se puede concluir que, de toda la saga:
-La película que más ingresos generó fue la 8 ($1,342,000,000).
-La película que menos ingresos generó fue la 3 ($796,700,000).
-De la 1 a la 3 los ingresos fueron decrecientes.
-De la 3 a la 8 los ingresos fueron crecientes.
----------------------------------------------------------------------
"""