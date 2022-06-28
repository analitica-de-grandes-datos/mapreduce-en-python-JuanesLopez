#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    db = [line.split('   ') for line in sys.stdin]
    col1 = [db[i][0] for i in range(len(db))]

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
    for reg in col1:

            #
            # escribe al flujo estandar de salida
            #
        sys.stdout.write("{}\t1\n".format(reg))