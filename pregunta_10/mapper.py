#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":

    #
    # itera sobre cada linea de codigo recibida
    # a traves del flujo de entrada
    #
    
    db = [line.replace('\n', '') for line in sys.stdin]
    db = [line.split('\t') for line  in db]
    col1 = [db[i][0] for i in range(len(db))]
    col2 = [db[i][1] for i in range(len(db))]

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
    for i in range(len(col1)):

            #
            # escribe al flujo estandar de salida
            #
        aux = col2[i].split(',')
        for reg in aux:
            sys.stdout.write("{}\t{}\n".format(reg.strip(), col1[i]))