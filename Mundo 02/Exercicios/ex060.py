from math import factorial

''' r = 'S'

while r == 'S':
  num = int(input('Digite um valor: '))
  fatorial = factorial(num)
  print('O fatorial de {} é {}'.format(num, fatorial))
  r = str(input('Deseja ver outro valor? ')).strip().upper()
'''

# SEM MODULO MATH

num = int(input('Digite um valor: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
  print('{}'.format(c), end= '')
  print(' x 'if c > 1 else ' = ', end= '') 
  f *= c
  c -= 1
print('{}'.format(f))