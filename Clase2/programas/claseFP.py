"""
a="hola"
print(type(a))
print(a[0])    
b=a[::-1]
print(b)

# la cadena a es un palindromo?
print(a==b)

numero=input("Cargar un entero: ")

print(numero.isdigit())

if numero.isdigit():
    num=int(numero)
    print("El número ingresado al cuadrado es ",num**2)
else:
    print("No se ingreso un número")

    
import math
print(math.pi)
print(f" Pi con tres decimales es {math.pi:.3f}")
print(" Pi con tres decimales es %f" % math.pi)
    """
print(len("hola"))
