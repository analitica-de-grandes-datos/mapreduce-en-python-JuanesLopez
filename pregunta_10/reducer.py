#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from operator import concat
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    col=[]
    numbers = ''
    

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            col.append(val)
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                col.sort()
                numbers = str(col.pop(0))
                for x in col:
                    numbers = numbers + ',' + str(x)
                            
                sys.stdout.write("{}\t{}\n".format(curkey,numbers))
                col = []

            curkey = key
            col.append(val)
    col.sort()
    numbers = str(col.pop(0))
    for x in col:
        numbers = numbers + ',' + str(x)                            
    sys.stdout.write("{}\t{}\n".format(curkey,numbers))