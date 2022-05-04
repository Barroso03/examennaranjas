# haz un dataframe con una funcion de pandas con una variable llamada naranjas de 100 numeros entre 100 y 230
# ordena los datos de menor a mayor y lo guarda en un archivo csv
# abre el archivo csv y lo guarda en un dataframe
# haz la media de los datos
# haz la desviacion tipica de los datos
# haz la varianza de los datos
# haz la mediana de los datos



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def naranjas():
    naranjas = pd.DataFrame(np.random.randint(100, 230, 100), columns=['naranjas'])
    naranjas = naranjas.dropna()
    naranjas.sort_values(by=['naranjas'], inplace=True)
    naranjas.to_csv('naranjas.csv', index=False)
    naranjas = pd.read_csv('naranjas.csv')
    return naranjas
print(naranjas())
# haz una funcion que haga la media de los datos
def media(naranjas):
    media = naranjas['naranjas'].mean()
    return media
print('La media del peso de las naranjas es:',media(naranjas()))
# haz una funcion que haga la desviacion tipica de los datos
def desviacion(naranjas):
    desviacion = naranjas['naranjas'].std()
    return desviacion
print('La desviacion del peso de las naranjas es:',desviacion(naranjas()))
# haz una funcion que haga la varianza de los datos
def varianza(naranjas):
    varianza = naranjas['naranjas'].var()
    return varianza
print('La varianza del peso de las naranjas es:',varianza(naranjas()))
# haz una funcion que haga la mediana de los datos
def mediana(naranjas):
    mediana = naranjas['naranjas'].median()
    return mediana
print('La mediana del peso de las naranjas es:',mediana(naranjas()))
# haz una funcion que haga los cuartiles de los datos
def cuartiles(naranjas):
    cuartiles = naranjas['naranjas'].quantile([0.25, 0.75])
    return cuartiles
print('Los cuartiles de las naranjas son:',cuartiles(naranjas()))
# haz una funcion que te diga cuantas naranjas hay menores de 130
def menores(naranjas):
    menores = naranjas['naranjas'][naranjas['naranjas'] < 130].count()
    return menores
print('Hay',menores(naranjas()),'naranjas que pesan menos 130')


# haz una funcion de un grafico de barras que muestre el peso de las naranjas en el ejex y el numero de veces que se repite cada peso en el ejey
def grafico_barras(naranjas):
    plt.figure(figsize=(10,5))
    
    sns.countplot(naranjas['naranjas'])
    # dira los datos del eje x 90 grados
    plt.xticks(rotation=90)
    # pon el titulo del grafico
    plt.title('Naranjas')
    # pon el nombre de los ejes
    plt.xlabel('Peso de la naranja en gramos')
    plt.ylabel('Cantidad de naranjas')
    
    # guarda el archivo en una carpeta llamada graficos y ponle el nombre de diagrama_barras.png
    plt.savefig('graficos/diagrama_barras.png')
    
    plt.show()
grafico_barras(naranjas())





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
dispersión(naranjas())





# haz una funcion de un grafico de pastel que muestre el peso de las naranjas en el ejex y el numero de veces que se repite cada peso en el ejey
def grafico_pastel(naranjas):
    fig, ax = plt.subplots()
    sectores =["<130", "130", " >130"]
    porcentajes = [naranjas['naranjas'][naranjas['naranjas'] < 130].count(), naranjas['naranjas'][naranjas['naranjas'] == 130].count(), naranjas['naranjas'][naranjas['naranjas'] > 130].count()]
    wedges, texts, autotexts = ax.pie(porcentajes, labels=sectores, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title('Naranjas')
    plt.show()
    fig.savefig('graficos/diagrama_sectores.png')
grafico_pastel(naranjas())



    

    




    










