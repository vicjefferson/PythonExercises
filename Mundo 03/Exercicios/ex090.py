# Faça um programa que leia nome e média (>= 7 == aproved) de um auno, guardando também a situação emum dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = dict()

aluno['nome']  = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é igual a {v}')
