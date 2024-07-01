import os

# Directorio principal
directorio_principal = "g_rs"

# Obtener la lista de carpetas dentro del directorio principal
carpetas = [nombre_carpeta for nombre_carpeta in os.listdir(directorio_principal) if os.path.isdir(os.path.join(directorio_principal, nombre_carpeta))]

# Procesar cada carpeta
for carpeta in carpetas:
    carpeta_ruta = os.path.join(directorio_principal, carpeta)
    archivos = [archivo for archivo in os.listdir(carpeta_ruta) if archivo.endswith("-gr.xvg")]

    if len(archivos) > 0:
        # Crear el archivo de salida llamado "gr.xvg"
        archivo_salida = os.path.join(carpeta_ruta, "gr.xvg")

        # Inicializar una lista para almacenar los promedios
        promedios = []

        # Leer los archivos -gr.xvg y calcular el promedio de cada fila
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_ruta, archivo)
            with open(ruta_archivo, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    valores = line.strip().split()
                    if valores:
                        primer_valor = float(valores[0])
                        valores_fila = [float(valor) for valor in valores[1:]]
                        promedio_fila = sum(valores_fila) / len(valores_fila) if len(valores_fila) > 0 else 0.0
                        promedios.append((primer_valor, promedio_fila))

        # Escribir los promedios en el archivo de salida
        with open(archivo_salida, 'w') as f:
            for primer_valor, promedio_fila in promedios:
                f.write(f"{primer_valor} {promedio_fila}\n")

print("Operación completada.")


	    
