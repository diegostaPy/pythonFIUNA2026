def validar ():
    n=float(input())
    while(not (int(n)==n) or n<=0):
        n=float(input())
    return int(n)    
    
def codificar(N):
    Ns=str(N)
    Nc=""
    for i in range(len(Ns)):
        Nc+=str((int(Ns[i])+7)%10)
    return Nc


# Se completa el tipo de variable de retorno y el codigo de la funión
# tipo de variable de retorno */codificado(int n):
#escriba su codigo
N=validar()
Nc=codificar(N)
print(Nc)
