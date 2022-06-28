#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#

if __name__ == '__main__':

    db=[]

    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        col1, col2, col3 = line.split(",")
        col3 = int(col3)
        aux = (col1, col2, col3)
        db.append(aux)

    finaldb = sorted(sorted(db, key = lambda item: item[2]), key = lambda item: item[0])

    for line in finaldb:
        sys.stdout.write("{}   {}   {}\n".format(line[0], line[1], line[2]))