
#Crea la función multiplica_por_dos(num)

valor = int(input("Ingresa un número: "))

def multiplica(entero):
    lista = []
    for i in range(entero + 1): 
        mul = i * 2
        lista.append(mul)
    return lista

print(multiplica(valor))

#  Crea la función suma_y_resta(lista)
num1 = int( input ("dame dos numeros"))
num2 = int(input ("ahora el otro"))
lista2 = [num1,num2]
def suma_y_resta(lista2):
    suma = lista2[0] + lista2[1]
    resta = lista2[0] - lista2[1]
    print(suma)
    return resta
print (suma_y_resta(lista2))


# Crea la función sumatoria_menos_longitud(lista)
def longitud (lista3):
    sum=0
    for i in (lista3):
        sum= sum+ i
    return (sum)
lista3= [1,2,5,7,9]
print (longitud(lista3) - len(lista3))



#Crea la función valores_multiplicados_segundo(lista)
lista4 =[4,3,9,5,1]
def multi(list):
    if len(lista4) <= 2:
        print(len(list))
        newlist=[]
    for i in list:
        newlist.append (i * lista4[1])
    print(len(list))
    return(newlist)

print(multi(lista4))




#Crea la función valor_multiplicado_longitud(valor, longitud)

nume1 = int( input ("dame un numero"))
nume2 = int( input ("ahora el otro"))

def valor_por_long (num, num2):
    lista= []
    for i in range(num2):
        lista.append (num*num2)
    return(lista)
print (valor_por_long(nume1,nume2))


paraguay = {

   "ciudades": ["Asunción", "Encarnación", "Pilar", "Villarrica"],

   "comidas": ["sopa paraguaya", "chipa", "reviro","soyo"]

}

def imprimirInfo(paraguay):
    for llave, valor in paraguay.items():  # Se debe indicar el diccionario
        print(f"{len(valor)} {llave.upper()}")
        for i in valor:
            print(i)

imprimirInfo(paraguay)