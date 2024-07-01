import os
import shutil

# Directorio principal
directorio_principal = "g_rs"

# Obtener la lista de archivos en el directorio principal
archivos = os.listdir(directorio_principal)

# Crear un diccionario para agrupar los archivos por la parte deseada del nombre
archivos_por_grupo = {}

# Iterar a través de los archivos y agruparlos por la parte deseada del nombre
for archivo in archivos:
    partes = archivo.split('-')
    if len(partes) >= 3:
        grupo = '-'.join(partes[1:3])  # La parte 2.8-2.9
        if grupo not in archivos_por_grupo:
            archivos_por_grupo[grupo] = []
        archivos_por_grupo[grupo].append(archivo)

# Crear subcarpetas y mover los archivos a ellas
for grupo, archivos in archivos_por_grupo.items():
    carpeta_grupo = os.path.join(directorio_principal, grupo)
    os.makedirs(carpeta_grupo, exist_ok=True)  # Crear la carpeta si no existe
    for archivo in archivos:
        origen = os.path.join(directorio_principal, archivo)
        destino = os.path.join(carpeta_grupo, archivo)
        shutil.move(origen, destino)

print("Archivos organizados correctamente.")

	    
