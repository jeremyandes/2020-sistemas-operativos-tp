#Parametros del sistema
from optparse import OpcionParser
'''Algoritmo de scheduling de procesador (FCFS, SJF sin desalojo,
 Prioridades sin desalojo, Round Robin).
Valor del Quantum (si el algoritmo de scheduling de procesador 
lo requiere). Se mide en segundos. 
Cantidad de threads (opcionalmente se podrán ejecutar utilizando 
múltiples thread), esto sólo está disponible para FCFS y SJF y 
Prioridades.
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")
action="store", type="string"
(options, args) = parser.parse_args()'''

parser=OptionParser()
parser.add_option("-a","--algoritmo", action="store", type="string", dest="algoritmo",
            choices=["FIFO","SJF","PR","RR"],
            help="Escriba el algoritmo de scheduling de procesador"
parser.add_option("-q", "--quantum", action="store", type="int", dest="quantum", default=2,
            help="Especifique la duracion del quantum en segundos")
parser.add_option("-t","--thread", action="store_true", dest="hilo", default="false",
            help="indique la cantidad de hilos")
(options, args) = parser.parse_args()

if options.algoritmo==None
    print("Debe indicar el algoritmo a utilizar")
else:
    print("El algorimo elegido fue")
    switch_algoritmo(options.algoritmo)

def switch_algortimo(argument):
    switcher = {
        "FIFO": "First in First out",
        "SJF": "Primero el mas corto",
        "PR": "Prioridades",
        "RR": "Round Robin",
    }
    print switcher.get(argument, "entrada invalida")
