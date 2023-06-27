import os

# Ruta de la carpeta
ruta_carpeta = r"D:/GitHub/Modulo-2---IA---Minirobots/Programas/Capitulo5/frutas_dataset1/peras/subcarpeta9"

# Número inicial
numero_inicial = 4342

# Obtener una lista de los archivos en la carpeta
archivos = [nombre for nombre in os.listdir(ruta_carpeta) if os.path.isfile(os.path.join(ruta_carpeta, nombre))]

# Ordenar los archivos alfabéticamente
archivos.sort()

# Cambiar los nombres de los archivos
for i, archivo in enumerate(archivos):
    nombre, extension = os.path.splitext(archivo)
    nuevo_numero = numero_inicial + i
    nuevo_nombre = f"peras{nuevo_numero}{extension}"
    ruta_actual = os.path.join(ruta_carpeta, archivo)
    nueva_ruta = os.path.join(ruta_carpeta, nuevo_nombre)
    os.rename(ruta_actual, nueva_ruta)
    print(f"Archivo renombrado: {ruta_actual} -> {nueva_ruta}")
