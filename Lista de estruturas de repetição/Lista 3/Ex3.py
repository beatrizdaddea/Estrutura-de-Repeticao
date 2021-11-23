""" 3.Construa  um  algoritmo  que,  dado  o  primeiro  elementoa 1e  a  razãor de  uma  progressão aritmética (PA), imprima todos os n primeiros elementos da PA, onde a1, re nsãoinformadospelo usuário. Lembre-se que uma PA pode ser crescente ou decrescente."""

a1 = int(input("Primeiro elemento da PA: "))
r = int(input("Razao da PA: "))
n = int(input('Digite os termos da PA: '))

formula = a1 + (n - 1) * r
formula = formula + 1
n = 1

for item in range(a1, formula, r):
    print('n', n, '=', item, end="; ")
    n += 1
