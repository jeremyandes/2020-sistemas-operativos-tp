#Parametros del sistema
from optparse import OptionParser
import sys

#Funcion que devuelve el nombre del algoritmo segun la sigla
def switch_algoritmo(argument):
    switcher = {
        "FIFO": "First in First out",
        "SJF" : "Primero el mas corto",
        "PR"  : "Prioridades",
        "RR"  : "Round Robin"
    }
    return switcher.get(argument, "entrada invalida")

#Definicion de los flags 
def definicion_params():
    usage= "usage: %prog -f <archivo> -a <algoritmo> [-q <quantum>] [-t <hilos>]"           #indicacion del correcto uso del programa
    parser=OptionParser(usage=usage)
    parser.add_option("-a","--algoritmo", choices=["FIFO","SJF","PR","RR"],
                help="Escriba el algoritmo de scheduling de procesador")
    parser.add_option("-q", "--quantum", action="store", type="int", dest="quantum", default=2,
                help="Especifique la duracion del quantum en segundos")
    parser.add_option("-t","--thread", action="store", type="int", dest="hilo", default=1,
                help="indique la cantidad de hilos")
    parser.add_option("-f","--filename",action="store",dest="filename",
                help="Escriba el nombre del achivo de texto")
    return parser

#Comprobando que ingresaron correctamente, (Algunas lineas son provisorias)
def comprueba_params(options):
    al=options.algoritmo
    #Si no se ingreso el nombre del archivo, termina el programa con un mensaje indicando la razon
    if options.filename==None :
        sys.exit("<< ERROR: Debe indicar el nombre del archivo a utilizar >>".center(20))
    else:
        pass
    #Si no se ingreso tipo de algortimo, termina el programa con un mensaje indicando la razon
    if al==None :
        sys.exit("<< ERROR: Debe indicar el algoritmo a utilizar >>".center(20))
    if options.hilo != 1 and al != "FIFO":
        sys.exit("<< ERROR: No está permitido el uso de threads en algoritmos que no sean FIFO >>")
    if options.hilo < 1 and al == "FIFO":
        sys.exit("<< ERROR: El numero de threads debe ser mayor o igual a 1 >>")
    if options.quantum != 2 and al != "RR":
        sys.exit("<< ERROR: No está permitido el uso de quantums en algoritmos que no sean Round Robin >>")
    
"""
    else:
        print("El algorimo elegido fue ", switch_algoritmo(al))
    if al == 'RR':
        print("El quantum es de ", options.quantum)
    else:
        pass

    if al== "FIFO" or al=="SJF" or al=="PR" :
        if options.hilo==None :
            print("No se especifico la cantidad de hilos a utilizar, se utilizara 1 hilo por defecto")
        else:
            print("Se utilizaran {} hilos".format( str(options.hilo) )) """

