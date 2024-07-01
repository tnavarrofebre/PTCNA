import numpy as np
import os

for filename in os.listdir('listas'):  # Cambia la ruta a tu carpeta
    if filename.endswith(".xvg"):
        minimo, maximo, numero = 0, 4, 41

        s = np.linspace(minimo, maximo, numero)

        T1 = []

        for c in s:
            t = []

            with open(os.path.join('listas', filename), 'r') as f:
                for line in f:
                    l = line.split(' ')
                    if c < float(l[-2]) < c + (maximo / (numero - 1)):
                        t.append(float(l[0]))
                    else:
                        if len(t) > 1:
                            T1.append((t[0], t[-1]))
                        t = []

                if len(t) > 1:  # Agregar el último intervalo si es necesario
                    T1.append((t[0], t[-1]))
            output_filename = filename.replace(".xvg", "_intervalos.xvg")
            with open(output_filename, "a") as m:
                m.write(str(round(c, 1)) + ' ' + str(round(c + (maximo / (numero - 1)), 1)) + '\t' + str(T1).strip('[]') + "\n")
                T1 = []
