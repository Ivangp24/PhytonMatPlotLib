#Consume los datos del archivo inversiones
#Almacena en un dataframe el NOM_ENS, la superficie y el TIPUSSOL
#Gráfico de dispersión de los totales de superficie por TIPUSSOL
#Gráfico de barras de la superficie media de los 10 primeros NOM_ENS
#Gráfico circular de la superficie de 10 TIPUSSOL

import pandas as pd
import matplotlib.pyplot as plt

def consumirInversiones():
    datos=pd.read_csv('suelo.csv')
    #print(datos)
    df=datos[['NOM_ENS', 'SUPERFICIE', 'TIPUSSOL']]
    #print(df)
    df.plot.scatter(x="SUPERFICIE", y='TIPUSSOL', alpha=0.3)
    plt.show()

consumirInversiones()