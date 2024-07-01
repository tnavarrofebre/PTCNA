
#!/bin/bash

# Cambia la ruta de la carpeta a la que deseas procesar
carpeta="intervalos"

for archivo in "$carpeta"/*.xvg; do
    if [ -f "$archivo" ]; then
        while IFS= read -r line; do
            # Buscar todos los pares de números entre paréntesis en la línea
            matches=$(echo "$line" | grep -oE '\(([0-9]+(\.[0-9]+)?), ([0-9]+(\.[0-9]+)?)\)')
            # Extraer todo lo que contiene la línea hasta el primer paréntesis
            contenido=$(echo "$line" | sed -E 's/\(.*//')
            # Reemplazar los espacios en blanco por guiones en el contenido
            contenido=$(echo "$contenido" | sed 's/ /-/g')
            # Contador para los pares
            pair_count=1
            # Extraer el número del nombre del archivo automáticamente
            filename="${BASH_SOURCE[0]}"
            filename=$(basename "$archivo")
            atom=$(echo "$archivo" | sed -E 's/[^0-9]//g')	
	    echo $filename
	    echo $atom

            # Iterar a través de los pares encontrados
            while IFS= read -r pair; do
                # Extraer los números de cada par
                num1=$(echo "$pair" | sed -E 's/\(([^,]+), ([^)]+)\)/\1/')
                num2=$(echo "$pair" | sed -E 's/\(([^,]+), ([^)]+)\)/\2/')
                pos="$contenido$pair_count"
                pos=$(echo "$pos" | sed 's/	/-/g')
                # Construir la variable 'pos' para este par
                echo $pos
                if ! [[ -z $num1 ]]; then
                    # Ejecutar el comando utilizando los números
                    gmx rdf -f md.trr -s md.gro -n index.ndx -o $atom-$pos.xvg -b $num1 -e $num2 <<EOF
                    3
                    a$atom
EOF
                    # Ejemplo: comando_a_ejecutar "$num1" "$num2"
                fi
                # Incrementar el contador de pares
                pair_count=$((pair_count+1))
            done <<< "$matches"
        done < "$archivo"
    fi
done




