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
    db = [line.split('   ') for line  in db]
    letras = [db[i][0] for i in range(len(db))]
    valores = [db[i][2] for i in range(len(db))]

        #
        # genera las tuplas palabra \tabulador 1
        # ya que es un conteo de palabras
        #
    for i in range(len(letras)):

            #
            # escribe al flujo estandar de salida
            #
        sys.stdout.write("{}\t{}\n".format(letras[i], valores[i]))