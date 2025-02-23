class Tamagotchi:

   def __init__(self, nombre, color, salud=100,felicidad=50, energia=50):# Puedes colocar valores default para salud, felicidad y energía
      self.nombre= nombre
      self.color=color
      self.salud=salud
      self.felicidad= felicidad
      self.energia= energia
   
   def jugar (self):
      self.salud -= 15 ; self.felicidad += 20 ; self.energia -=10  

   def comer(self):   
      self.felicidad+=5 ; self.salud+=10 ; self.energia -= 10

   def curar(self):
      self.felicidad-=15 ; self.salud+=20 ; self.energia += 5

#nombre=["Marutchi","Tamatchi","Pochitchi"]
#color=["amarillo","rojo","verde"]


