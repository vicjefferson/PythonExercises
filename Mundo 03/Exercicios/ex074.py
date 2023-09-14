from random import randint
a = b = c = d = e = maior = 0
menor = 100

a  = randint(0, 100)
b  = randint(0, 100)
c  = randint(0, 100)
d  = randint(0, 100)
e  = randint(0, 100)

tuplaTotal = (a, b, c, d, e)

print(a, b, c, d, e)

if maior < a:
  maior = a
print(f'Maior atual é: {maior}')
if maior < b:
  maior = b
print(f'Maior atual é: {maior}')
if maior < c:
  maior = c
print(f'Maior atual é: {maior}')
if maior < d:
  maior = d
print(f'Maior atual é: {maior}')
if maior < e:
  maior = e
print(f'Maior atual é: {maior}')

print('='*20)

if menor > a:
  menor = a
print(f'Menor atual é: {menor}')
if menor > b:
  menor = b
print(f'Menor atual é: {menor}')
if menor > c:
  menor = c
print(f'Menor atual é: {menor}')
if menor > d:
  menor = d
print(f'Menor atual é: {menor}')
if menor > e:
  menor = e
print(f'Menor atual é: {menor}')

print(tuplaTotal, menor, maior)