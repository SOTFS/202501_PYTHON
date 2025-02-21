numero1 = 70 #declaracion de  variable. tipo entero
numero2 = 3.14 # declaracion de variable. tipo flotante
booleano = False # declaracion de variable.tipo booleano
cadena = 'Hola Mundo'# declaracion de variable. tipo string
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] # declaracion de variable. tipo lista
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} # declaracion de variable. tipo diccionario
frutas = ('guayaba', 'fresa', 'papaya') # declaracion de variable. tipo tupla
print(type(frutas)) #imprimir el tipo de variable
print(ingredientes_pastel[2]) #imprimir elemento de una lista
ingredientes_pastel.append('Mantequilla') #agregar un valor a una lista
print(persona['nombre']) #imprimir valor de un diccionario
persona['nombre'] = 'Kevin' #cambiar valor de un diccionario
persona['color_ojos'] = 'cafe' #agregar un valor a un diccionario
print(frutas[2]) #imprimir valor de una tupla

if numero1 > 45:    #condicional if
    print("Numero mayor") #imprimir un strinig si se cumple la condicion
else:  #condicional else
    print("Numero menor") #imprimir un string si no se cumple la condicion

if len(cadena) < 5: #condicional if
    print("Cadena corta") #imprimir un string si se cumple la condicion
elif len(cadena) > 15: #condicional else if
    print("Cadena larga") #imprimir un string si se cumple la condicion
else: #condicional else
    print("Cadena perfecta") #imprimir un string si no se cumple la condicion

for x in range(8): #ciclo for inicio en 0  incremento de 1 
    print(x) #imprimir el valor de variable x
for x in range(2,8): #ciclo for inicio en 2 incremento de 1
    print(x) #imprimir el valor de variable x
for x in range(2,8,2): #ciclo for inicio en 2 incremento de 2
    print(x) #imprimir el valor de variable x
x = 0 #declaracion de variable
while(x < 8): #ciclo while 
    print(x) #imprimir el valor de variable x
    x += 1 #incremento de variable x

ingredientes_pastel.pop() #eliminar el ultimo elemento de una lista
ingredientes_pastel.pop(1) #eliminar un elemento de una lista

print(persona) #imprimir un diccionario
persona.pop('color_ojos') #eliminar un elemento de un diccionario
print(persona) #imprimir un diccionario

for ingrediente in ingredientes_pastel: #ciclo for para recorrer una lista
    if ingrediente == 'Harina': #condicional if
        continue #salto a la siguiente iteracion
    print('Después de la primera sentencia') #imprimir un string
    if ingrediente == 'Chocolate': #condicional if
        break #terminar el ciclo

def imprime_hola_10_veces(): #declaracion de una funcion
    for numero in range(10): #ciclo for
        print('Hola') #imprimir un string

imprime_hola_10_veces() #llamada a una funcion

def imprime_hola_n_veces(n): #declaracion de una funcion con argumento n
    for numero in range(n): #ciclo for
        print('Hola') #imprimir un string

imprime_hola_n_veces(5) #llamada a una funcion con argumento 5

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)