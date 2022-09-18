# > Dicionários

# Criando dicionários

dicionario = {}
dicionario = dict()

dicionario = {'nome': 'Cristina', 'idade': 27, 'altura': 1.55}

print(dicionario)
print(dicionario['idade'])

# Adicionando elementos em um dicionário

dicionario['programadora'] = True

print(dicionario)

dicionario['altura'] = 2

print(dicionario)

#Interando Sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

# Testando a existência de uma chave

print('peso' in dicionario)
print('altura'in dicionario)