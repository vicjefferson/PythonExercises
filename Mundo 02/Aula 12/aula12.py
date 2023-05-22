nome = str(input('Qual seu nome: ')).capitalize()

if nome == 'Victor':
  print('Que nome top')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
  print('Seu nome é bem popular no Brasil.')
elif nome in 'Aurora Bloom Jessica Lia Hellen':
  print('Seu nome é lindo')
else:
  print('Seu nome é bem normal')

print('Tenha um bom dia, {}!'.format(nome))

from random import choice

print('Suas opções:')
print('''
[1] PEDRA
[2] PAPEL
[3] TESOURA''')

jogador = int(input('Qual a sua jogada? '))

jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
escolha = choice(jokenpo)

empate = 'Empate, vamos mais uma vez.'
vitoria = 'Parabéns! você ganhou.'
derrota = 'Que pena! Você perdeu.'


if jogador == 1 and escolha == escolha == 'PEDRA':
  print(escolha)
  print(empate)
elif jogador == 1 and escolha == escolha == 'PAPEL':
  print(escolha)
  print(derrota)
elif jogador == 1 and escolha == escolha == 'TESOURA':
  print(escolha)
  print(vitoria)
elif jogador == 2 and escolha == escolha == 'PEDRA':
  print(escolha)
  print(vitoria)
elif jogador == 2 and escolha == escolha == 'PAPEL':
  print(escolha)
  print(empate)
elif jogador == 2 and escolha == escolha == 'TESOURA':
  print(escolha)
  print(derrota)
elif jogador == 3 and escolha == escolha == 'PEDRA':
  print(escolha)
  print(derrota)
elif jogador == 3 and escolha == escolha == 'PAPEL':
  print(escolha)
  print(vitoria)
elif jogador == 3 and escolha == escolha == 'TESOURA':
  print(escolha)
  print(empate)
else: 
  print('Opção Inválida')