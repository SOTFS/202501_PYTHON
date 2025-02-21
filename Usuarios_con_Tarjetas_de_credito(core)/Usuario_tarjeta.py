from Tarjeta_de_credito2 import TarjetaCredito

class Usuario:

    def __init__(self, nombre, apellido, email, saldo_inicial, limite_credito, intereses):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.tarjeta = TarjetaCredito(saldo_pagar=saldo_inicial, limite_credito=limite_credito, intereses=intereses)

    def hacer_compra(self, monto):
        if self.tarjeta.compra(monto):
            return f"La compra de {self.nombre} fue de: {monto}$"
        return ""
    def pagar_tarjeta(self, monto):
        resultado = self.tarjeta.pagar_saldo(monto)
        if resultado:
            return f"{self.nombre} hizo un pago de: {monto}$"
        return f"el pago de {self.nombre} excede la deuda. Tu deuda actual es: {self.tarjeta.saldo_pagar}"
    def mostrar_saldo_usuario(self):
        return f"Tarjeta de {self.nombre}= {self.tarjeta.mostrar_info_tarjeta()}"


miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@skillnest.la", 0, 4000, 0.010)
daniel = Usuario("Daniel", "Larusso", "daniel@skillnest.la", 0, 7000, 0.15)
yo = Usuario("Ale", "Bordon", "ale.@gmail.com", 0, 5000, 0.010)


print(miyagi.hacer_compra(180))
print(miyagi.hacer_compra(1100))
print(miyagi.hacer_compra(1100))
print(daniel.hacer_compra(1580))
print(daniel.hacer_compra(2050))
print(daniel.hacer_compra(11580))
print(yo.hacer_compra(700))
print(yo.hacer_compra(900))
print(yo.hacer_compra(800))

print(miyagi.pagar_tarjeta(2200))
print(daniel.pagar_tarjeta(2000))
print(yo.pagar_tarjeta(500))
print(daniel.pagar_tarjeta(2000))



miyagi.tarjeta.cobrar_interes()
daniel.tarjeta.cobrar_interes()
yo.tarjeta.cobrar_interes()

print(miyagi.mostrar_saldo_usuario())
print(daniel.mostrar_saldo_usuario())
print(yo.mostrar_saldo_usuario())

