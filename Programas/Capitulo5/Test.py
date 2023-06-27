import numpy as np
from PIL import Image
import os
import random
from sklearn.model_selection import train_test_split

# Directorio principal donde se encuentran las imágenes
directorio_principal = r"D:/GitHub/Modulo-2---IA---Minirobots/Programas/Capitulo5/frutas_dataset1"

# Lista de las frutas
frutas = ["manzanas", "peras", "bananos", "fresas"]

# Tamaño deseado para las imágenes
tamaño_imagen = (100, 100)  # Ejemplo de tamaño, puedes ajustarlo según tus necesidades

# Lista para almacenar las imágenes y sus etiquetas
imagenes = []
etiquetas = []

# Recorre cada fruta y carga las imágenes etiquetadas
for etiqueta, fruta in enumerate(frutas):
    carpeta_fruta = os.path.join(directorio_principal, fruta)
    archivos = os.listdir(carpeta_fruta)
    
    for archivo in archivos:
        ruta_completa = os.path.join(carpeta_fruta, archivo)
        imagen = Image.open(ruta_completa)
        
        # Redimensiona la imagen al tamaño deseado
        imagen_redimensionada = imagen.resize(tamaño_imagen)
        
        # Convierte la imagen en un array de píxeles y normalízala
        imagen_array = np.array(imagen_redimensionada) / 100.0
        
        # Agrega la imagen y su etiqueta a las listas
        imagenes.append(imagen_array)
        etiquetas.append(etiqueta)

# Convierte las listas en arrays numpy
imagenes = np.array(imagenes)
etiquetas = np.array(etiquetas)

# Divide el conjunto de datos en entrenamiento y validación
imagenes_entrenamiento, imagenes_validacion, etiquetas_entrenamiento, etiquetas_validacion = train_test_split(
    imagenes, etiquetas, test_size=0.2, random_state=42)

# Divide el conjunto de validación en validación y prueba
imagenes_validacion, imagenes_prueba, etiquetas_validacion, etiquetas_prueba = train_test_split(
    imagenes_validacion, etiquetas_validacion, test_size=0.5, random_state=42)

# Imprime la forma de los conjuntos de datos resultantes
print("Forma de los conjuntos de datos:")
print("Entrenamiento:", imagenes_entrenamiento.shape, etiquetas_entrenamiento.shape)
print("Validación:", imagenes_validacion.shape, etiquetas_validacion.shape)
print("Prueba:", imagenes_prueba.shape, etiquetas_prueba.shape)
