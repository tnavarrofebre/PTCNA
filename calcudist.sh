#!/bin/bash
# Este programa está basado en el otorgado por Griselda Corral para la generación automática de
# archivos .xvg para generar las g(r)

rm -f fort.*

# a indica el número de átomo (grupo) central
# 1 es el grupo de los OW
# cambiar los límites del intervalo según lo guardado en index.ndx

for a in $(seq 0 284)
do

# comando de gromacs

gmx distance -f TRP-NaCl-1M.trr -n pares2.ndx -oall distancias/dist-$a.xvg -dt 1 <<EOF

$a

EOF

done
