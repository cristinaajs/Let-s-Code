numero_sorteado = 15

numero_escolhido = (input('Informe um número entre 1 e 20: '))

while numero_escolhido != numero_sorteado:
    print('Você errou o número, tente novamente...')
    numero_escolhido = int(input('Informe um número entre 1 e 20: '))
print('Parabéns! Você acertou ')


# Exemplo 02: Estrutura com contador

while contador < 5:
    print(contador)

    contador = contador + 1