#sublibrería "path" de la librería "os"
import os.path

def CargaListas():
    #usando la librería "os", invoco la función "listdir" que retorna todos los nombres de archivos en una lista
    archivos = os.listdir('ListasProcesos/')
    
    #retorno la lista resultante
    return archivos
