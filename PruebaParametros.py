#Parametros del sistema
from optparse import OptionParser

#Funcion que devuelve el nombre del algoritmo segun la sigla
def switch_algoritmo(argument):
    switcher = {
        "FIFO": "First in First out",
        "SJF" : "Primero el mas corto",
        "PR"  : "Prioridades",
        "RR"  : "Round Robin"
    }
    return switcher.get(argument, "entrada invalida")

#Definicion de las opciones
parser=OptionParser()
parser.add_option("-a","--algoritmo", choices=["FIFO","SJF","PR","RR"],
            help="Escriba el algoritmo de scheduling de procesador")
parser.add_option("-q", "--quantum", action="store", type="int", dest="quantum", default=2,
            help="Especifique la duracion del quantum en segundos")
parser.add_option("-t","--thread", action="store", type="int", dest="hilo", 
            help="indique la cantidad de hilos")
parser.add_option("-f","--filename",action="store",dest="filename",
            help="Escriba el nombre del achivo de texto")

#Almacena los parametros del sistema en los atributos de options
(options, args) = parser.parse_args()

#Comprobando que ingresaron correctamente, (lineas provisorias)
al=options.algoritmo
archivo=options.filename

if al==None :
    print("Debe indicar el algoritmo a utilizar")
else:
    print("El algorimo elegido fue ", switch_algoritmo(al))

if al == 'RR':
    print("El quantum es de ", options.quantum)
else:
    pass

if al== "FIFO" or al=="SJF" or al=="PR" :
    if options.hilo==None :
        print("No se especifico la cantidad de hilos a utilizar")
    else:
        print("Se utilizaran {} hilos".format( str(options.hilo) ))

