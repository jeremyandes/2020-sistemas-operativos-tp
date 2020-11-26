import Parametros
import CargaTxt
import ordenaListas
import Resultados
from RoundRobin import round_robin
from termcolor import colored
from FIFO import algoritmo_fifo
from Threads_FIFO import CreaThreads
from PrioridadesDesalojo import prioridadesDesalojo
from PrioridadesSinDesalojo import prioridadesSinDesalojo
from PrimeroMasCorto import primeroMasCorto

parser=Parametros.definicion_params()
(options, args) = parser.parse_args()#Almacena los parametros del sistema en los atributos de options
Parametros.comprueba_params(options)#Contiene System.exit(), puede finalizar el programa
Procesos = CargaTxt.CargaArchivo(options.filename)#Carga la lista de procesos desde el archivo
Procesos = ordenaListas.OrdenaPor(1,Procesos)#Ordena la lista de procesos por orden de llegada
#procesador.iniciaProcesador(Procesos)#Muestra la carga de los procesos
nomArch=input("Que nombre desea ponerle al archivo en el que se guardan los resultados de la simulacion? ")
print("\n")
if options.algoritmo== "FIFO" :
    if options.hilo != 1:
        #Ejecuta algoritmo FIFO con varios hilos, parametros(options.hilo, procesos)
        print(colored("Se ejecuta FIFO multihilo...", "magenta"))
        terminados = CreaThreads(options.hilo, Procesos)
    else:
        #Ejecuta algoritmo FIFO con un hilo, parametro(procesos)
        print(colored("Se ejecuta FIFO un hilo...","magenta"))
        terminados = algoritmo_fifo(Procesos)
elif options.algoritmo=="SJF" :
    #Ejecuta algoritmo SJF, parametro(procesos)
    print(colored("Se ejecuta primero el mas corto...", "magenta"))
    terminados=primeroMasCorto(Procesos)
elif options.algoritmo=="PR"  : 
    #Ejecuta algoritmo de prioridades, parametro(procesos)
    desalojo=int(input("Como desea ejecutar el algoritmo de prioridades: 1- con desalojo. 2- sin desalojo "))
    while desalojo != 1 and desalojo != 2 :
        print("Entrada incorrecta, elija una opcion valida.")
        desalojo=input("Como desea ejecutar el algoritmo de prioridades: 1- con desalojo. 2- sin desalojo ")
    if desalojo == 1 :
        print(colored("Se ejecuta prioridades con desalojo...", "magenta"))
        terminados= prioridadesDesalojo(Procesos)
    else:
        print(colored("Se ejecuta prioridades sin desalojo...", "magenta"))
        terminados= prioridadesSinDesalojo(Procesos)
elif options.algoritmo=="RR":
    #Ejecuta algoritmo round robin, param(options.quantum, procesos)
    print(colored("Se ejecuta round robin...", "magenta"))
    terminados=round_robin(Procesos, options.quantum)
print(colored("Ejecucion finalizada...\n", "magenta"))
#se muestran los resultados de las imulacion a nivel proceso
Resultados.muestra_result(terminados)
#Se calculan los resultados de la simulacion a nivel sistema
promTurna = Resultados.promedio_turnaround(terminados)
esptotal = Resultados.espera_total(terminados)
promrta = Resultados.promedio_respuesta(terminados)
promtrabajos= Resultados.promedio_trabajos(terminados)
#se muestran los resultados de la sumulacion a nivel sistema
Resultados.muestra_sisresult(promTurna,esptotal, options.hilo , promrta, promtrabajos)
#se guardan los resultados de la simulacion en un archivo de salida
print(colored("Escribiendo resultados en archivo...", "magenta"))
Resultados.escribe_archivo(nomArch, terminados, promTurna, esptotal, options.hilo , promrta, promtrabajos)