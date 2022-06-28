#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    col1 = []
    col2 = []
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        aux1, aux2 = line.split("\t")
        col1.append(aux1)
        col2.append(aux2)

    col2, col1 = zip(*sorted(zip(col2, col1)))

    for i in range(len(col1)):
        sys.stdout.write("{},{}".format(col1[i], col2[i]))