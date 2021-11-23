""" 4. Escrever um algoritmo que leia uma quantidade números inseridos pelo usuário e conte quantos delesestão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deveterminar quando for lido um número negativo."""
n = int(input("Quantos números você quer analisar: "))
i = 0
num_0_25 = 0
num_26_50 = 0
num_51_75 = 0
num_76_100 = 0
while i < n:
    numero = int(input("Insira um número inteiro:"))
    i = i + 1
    if numero < 0:
        print('Valor Inválido!!!!!')
    else:
        if(numero >= 0) and (numero <= 25):
            num_0_25 += 1

        elif (numero >= 26) and (numero <= 50):
            num_26_50 += 1

        elif (numero >= 51) and (numero <= 75):
            num_51_75 += 1

        elif (numero >= 76) and (numero <= 100):
            num_76_100 += 1
        else:
            pass

print(f"Foram lidos {num_0_25} números entre [0-25]")
print(f"Foram lidos {num_26_50} números entre [26-50]")
print(f"Foram lidos {num_51_75} números entre [51-75]")
print(f"Foram lidos {num_76_100} números entre [76-100]")
