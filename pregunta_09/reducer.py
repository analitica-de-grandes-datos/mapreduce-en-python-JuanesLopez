#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from typing import final
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

    finaldb = sorted(db, key = lambda item: item[2])
    finaldb = finaldb[:6]

    for line in finaldb:
        sys.stdout.write("{}   {}   {}\n".format(line[0], line[1], line[2]))