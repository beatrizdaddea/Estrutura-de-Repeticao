"""Crie um algoritmo que, dado um número informado pelo usuário, imprima a tabuada dele de 1 a 10. Use o formato de apresentação (considerando que o usuário informouo número 5):5 x 1 = 55 x 2 = 105 x 3 = 15etc..."""

num = int(input('Digite uma tabuada: '))
cont = 1

while (cont <= 10):
    tabuada = num * cont
    print(f'{num} X {cont} = {tabuada}')
    cont += 1
