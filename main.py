from motor import Motor
from vehiculo import Vehiculo
from simulador import Simulador

motor1 = Motor ("45637",1000)
motor2 = Motor ("3578",3679)

familiar = Vehiculo ("4241MJM","azul","Toyota","2015","gasolina",1100,53.1,"SI")
deportivo = Vehiculo ("4040JHM","amarillo","Suzuki","2019","gasolina",1000,47.1,"SI")
grande = Vehiculo ("3745JOE","negro","Nissan","2010","diesel",1145,57.3,"NO")

deportivo.poner_motor(motor1)
familiar.poner_motor(motor2)
grande.poner_motor(motor1)

vehiculos=[familiar,deportivo,grande]

s=Simulador(vehiculos)

s.iniciar_simulacion(2)