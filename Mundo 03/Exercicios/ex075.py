a = int(input('Valor: '))
b = int(input('Valor: '))
c = int(input('Valor: '))
d = int(input('Valor: '))
par = 0
tupla = a, b, c, d

if a % 2 == 0:
  par+=1
if b % 2 == 0:
  par+=1
if c % 2 == 0:
  par+=1
if d % 2 == 0:
  par+=1

print(f'Apareceu o número 9 apareceu {tupla.count(9)} vezes')
print(f'O primeiro valor 3 aparece na posição {tupla.index(3)+1}')
print(f'Total de números pares: {par}')