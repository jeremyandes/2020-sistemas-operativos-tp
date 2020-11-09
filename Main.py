import Parametros
import CargaTxt
import ordenaListas
import procesador


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
        print("Se ejecuta FIFO varios hilos")
    else:
        #Ejecuta algoritmo FIFO con un hilo, parametro(procesos)
        print("Se ejecuta FIFO un hilo")
elif options.algoritmo=="SJF" :
    #Ejecuta algoritmo SJF, parametro(procesos)
    print("Se ejecuta primero el mas corto")
elif options.algoritmo=="PR"  :
    #Ejecuta algoritmo de prioridades, parametro(procesos)
    print("Se ejecuta prioridades")
elif options.algoritmo=="RR":
    #Ejecuta algoritmo round robin, param(options.quantum, procesos)
    print("Se ejecuta round robin")

