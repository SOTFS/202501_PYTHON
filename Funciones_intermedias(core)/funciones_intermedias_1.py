#1  Actualiza los valores en diccionarios y listas
matriz = [ [10, 15, 20], [3, 7, 14] ]

#Cambia el valor de 3 en matriz por 6. Una vez realizado el cambio tu matriz debería ser: [ [10, 15, 20], [6, 7, 14] ]
matriz[1][0]=6
print(matriz)

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes [0]["nombre"]= "Enrique martin Morales"
print(cantantes[0])


ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}
#En ciudades, cambia “Cancún” por “Monterrey”

ciudades ["México"][2]= "Monterey"
print(ciudades["México"])


coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]
#En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0]["latitud"]= 9.9355431
print(coordenadas[0])

#2 Crea la función iterarDiccionario(lista)


cantantes2 = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"},

   {"nombre": "José José", "pais": "México"},

   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}

]


def iterarDiccionario(lista):
   for diccionario in lista:
      for llave, valor in diccionario.items():
         print(f"- {llave} - {valor}")

iterarDiccionario(cantantes2)

#3. Obtener valores de una lista de diccionarios

dic1 = {
    "nombre": "Argentina",
    "capital": "Buenos Aires",
    "independencia": 1816
}

dic2 = {
    "nombre": "Paraguay",
    "capital": "Asunción",
    "independencia": 1811 
}
listas= [dic1, dic2]

def iterarDiccionario2(llave, lista):
   for diccionario in lista:
      if llave in diccionario:
         print(diccionario[llave])

iterarDiccionario2("nombre", listas)


#4. Iterar a través de un diccionario con valores de lista

paraguay = {
   "ciudades": ["Asunción", "Encarnación", "Pilar", "Villarrica"],
   "comidas": ["sopa paraguaya", "chipa", "reviro", "soyo"]
}

def imprimirInfo(diccionario):
   for llave, valor in diccionario.items():
      print(f"{len(valor)} {llave.upper()}")
      for i in valor:
         print(i)
imprimirInfo(paraguay)