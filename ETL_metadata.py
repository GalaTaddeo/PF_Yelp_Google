# ETL de dataframe de metadata el cual contiene informacion de los negocios 

# Librerias a usar 
import pandas as pd 
import numpy as np

# Eliminar columnas inservibles

df = "ruta" # aqui debemos depositar el dataset que queramos tratar
df = df.drop(columns=['description','avg_rating', 'num_of_reviews', 'price', 'hours', 'state', 'relative_results', 'url'])

# Creamos la variable location la cual contendra las coordenadas del negocio concatenando las variables latitude y longitude separados con una ,

df['location'] = df['latitude'].map(str) + ', ' + df['longitude'].map(str)

# EL siguientes algoritmo separa el string de la columna address en 4 columnas 'direccion', 'ciudad', 'estado', 'codigo_postal'

def procesar_direccion(address):
    if not address:
        return [None, None, None, None]
    partes = address.split(', ')
    if len(partes) >= 3:
        direccion = ', '.join(partes[:-2])
        ciudad = partes[-2]
        estado_y_codigo = partes[-1]
        estado, codigo_postal = estado_y_codigo.split(' ')[0], ' '.join(estado_y_codigo.split(' ')[1:])
        return [direccion, ciudad, estado, codigo_postal]
    else:
        # Manejar direcciones que no cumplen con el formato esperado
        return [address, None, None, None]  # Ajusta según sea necesario

# Aplicamos la función y expandimos el resultado en nuevas columnas
    
df[['direccion', 'ciudad', 'estado', 'codigo_postal']] = pd.DataFrame(df['address'].apply(procesar_direccion).tolist(), index=df.index)

# Ahora realizaremos un filtro en el estado donde se encuentra el neogico en este caso sera la florida "fl"

df = df[df['estado'] == 'FL']

# Eliminar columnas inservibles las cuales fueron reemplazadas con las anteriores trnasformaciones 

df = df.drop(['address', 'latitude', 'longitude'], axis=1, errors='ignore')

# El siguiente algoritmo realizara un filtro sobre la columna category para enfocar los datos en nuestra objetivo 

df["category"] = df["category"].apply(lambda x: str(x).lower()) # convertri los datos a minisculas

def filter_dataframe_by_multiple_words(df, column_name, keywords):

  filtered_df = pd.DataFrame()
  for keyword in keywords:
    filtered_df = pd.concat([filtered_df, df[df[column_name].str.lower().str.contains(keyword.lower(), na=False)]])

  return filtered_df

column_name = "category"
keywords = ['meditation','fitness','ciclyng','pilates','wellness','boxing','athletic','tennis','health','weightlifting', 'juice', 'vegetarian', 'vegan', 'açaí','salad', 'gluten free', 'gluten-free', 'tofu', 'protein', 'spa', 'chiropractor', 'therapist', 'acunputurist', 'yoga', 'alternative medicine', 'vitamin', 'suplement','organic','fruit','natural', 'aromatherapy', 'nut', 'greengrocer']

df = filter_dataframe_by_multiple_words(df, column_name, keywords)

# Eliminar columnas innecearias 

df = df.drop('MISC', axis=1)