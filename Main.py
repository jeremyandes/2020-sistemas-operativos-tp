import Parametros
import CargaTxt
import ordenaListas
import procesador
from RoundRobin import round_robin
from termcolor import colored
from Resultados import muestra_result
from Resultados import escribe_archivo
from FIFO import algoritmo_fifo
from Threads_FIFO import CreaThreads
#importar archivos de cada algoritmo


parser=Parametros.definicion_params()
(options, args) = parser.parse_args()#Almacena los parametros del sistema en los atributos de options
Parametros.comprueba_params(options)#Contiene System.exit(), puede finalizar el programa
Procesos = CargaTxt.CargaArchivo(options.filename)#Carga la lista de procesos desde el archivo
Procesos = ordenaListas.OrdenaPor(1,Procesos)#Ordena la lista de procesos por orden de llegada
#procesador.iniciaProcesador(Procesos)#Muestra la carga de los procesos

if options.algoritmo== "FIFO" :
    if options.hilo != 1:
        #Ejecuta algoritmo FIFO con varios hilos, parametros(options.hilo, procesos)
        print(colored("Se ejecuta FIFO varios hilos", "magenta"))
        CreaThreads(options.hilo, Procesos)
    else:
        #Ejecuta algoritmo FIFO con un hilo, parametro(procesos)
        print(colored("Se ejecuta FIFO un hilo","magenta"))
        terminados = algoritmo_fifo(Procesos)
elif options.algoritmo=="SJF" :
    #Ejecuta algoritmo SJF, parametro(procesos)
    print(colored("Se ejecuta primero el mas corto", "magenta"))
elif options.algoritmo=="PR"  : 
    #Ejecuta algoritmo de prioridades, parametro(procesos)
    print(colored("Se ejecuta prioridades", "magenta"))
elif options.algoritmo=="RR":
    #Ejecuta algoritmo round robin, param(options.quantum, procesos)
    print(colored("Se ejecuta round robin", "magenta"))
    terminados=round_robin(Procesos, options.quantum)
    muestra_result(terminados)
nomArch=input("Que nombre desea ponerle al archivo en el que se guardan los resultados de la simulacion?")
escribe_archivo(nomArch, terminados)
#imprimir resultados a nivel sistema


