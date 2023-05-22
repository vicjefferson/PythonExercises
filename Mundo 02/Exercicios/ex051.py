
# Desenvolva um programa queleia o Primeiro termo e a razão
# de uma PA. No final, mostre os 10 primeiros termos dessa progressão
print('-=-' * 10)
print('   PROGRESSÃO ARITIMÉTICA   ')
print('-=-' * 10)
primeiroTermo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
decimoTermo = primeiroTermo + (11 - 1) * razão

for c in range(primeiroTermo, decimoTermo, razão):
  print('{} ->'.format(c), end= ' ')
print('ACABOU', end= ' ')