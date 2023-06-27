import os

# Ruta de la carpeta principal
carpeta_principal = r"D:/GitHub/Modulo-2---IA---Minirobots/Programas/Capitulo5/frutas_dataset1"

# Obtener una lista de todas las carpetas en la carpeta principal
carpetas_frutas = ["bananos", "fresas", "manzanas", "peras"]

# Recorrer cada carpeta de frutas
for carpeta_fruta in carpetas_frutas:
    ruta_carpeta_fruta = os.path.join(carpeta_principal, carpeta_fruta)
    
    # Obtener una lista de las subcarpetas en la carpeta de frutas
    subcarpetas = [nombre for nombre in os.listdir(ruta_carpeta_fruta) if os.path.isdir(os.path.join(ruta_carpeta_fruta, nombre))]
    
    # Cambiar los nombres de las subcarpetas
    for i, subcarpeta in enumerate(subcarpetas):
        nueva_subcarpeta = f"subcarpeta{i+1}"
        ruta_actual = os.path.join(ruta_carpeta_fruta, subcarpeta)
        nueva_ruta = os.path.join(ruta_carpeta_fruta, nueva_subcarpeta)
        os.rename(ruta_actual, nueva_ruta)
        print(f"Carpeta renombrada: {ruta_actual} -> {nueva_ruta}")
