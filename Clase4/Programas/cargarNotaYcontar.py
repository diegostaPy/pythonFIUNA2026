N=float(input())
while(N<0 or not(N==int(N)) ):
    N=float(input("Ingrese un numero entero y positivo"))
print(f"Se van a cargar {int(N)} notas")
N=int(N)
notas=[]
for i in range(N):
    nota=float(input(f"Ingrese la nota del estudiante {i+1}:"))
    while(nota<0 or nota>100):
        nota=float(input(f"Ingrese nuevamente la nota del estudiante {i+1}:"))
    
    
    notas.append(nota)
    

print(notas)
suma=0
for nota in notas:
    suma=suma+nota
promedio=suma/N
contar=0
for nota in notas:
    if nota<promedio:
        contar=contar+1
print(f"El promedio de las notas es {promedio} y {contar} estudiantes tienen puntaje menor al promedio")