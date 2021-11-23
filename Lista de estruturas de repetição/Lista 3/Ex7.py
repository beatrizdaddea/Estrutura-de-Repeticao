""" 7.A  sequência  de  Fibonacci  tem  papel  importante  na  explicação  de  fenômenos  naturais.Ela  é também bastante utilizada para fins estéticos, pela sua reconhecida harmonia.Exemplo disso foi sua  utilização  na  construção  do  Partenon,  em  Atenas.  A  sequênciadá-se  inicialmente  por  dois números 1. A partir do terceiro elemento usa-se aexpressão: elementon= elementon-1 + elementon-2. Exemplo de sequência: 1, 1, 2, 3, 5,8, 13, ...
Construa um algoritmo que imprima na tela os nprimeiros elementos da sequênciade Fibonacci, onde né informado pelo usuário. """

num = int(input('Quantos termos, baseados na sequência de Fibonacci, serão demonstrados?: '))
v1 = 0
elemento = 1
cont = 1

while (num >= cont):
    print(elemento, end= ' - ')
    elemento = elemento + v1
    v1 = elemento - v1
    cont = cont + 1