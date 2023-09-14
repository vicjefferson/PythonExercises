extenso ='zero', 'um', 'dois', 'tres',  'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
numero  = -1

while True:
  if numero < 0 or numero > 20:
    numero = int(input('Digite um número: '))
  else:
    break

for i in range(len(extenso)):
  i = extenso[i]

print(f'Você digitou o número {extenso[numero]}')

