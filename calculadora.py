class Calculadora :
    def __init__ (self,numero1,numero2):
        self.numero1=numero1
        self.numero2=numero2

    def sumar (self):
        try:
            g=self.numero1+self.numero2
            print("la suma de {} y {} es : {}".format(self.numero1,self.numero2,g))
        except TypeError:
            print("Tipo de dato debe ser numerico")
        except:
            print("Error al sumar")

    def restar (self):
        try:
            p=self.numero1-self.numero2
            print("la resta de {} y {} es : {}".format(self.numero1,self.numero2,p))
        except TypeError:
            print("Tipo de dato debe ser numerico")
        except:
            print("Error al restar")

    def multiplicar (self):
        try:
            e=self.numero1*self.numero2
            print("la multiplicacion de {} y {} es : {}".format(self.numero1,self.numero2,e))
        except TypeError:
            print("Tipo de dato debe ser numerico")
        except:
            print("Error al multiplicar")

    def dividir (self):
        try:
            t=self.numero1/self.numero2
            print("la division de {} y {} es : {}".format(self.numero1,self.numero2,t))
        except ZeroDivisionError:
            print("No se puede dividir entre cero")
        except TypeError:
            print("Tipo de dato debe ser numerico")
        except:
            print("Error al dividir")

    def sacar_exponente (self):
        try:
            s=self.numero1**self.numero2
            print("el exponente de {} y {} es : {}".format(self.numero1,self.numero2,s))
        except TypeError:
            print("Tipo de dato debe ser numerico")
        except:
            print("Error al sacar el exponente")