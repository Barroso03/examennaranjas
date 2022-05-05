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



    

    




    










