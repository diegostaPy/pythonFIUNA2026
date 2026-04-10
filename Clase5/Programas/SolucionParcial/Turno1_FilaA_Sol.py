print("\033c") #para resetear el terminal de VSCode

# Validación de N
N = float(input("Ingrese el valor de N: "))
while N!=int(N) or N<=0 or N>10000:
    N = float(input("Ingrese el valor de N: "))
N = int(N)

# Validación y proceso con los N números
total_1_max = 0
resp = 0
for i in range(N):
    #Validación del i número ingresado
    x = float(input(f"Ingrese el valor {i}: "))
    while x!=int(x) or x<=0 or x>10000:
        x = float(input(f"Ingrese el valor {i}: "))
    x = int(x)
    #Obtenemos los bits y contamos la cantidad de 1's
    cont = 0
    y = x
    while y>0:
        d = y%2
        y = y//2
        if d==1:
            cont+=1
    #Actualizamos la respuesta (si corresponde)
    if cont>total_1_max:
        total_1_max = cont
        resp = x

#Impresión del resultado
print(f"{resp} -> {total_1_max}")