# ETL para aplicar a los datasets de reviews de google
# Eliminar columnas innecearias
df_reviews_sample.drop(columns=['time', 'pics'], axis=1, inplace=True)

# convertir la columna resp en formato booleano 
df_reviews_sample['resp'] = df_reviews_sample['resp'].notna()

# analisis de sentimiento sobre la columna text para cuantificar las reviews de los usuarios en una escala entre 0 y 2 donde 0 es neutral, 1 es negativo y 2 es positivo
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Descargar el lexicon necesario para el análisis de sentimientos
nltk.download('vader_lexicon')

# Crear una instancia del analizador de sentimientos
sia = SentimentIntensityAnalyzer()
# Convertimos la columna 'review' en tipo string para aplicar nuestrop modelo de analisis de sentimiento
df_reviews_sample['text'] = df_reviews_sample['text'].astype(str)

# Supongamos que tienes un DataFrame llamado df con una columna "reviews"
# Calcula el puntaje de sentimiento para cada reseña y crea una nueva columna "sentimiento"
df_reviews_sample['sentimiento'] = df_reviews_sample['text'].apply(lambda x: sia.polarity_scores(x)['compound'])

# Define umbrales para clasificar las reseñas en positivas, neutrales y negativas
umbral_positivo = 0.2
umbral_negativo = -0.2

# Crea una nueva columna "sentimiento_etiqueta" para clasificar en positivo, neutral y negativo
df_reviews_sample['sentiment_analysis'] = df_reviews_sample['sentimiento'].apply(lambda x: 2 if x > umbral_positivo else (0 if x < umbral_negativo else 1))