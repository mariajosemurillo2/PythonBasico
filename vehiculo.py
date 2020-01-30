class Vehiculo:
    DISTANCIA_BASE=12
    FACTOR_EMISION_GASOLINA=2.196
    FACTOR_EMISION_DIESEL=2.471
    def __init__ (self,placa,color,marca,modelo,combustible,km,tanque,AC):
        self.placa = placa
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.km = km
        self.tanque = tanque
        self.AC = AC
        self.encendido = True
        self.litros_consumidos=0

    def encender(self):
        if self.encendido == False :
            self.encendido = True
            print("el vehiculo a sido encendido")
        else :
            print ("el vehiculo ya esta encendido !")

    def apagar(self):
        if self.encendido == False :
            print("el vehiculo ya esta apagado !")
        else :
            self.encendido = True
            print ("el vehiculo a sido apagado ")

    def tocar_bocina(self):
        print ("muuuuu")

    def frenar(self):
        print ("frenando")

    def combustible(self):
        return (tanque)
    
    def mostrar_vehiculo(self):
        print ("La placa es "+self.placa)
        print ("el color es "+self.color)
        print ("la marca es "+self.marca)
        print ("el modelo es "+self.modelo)
        print ("el combustible que usa es "+self.combustible)
        print ("el km es "+str(self.km))
        print ("tanque "+str(self.tanque))
        print ("AC "+self.AC)

    def cargar_combustible(self,litros):
        self.tanque += litros
        print("Cargando combustible")

    def recorrer_distancia(self,distancia):
        variante = self.obtener_variante()
        if (self.encendido):
            if (distancia<(self.tanque*variante)):
                self.km+= distancia
                total_litros = round(distancia/ variante)
                self.litros_consumidos+=total_litros
                self.tanque-=total_litros
                print("recorriendo {} kilometros".format(distancia))
            else :
                print("No tiene suficiente combustible")
        else:
            print("El vehiculo esta apagado")

    def calcular_co2(self):
        if (self.combustible=="gasolina"):
            return self.FACTOR_EMISION_GASOLINA*self.litros_consumidos
        else :
            return self.FACTOR_EMISION_DIESEL*self.litros_consumidos

    def poner_motor(self,motor):
        self.motor = motor

    def obtener_variante(self):
        cilindrada = self.motor.obtener_cilindrada()
        if (cilindrada==1000):
            return 12
        elif (cilindrada==2000):
            return 10
        else :
            return 8

    def hay_combustible(self,distancia):
        variante = self.obtener_variante()
        if not distancia<(variante*self.tanque):
            return False
        else :
            return True

    def obtener_informe(self):
        informe ="\n----------"
        informe+="\n INFORMEFINAL-EMISIONCO2"
        informe+="\n----------"
        informe+="\n Ud esta conduciendo un vehiculo marca {}, modelo {},color {}".format(self.marca,self.modelo,self.color)
        informe+="\n Ha recorrido un total de {} km de distancia".format(self.km)
        informe+="\n Ha condumido un total de {} litros de {} ".format(self.litros_consumidos,self.combustible)
        informe+="\n En su tanque tiene {} litros de {}".format(self.tanque,self.combustible)
        informe+="\n Se envio a la atmosfera un total de {} kg de CO2".format(round(self.calcular_co2(),2))
        return informe
        