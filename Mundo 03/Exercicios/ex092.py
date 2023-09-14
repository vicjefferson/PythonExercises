# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade)
# em um dicionário se por acaso a CTPS dor diferente de ZERO. O dicionário receberá também o ano de
# contratação e o salário. Calcule e acrescente, além da idade, comqantos anos a pessoa vai se aposentar.

import datetime

#datetime.now().year

date = datetime.date.today()
year = int(date.strftime("%Y"))

pessoa = {}

pessoa['nome'] = str(input('Nome: '))
pessoa['ano']  = int(input('Ano de nascimento: '))
pessoa['CTPS'] = int(input('CTPS: '))

idade = year - pessoa['ano']

if pessoa['CTPS'] != 0:
    pessoa['contratacao']   = int(input('Ano de contratação: '))
    pessoa['salario']       = float(input('Salário: R$ '))
    contribuicao = year - pessoa['contratacao']
    if contribuicao < 35:
        pessoa['aposentadoria'] = idade + (35 - contribuicao)

for k, v in pessoa.items():
    print(f'{k} tem valor {v}')

 