import random
class Simulador:
    
    def __init__ (self,vehiculos):
        self.vehiculos=vehiculos
    def iniciar_simulacion (self,dias):
        for i in self.vehiculos:
            print ( "\n")
            print ("vehiculo {}".format(i.placa))
            if not i.motor.esta_encendido():
                i.motor.encender()
            for dia in range(1,dias+1):
                print ("------------")
                print ("dia#{}" .format(dia))
                print ("------------")
                distancia=random.randint(0,100)
                if not i.hay_combustible(distancia):
                    litros=random(30,60)
                    i.cargar_combustible(litros)
                i.recorrer_distancia(distancia)
            print(i.obtener_informe())