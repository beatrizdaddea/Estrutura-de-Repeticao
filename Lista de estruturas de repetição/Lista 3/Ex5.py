"""5. Escreva  um  programa  que  leia  um  conjunto  de  inteiros  e,  em  seguida,  imprima  a  soma  dos inteiros pares e ímpares. """

tela_resp = str(input("Deseja realizar um calculo? (Responda com: Sim / Nao): "))
Soma = 0
S_par = 0
S_impar = 0

while (tela_resp == "Sim"):
    n = int(input("Insira um número inteiro: "))
    if (n % 2 == 0):
        S_par = S_par + n
    else:
        S_impar = S_impar + n
    Soma = S_par + S_impar
    tela_resp = (str(input("Deseja continuar no programa? ")))
else:
    pass

print("Soma de todos os elementos = ", Soma)
print("Soma dos elementos pares = ", S_par)
print("Soma dos elementos ímpares = ", S_impar)
