# MELHORANDO O EXERCÍCIO ANTERIOR

# Desenvolva um programa queleia o Primeiro termo e a razão
# de uma PA. No final, mostre os 10 primeiros termos dessa progressão
print('-=-' * 10)
print('   PROGRESSÃO ARITIMÉTICA   ')
print('-=-' * 10)
primeiroTermo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
decimoTermo = primeiroTermo + (10 - 1) * razão

# USANDO WHILE

c = primeiroTermo # Digamos que o primeiroTermo seja 0 e a razão 2
r = 'S'
while r == 'S':
  while c < decimoTermo + razão: # 0 < 18 + 2 -> 0 < 20
    print("{} ".format(c), end="-> ") # 0
    c = c + razão # 0 = 0 + 2 -> c = 2
  print("ACABOU")
  r = str(input('Quer mostrar mais alguns termos? ')).strip().upper()
  decimoTermo = primeiroTermo + (15 - 1) * razão

