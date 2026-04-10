N=float(input("Ingrese un número: "))
while(not(int(N)==N) or N<0 or N>10000):
    print("Número no válido. Ingrese un número entero positivo.")
    N=float(input("Ingrese un número: "))
N=int(N)
numeroConMayorCantidadUnosSeguidos=0
cantidadUnosSeguidosMayor=0
for i in range(1,N+1):
    print(f"Cargar el {i} ", end="")
    ai=float(input("Ingrese el número: "))
    while(not(int(ai)==ai) or ai<0 or ai>10000):
        print("Número no válido. Ingrese un número entero positivo.")
        ai=float(input("Ingrese un número: "))
    ai=int(ai)
    a=ai
    j=0
    cantidadUnosSeguidos=1
    while ai>0:
        digito=ai%2
        ai=ai//2
        j=j+1
        if(j>=2):
            if digito ==1 and digitoAnterior==1:
                cantidadUnosSeguidos=cantidadUnosSeguidos+1
        digitoAnterior=digito
    if(i==1):
        numeroConMayorCantidadUnosSeguidos=a
        cantidadUnosSeguidosMayor=cantidadUnosSeguidos
    if(cantidadUnosSeguidos>cantidadUnosSeguidosMayor):
        numeroConMayorCantidadUnosSeguidos=a
        cantidadUnosSeguidosMayor=cantidadUnosSeguidos
    print(numeroConMayorCantidadUnosSeguidos,cantidadUnosSeguidosMayor)
    print(f"Cantidad de unos seguidos: {cantidadUnosSeguidos}")
print(f"El número con mayor cantidad de unos seguidos es: {numeroConMayorCantidadUnosSeguidos} con {cantidadUnosSeguidosMayor} unos seguidos.")

