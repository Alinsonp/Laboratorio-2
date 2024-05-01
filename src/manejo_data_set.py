
import pandas as pd
import os
import pprint
import math
ruta_csv = './data_set/flights_final.csv'

#Ruta Absoluta del Dataset
ruta_absoluta = os.path.abspath(ruta_csv)

df = pd.read_csv(ruta_absoluta)

df = df.reset_index(drop=True)

#filtra el dataset sin filas que esten exactamente repetidas
df = df.drop_duplicates()
df = df.reset_index(drop=True)
num_filas, num_columnas = df.shape


#crear un diccionario para guardar el source_airport_code y el destination_airport_code, a los que son iguales ponerle el mismo id
diccionario = {}
codido_id = 1
for i in range(num_filas):
    if df['Source Airport Code'][i] not in diccionario:
        diccionario[df['Source Airport Code'][i]] = codido_id
        codido_id += 1

for i in range(num_filas):
    if df['Destination Airport Code'][i] not in diccionario:
        diccionario[df['Destination Airport Code'][i]] = codido_id
        codido_id += 1


def distancia_haversine(lat1, lon1, lat2, lon2):
    # Radio de la Tierra
    r = 6371.0

    # Convierte las coordenadas de grados a radianes
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Diferencia entre las longitudes y latitudes
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # Fórmula haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calcula la distancia
    distancia = r * c

    return distancia