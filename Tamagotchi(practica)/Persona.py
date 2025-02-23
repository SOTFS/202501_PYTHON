from Tamagotchi import Tamagotchi
class Persona:
   def __init__(self, nombre, apellido,tamagotchi_nombre, tamagotchi_color):
      self.nombre= nombre
      self.apellido= apellido
      self.tamagotchi= Tamagotchi(nombre=tamagotchi_nombre, color= tamagotchi_color)

   def jugar_con_tamagotchi (self):
      self.tamagotchi.jugar()
      print (f"jugando con {self.tamagotchi.nombre} en proceso...")
      print (f"{self.tamagotchi.nombre} aumento la felicidad a: {self.tamagotchi.felicidad}, su salud disminuyo a: {self.tamagotchi.salud}. La energia restante es: {self.tamagotchi.energia}")


   def darle_comida(self):
      self.tamagotchi.comer()
      print(f"alimentando a {self.tamagotchi.nombre} en proceso...")
      print (f"{self.tamagotchi.nombre} de {self.nombre }, incremento la salud a: {self.tamagotchi.salud} e incremento la felicidad a: {self.tamagotchi.felicidad}. La energia restante es: {self.tamagotchi.energia}")
      
   def curarlo (self):  
      self.tamagotchi.curar()
      print( f"curando heridas de {self.tamagotchi.nombre} en proceso...")
      print (f"{self.tamagotchi.nombre} de {self.nombre}, incremento la salud a: {self.tamagotchi.salud} y disminuyo la felicidad a: {self.tamagotchi.felicidad}. La energia aumento a: {self.tamagotchi.energia}")
      
      
   def mostrar_color(self):
      print (f"El color de {self.tamagotchi.nombre} de {self.nombre} es: {self.tamagotchi.color}")

ale= Persona(nombre="Ale", apellido="Bordon", tamagotchi_nombre="Marutchi", tamagotchi_color="amarillo")
   #Métodos:

   #curarlo(): sana las heridas de su tamagotchi invocando al método de tamagotchi curar()
ale.jugar_con_tamagotchi()
ale.darle_comida()
ale.curarlo()
ale.mostrar_color()