<h1 align="center">	Examen naramjas</h1>

<h2>Repositorio:</h2>

Este es el link del [repositorio](https://github.com/Barroso03/examennaranjas.git)
***
<h2>¿De qué trata esta tarea?</h2>

En este examen hemos cogido un dataset con una variable llamada naranjas que tenía 100 lineas de datos de pesos de distintas naranjas y hemos analizado sus datos estadísticos y hemos dibujado sus gráficos
***




## Código:<a name="id1"></a>



```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



def dataframe_naranjas():
    naranjas = pd.DataFrame(np.random.randint(100, 230, 100), columns=['naranjas'])
    naranjas = naranjas.dropna()
    naranjas.sort_values(by=['naranjas'], inplace=True)
    naranjas.to_csv('naranjas.csv', index=False)
    naranjas = pd.read_csv('naranjas.csv')
    return naranjas
print(dataframe_naranjas())



def media(naranjas):
    media = naranjas['naranjas'].mean()
    return media
print('La media del peso de las naranjas es:',media(dataframe_naranjas()))



def desviacion(naranjas):
    desviacion = naranjas['naranjas'].std()
    return desviacion
print('La desviacion del peso de las naranjas es:',desviacion(dataframe_naranjas()))



def varianza(naranjas):
    varianza = naranjas['naranjas'].var()
    return varianza
print('La varianza del peso de las naranjas es:',varianza(dataframe_naranjas()))



def mediana(naranjas):
    mediana = naranjas['naranjas'].median()
    return mediana
print('La mediana del peso de las naranjas es:',mediana(dataframe_naranjas()))


def moda(naranjas):
    moda = naranjas['naranjas'].mode()
    return moda
print('La moda de las naranjas es:',moda(dataframe_naranjas()))


def cuartiles(naranjas):
    cuartiles = naranjas['naranjas'].quantile([0.25, 0.75])
    return cuartiles
print('Los cuartiles de las naranjas son:',cuartiles(dataframe_naranjas()))




def menores(naranjas):
    menores = naranjas['naranjas'][naranjas['naranjas'] < 130].count()
    return menores
print('Hay',menores(dataframe_naranjas()),'naranjas que pesan menos 130')



def grafico_barras(naranjas):
    plt.figure(figsize=(10,5))
    sns.countplot(naranjas['naranjas'])
    plt.xticks(rotation=90)
    plt.title('Naranjas')
    plt.xlabel('Peso de la naranja en gramos')
    plt.ylabel('Cantidad de naranjas')
    plt.savefig('graficos/diagrama_barras.png')
    plt.show()
grafico_barras(dataframe_naranjas())



def dispersión(naranjas):
    naranjas = pd.read_csv('naranjas.csv')
    data= naranjas['naranjas'].groupby(pd.cut(naranjas['naranjas'], range(100,240,10))).count()
    fig, ax = plt.subplots()
    lista=[]
    for i in range(100,230,10):
        lista.append(i)
    plt.scatter(lista, data)
    plt.title('Naranjas')
    plt.show()
    fig.savefig('graficos/diagrama_dispersion.png')
dispersión(dataframe_naranjas())





def grafico_pastel(naranjas):
    fig, ax = plt.subplots()
    sectores =["<130", "130", " >130"]
    porcentajes = [naranjas['naranjas'][naranjas['naranjas'] < 130].count(), naranjas['naranjas'][naranjas['naranjas'] == 130].count(), naranjas['naranjas'][naranjas['naranjas'] > 130].count()]
    wedges, texts, autotexts = ax.pie(porcentajes, labels=sectores, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Naranjas')
    plt.show()
    fig.savefig('graficos/diagrama_sectores.png')
grafico_pastel(dataframe_naranjas())

```


***

## Explicación código:
**Pasos:**

**1.** Importamos las librerías necesarias:
 
    -Pandas: esta librería sirve para crear el dataframe y leerlo.
    -Numpy: esta librería sirve para hacer calculos matemáticos como la media o 
    la varianza.
    -Matplotlib: esta libreria sirve para hacer diadramas en dos dimensiones como 
    diagramas de barras.
    -Seaborn:  esta libreria sirve para hacer diagrama mas complejos que los de 
    matplotlib.

**2.** Creamos una funcion para que cree el dataframe, lo limpie, lo ordene de menor a mayor,permita leerlo y lo devuelva.

**3.** Creamos las siguientes funciones estadisticas para proceder al estudio del dataframe:
       
    -Media: calcula la media con .mean() que es una función de numpy para 
    calcular la media.
    -Desviación típica: calcula la desviación típica con .std() que es una 
    función de numpy para calcular la desviación típica.
    -Varianza: calcula la varianza con .var() que es una función de numpy para 
    calcular la varianza.
    -Mediana: calcula la mediana con .median() que es una función de numpy para 
    calcular la mediana.
    -Moda: calcula la moda con .mode() que es una función de numpy para calcular 
    la moda.
    -Cuartiles: calcula los cuartiles 25 y 75 con .quantile() que es una función 
    de numpy para calcular los cuartiles.
       
**4.** Creamos la función menores para responder la pregunta de cuantas naranjas pesan menos de 130

**5.** Creamos las siguientes gráficas:
    
    -Diagrama de sectores: utilizamos la librería Matplotlib. Dentro de esta función encontramos uso de diversas funciones como son:
   
    *ax.pie(): se utiliza para trazar gráficos circulares.
    *plt.subplots(): es una función que devuelve una tupla que contiene una 
    figura y objeto (s) de ejes. Por lo tanto, al usar fig, ax = plt.subplots() 
    descomprime esta tupla en las variables fig y ax. Teniendo fig es útil si 
    desea cambiar los atributos a nivel de figura o guardar la figura como un 
    archivo de imagen más tarde (por ejemplo, con 
    fig.savefig('yourfilename.png')).
    *plt.title(): lo utlizamos para especificar el título de la visualización 
    representada.

   -Diagrma de barras: utilizamos dos librerías: Matplotlib y Seaborn.
                       
    *sns.countplot(): se usa para mostrar los conteos de observaciones en cada 
    contenedor categórico usando barras.
                         
   
   -Diagrama de dispersión: utilizamos la libreía Matplotlib.
   
   *plt.scatter(): se usa para crear diagramas de dispersión

  
      


