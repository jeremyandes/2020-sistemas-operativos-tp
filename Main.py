import Parametros
import CargaTxt
import ordenaListas
import procesador
import Resultados
from RoundRobin import round_robin
from termcolor import colored
from Prioridades import prioridades
from FIFO import algoritmo_fifo

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
    else:
        #Ejecuta algoritmo FIFO con un hilo, parametro(procesos)
        print(colored("Se ejecuta FIFO un hilo","magenta"))
        terminados = algoritmo_fifo(Procesos)
    turna = 0
    cola = 0
    esptot = 0
    rta = 0
    cpu = 0
elif options.algoritmo=="SJF" :
    #Ejecuta algoritmo SJF, parametro(procesos)
    print(colored("Se ejecuta primero el mas corto", "magenta"))
elif options.algoritmo=="PR"  :
    #Ejecuta algoritmo de prioridades, parametro(procesos)
    print(colored("Se ejecuta prioridades", "magenta"))
    prioridades(Procesos)
elif options.algoritmo=="RR":
    #Ejecuta algoritmo round robin, param(options.quantum, procesos)
    print(colored("Se ejecuta round robin", "magenta"))
    terminados=round_robin(Procesos, options.quantum)
    turna = 6
    cola = 7
    esptot = 7
    rta = 5
    cpu = 4
Resultados.muestra_result(terminados, turna, cola, esptot, rta, cpu)
'''Tiempo de Turnaround Promedio de los procesos en el sistema. Se mide en segundos.
Tiempo de Espera Total de los procesos en el sistema. Se mide en segundos.
Tiempo de Respuesta Promedio de los procesos en el sistema. Se mide en segundos.
Cantidad promedio de trabajos finalizados por cada 1000 segundos.
Cantidad de threads utilizados (si corresponde).'''
#Se calculan los resultados de la simulacion a nivel sistema
promTurna = Resultados.promedio_turnaround(terminados, turna)
esptotal = Resultados.espera_total(terminados, esptot)
Resultados.muestra_sisresult(promTurna,esptotal)
Resultados.escribe_archivo(nomArch, terminados, turna, cola, esptot, rta, cpu)


