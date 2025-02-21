
class TarjetaCredito:

   #Incluye en este método valores por default
   nuevas_tarjetas= []
   def __init__(self, saldo_pagar, limite_credito, intereses):
      self.saldo_pagar = saldo_pagar
      self.limite_credito = limite_credito
      self.intereses = intereses
      TarjetaCredito.nuevas_tarjetas.append(self)
      #TU CODIGO (Aquí va los atributos de instancia y sus asignaciones de valor)

   def compra(self, monto):
      if monto <= self.limite_credito -self.saldo_pagar:
         self.saldo_pagar += monto
      else:
         print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
      return self

   def pagar_saldo(self, monto):
      self.saldo_pagar -= monto 
      return self



   def mostrar_info_tarjeta(self):
      print("saldo a pagar:", self.saldo_pagar)
      return self       



   def cobrar_interes(self):
      self.saldo_pagar += self.saldo_pagar * self.intereses
      return self


credito1= TarjetaCredito(0,4000,0.020)
credito2= TarjetaCredito(0,5000,0.025)
credito3= TarjetaCredito(0,3000,0.015)

credito1.compra(700).compra(1000).pagar_saldo(950).cobrar_interes().mostrar_info_tarjeta()

credito2.compra(2000).compra(2500).pagar_saldo(4300).compra(500).pagar_saldo(600).cobrar_interes().mostrar_info_tarjeta()
credito3.compra(400).compra(1500).compra(600).compra(400).compra(500).cobrar_interes().mostrar_info_tarjeta()











