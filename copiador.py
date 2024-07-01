import os

# Directorio principal
directorio_principal = "g_rs"

# Obtener la lista de carpetas dentro del directorio principal
carpetas = [nombre_carpeta for nombre_carpeta in os.listdir(directorio_principal) if os.path.isdir(os.path.join(directorio_principal, nombre_carpeta))]

# Procesar cada carpeta
for carpeta in carpetas:
    carpeta_ruta = os.path.join(directorio_principal, carpeta)
    archivos = [archivo for archivo in os.listdir(carpeta_ruta) if archivo.endswith(".xvg")]

    if len(archivos) > 0:
        # Crear un diccionario para almacenar las segundas columnas
        segundas_columnas = {}

        # Leer todas las segundas columnas de los archivos
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_ruta, archivo)
            with open(ruta_archivo, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip() and not line.startswith("@") and not line.startswith("#"):
                        tokens = line.strip().split()
                        if len(tokens) == 2:
                            x_value, y_value = float(tokens[0]), float(tokens[1])
                            if x_value not in segundas_columnas:
                                segundas_columnas[x_value] = []
                            segundas_columnas[x_value].append(y_value)

        # Crear el archivo de salida con el nombre de la carpeta más '-gr.xvg'
        archivo_salida = os.path.join(carpeta_ruta, f"{carpeta}-gr.xvg")
        with open(archivo_salida, 'w') as f:
            # Escribir la primera columna y las segundas columnas combinadas
            for x_value in sorted(segundas_columnas.keys()):
                f.write(f"{x_value} ")
                valores_y = segundas_columnas[x_value]
                for y_value in valores_y:
                    f.write(f"{y_value} ")
                f.write("\n")

print("Operación completada.")

