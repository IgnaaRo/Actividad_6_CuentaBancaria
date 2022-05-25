class Cuenta():
  def __init__(self,titular="Ignacio",cantidad=0):
    self.titular=titular
    self.cantidad=cantidad
  
  def mostrar(self):
    print("Titular:", self.titular)
    print("Cantidad de dinero:", self.cantidad)
  
  def ingresar(self,cantidad):
    self.cantidad+=cantidad
    print("Se ingreso de dinero: ",cantidad,"en total tenes de dinero:",self.cantidad,"Pesos")
  
  def retirar(self,cantidad):
    self.cantidad-=cantidad
    print("Se retiro de dinero:",cantidad,"el dinero total es:",self.cantidad,"Pesos")
    
cuenta1=Cuenta("Ignacio",3000)
cuenta1.mostrar()
cuenta1.ingresar(1000)
cuenta1.retirar(500)
print(cuenta1)