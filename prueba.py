#clase "Proceso"
#campo = "valor posible" // pID = >1 && <9999 // tda = >0 && <99999 segundos // pdp = >1 && <15 // tdp = >0 && <9999 segundos
class Proceso:
    def __init__(self):
        self.campo = ""
        self.pID = -1
        self.tda = -1
        self.pdp = -1
        self.tdp = -1
    def muestra(self):
        return '{}, {}, {}, {}, {}'.format(self.campo,self.pID,self.tda,self.pdp,self.tdp)

class ListaProcesos(list): 

    f = open ("procesos.txt", "r")#El nombre del archivo pasa por param

    def __init__(self, nomarchivo):
        for linea in self.f:
            self.append(self.setProceso(linea))

    def setProceso(self, linea): #Esto no es un setProceso jajaja
        datos = linea.split(".")
        procesoNuevo = Proceso()
        procesoNuevo.pID = datos[0]
        procesoNuevo.tda = datos[1]
        procesoNuevo.pdp = datos[2]
        procesoNuevo.tdp = datos[3]
        return procesoNuevo

    def getProcesos(self):
        for obj in self:
            # print(obj.pID, obj.tda, obj.pdp, obj.tdp)
            print("pID: {}\ntda: {}\npdp: {}\ntdp: {}\n-----------------------------------"
            .format(obj.pID, obj.tda, obj.pdp, obj.tdp))
            print("-----------------------------------\n")