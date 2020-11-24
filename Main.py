import Parametros
import CargaTxt
import ordenaListas
import procesador
import Resultados
from RoundRobin import round_robin
from termcolor import colored
from FIFO import algoritmo_fifo
from Threads_FIFO import CreaThreads
#importar archivos de cada algoritmo


parser=Parametros.definicion_params()
(options, args) = parser.parse_args()#Almacena los parametros del sistema en los atributos de options
Parametros.comprueba_params(options)#Contiene System.exit(), puede finalizar el programa
Procesos = CargaTxt.CargaArchivo(options.filename)#Carga la lista de procesos desde el archivo
Procesos = ordenaListas.OrdenaPor(1,Procesos)#Ordena la lista de procesos por orden de llegada
#procesador.iniciaProcesador(Procesos)#Muestra la carga de los procesos
nomArch=input("Que nombre desea ponerle al archivo en el que se guardan los resultados de la simulacion? ")
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
'''
#se muestran los resultados de las imulacion a nivel proceso
Resultados.muestra_result(terminados)
#Se calculan los resultados de la simulacion a nivel sistema
promTurna = Resultados.promedio_turnaround(terminados)
esptotal = Resultados.espera_total(terminados)
promrta = Resultados.promedio_respuesta(terminados)
#se muestran los resultados de la sumulacion a nivel sistema
Resultados.muestra_sisresult(promTurna,esptotal, options.hilo , promrta)
#se guardan los resultados de la simulacion en un archivo de salida
Resultados.escribe_archivo(nomArch, terminados)'''




