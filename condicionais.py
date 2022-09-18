# > Estruturas Condicionais

idade = 20

if idade >= 18:
    print('Você é maior de idade.')
else:
    print('Você é menor de idade.')

"""
Imagine que você qeira imprimir "Aprovada", caso o estudante tenha uma média superior 
ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""

# Tentativa _____________________________________________________________________________________
media = 7

if media >= 7:
    print('Você está aprovado')
else:
    print('Você está reprovado')
# Tentativa _____________________________________________________________________________________

media = float(input('Informe a média do estudante: '))

if media >= 7:
    print('Você está aprovado')
elif media >= 5:
    print('Recuperação')
else:
    print('Você está reprovado')


    media = 10
    presenca = 100

    if media >= 7 and presenca >=70:
        print('Aprovada!')
    else: 
        print('Reprovado')
