""" 6.Escreva um programa para imprimir todos os números Armstrong entre 1 e 500. Se a soma da cada dígito elevado a n, onde n é quantidade de dígitos que o número possui,for igual ao próprio número, então o número é chamado de número Armstrong.Por exemplo, 153 = (1 * 1 * 1) + (5 * 5 * 5) + (3 * 3 * 3)"""
num = 1
num_ = 500

for ordem in range(num, num_ + 1):
    n = len(str(ordem)) # O LEN É SÓ PARA ITENS ITERÁVEIS, POR ISSO COLOQUEI O STR PARA CONVERSÃO DO ELEMENTO
    cont = 0
    temp = ordem

    while temp > 0:
        digit = temp % 10 # MODULO DE DIVISAO
        cont += digit ** n # ** POTENCIACAO
        temp //= 10

    if ordem == cont:
        print('É um número de Armstrong:', ordem)
    else:
        pass
