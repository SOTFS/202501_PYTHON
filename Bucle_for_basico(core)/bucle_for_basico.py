#1. Básico
for i in range (1, 101):
    print(i)

#2. Múltiples de 2
for i in range (1, 501):
    if i%2==0:
        print(i)


#3. Contando Vanilla Ice
for i in range (1, 101):
    if i%10==0:
        print("baby")
    elif i%5==0:
        print("ice ice")

#4. Wow. Número gigante a la vista
cont=0
for i in range (1, 500001):
    cont= cont + i
print(cont)

#5. Regrésame al 3
for i in range (2025, 0, -3):
    print(i)

#6. Contador dinámico

numInicial= 15
numFinal= 88
multiplo=7
for i in range (numInicial, numFinal):
    if i%multiplo==0:
        print(i)