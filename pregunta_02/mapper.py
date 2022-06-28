#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    db = [line.split(',') for line in sys.stdin]
    purposes = [db[i][3] for i in range(len(db))]
    amounts = [db[i][4] for i in range(len(db))]

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
    for i in range(len(purposes)):

            #
            # escribe al flujo estandar de salida
            #
        sys.stdout.write("{}\t{}\n".format(purposes[i], amounts[i]))