print('-' * 30)
print('Sequência de Fibonacci')
print('-' * 30)

n = int(input('Quantos termos quer mostrar? '))

# Com lista - VICTOR

'''
fibonacci = [0, 1]

c = 0
while c < n:
  novoTermoFibonnaci = fibonacci[-1] + fibonacci[-2]
  fibonacci.append(novoTermoFibonnaci)
  c += 1
print(fibonacci[0: -2])
'''

t1 = 0
t2 = 1
print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
c = 3
while c <= n:
  t3 = t1 + t2
  print(' -> {}'.format(t3), end='')
  t1 = t2
  t2 = t3
  c += 1
print(' -> FIM')

