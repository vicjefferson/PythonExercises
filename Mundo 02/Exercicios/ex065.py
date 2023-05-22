resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
  num = int(input('Digite um número: '))
  soma += num
  quant += 1
  if quant == 1:
    maior = menor = num
  else:
    if num > maior:
      maior = num
    if num < menor: 
      menor = num
  resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

# JEITO VICTOR
'''
c = 2
soma = maior = totnum = 0
menor = 999999999

while c != 0:
  num = int(input('Digite um valor: '))
  soma += num
  totnum += 1
  if num > maior:
    maior = num
  elif num < menor:
    menor = num
  c -= 1
  if c == 1:
    res = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if res == 'S':
      c += 1
    else:
      c -= 1

media = soma / totnum

print('A média entre os {} números foi {}'.format(totnum, media))
print('O maior número entre os {} digitados foi {} e o menor foi {}'.format(totnum, maior, menor))
'''