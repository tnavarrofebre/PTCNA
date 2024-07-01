with open("dist.ndx", "r") as file:
    lineas = file.read()
    lineas = lineas.split("\n")

arg = []
Arg = []
Dic = []
for i, linea in enumerate(lineas):
    if linea.startswith("["):
        if len(arg) > 0: 
            Dic.append([indice,Arg])
            Arg = []
        if len(arg) > 0:
            Arg.append(arg)
            arg = []
        indice = linea
    else:
        arg.append(linea)

print(Dic)