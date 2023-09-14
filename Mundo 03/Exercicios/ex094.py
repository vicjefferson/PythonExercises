# Crie um programa que leia nome, sexo e idade de varias pessoas. Guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas.
# B) A média de idade do grupo.
# C) Uma lista com todas as mulheres.
# D) Uma lista com todas as pessoas com idade acima da média.

pessoa            = dict()
lista_de_pessoas  = list()
lista_de_mulheres = list()
lista_idade_acima = list()

while True:
    pessoa.clear()
    pessoa['nome']  = str(input('Nome: '))

    while True:
        pessoa['sexo']  = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    
    pessoa['idade'] = int(input('Idade: '))

    lista_de_pessoas.append(pessoa.copy())

    while True:
        resp = str(input('Cadastrar uma nova pessoa? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N.')
    if resp == 'N':
        break


print(lista_de_pessoas)
print('-='*20)

idadeTotal = 0
for i in range(len(lista_de_pessoas)):
    idadeTotal += lista_de_pessoas[i]['idade']
    if lista_de_pessoas[i]['sexo'] == 'F':
        lista_de_mulheres.append(lista_de_pessoas[i])

mediaIdade = idadeTotal / len(lista_de_pessoas)
for i in range(len(lista_de_pessoas)):
    if lista_de_pessoas[i]['idade'] > mediaIdade:
        lista_idade_acima.append(lista_de_pessoas[i])
        
print(f'A) Ao todo foram cadastradas {len(lista_de_pessoas)} pessoas')
print(f'B) A média de idade do grupo é {mediaIdade}')
print(f'C) As mulheres cadastradas foram: {lista_de_mulheres}')
print(f'D) Pessoas com idade acima da média {lista_idade_acima}')
