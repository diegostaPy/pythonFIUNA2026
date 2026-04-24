def validarNumero():
    x=float(input())
    while(not(int(x)==x) or x<0 or x>10000):
        print("Número no válido. Ingrese un número entero positivo.")
        x=float(input("Ingrese un número: "))
    x=int(x)
    return x
def imprimirResultado(numeroConMayorCantidadUnosSeguidos,cantidadUnosSeguidosMayor):
    print(f"El número con mayor cantidad de unos seguidos es: {numeroConMayorCantidadUnosSeguidos} con {cantidadUnosSeguidosMayor} unos seguidos.") 

N=validarNumero()
numeroConMayorCantidadUnosSeguidos=0
cantidadUnosSeguidosMayor=0
for i in range(1,N+1):
    print(f"Cargar el {i} ", end="")
    ai=validarNumero()
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
imprimirResultado(numeroConMayorCantidadUnosSeguidos,cantidadUnosSeguidosMayor)
