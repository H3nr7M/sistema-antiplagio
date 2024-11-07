import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# # Cargar los títulos de las tesis desde el archivo Excel
# df = pd.read_excel('tus_tesis.xlsx')
# titulos_existentes = df['Título'].tolist()

# nltk.download('stopwords')
# stop_words = set(stopwords.words('spanish'))

# def preprocesar_texto(texto):
#     palabras = word_tokenize(texto)
#     palabras_filtradas = [palabra for palabra in palabras if palabra not in stop_words]
#     # Aquí podrías agregar lematización si lo deseas
#     return palabras_filtradas

# vectorizer = TfidfVectorizer()
# tfidf_matrix = vectorizer.fit_transform(titulos_existentes)

# def encontrar_similares(nuevo_titulo):
#     nuevo_vector = vectorizer.transform([nuevo_titulo])
#     similitudes = cosine_similarity(nuevo_vector, tfidf_matrix)[0]
#     return similitudes

# titulo_propuesto = "Mi tesis sobre inteligencia artificial"
# similares = encontrar_similares(titulo_propuesto)
# # Establecer un umbral de similitud (por ejemplo, 0.8)
# umbral = 0.8
# indices_similares = np.where(similares > umbral)[0]
# if len(indices_similares) > 0:
#     print("Se encontraron títulos similares:")
#     for indice in indices_similares:
#         print(titulos_existentes[indice])