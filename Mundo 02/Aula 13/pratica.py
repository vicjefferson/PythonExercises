

for c in range (0, 6): # Print de 0 a 5 
  print(c)
print('FIM!')

for c in range (6, 0, -1): # Print de 5 a 0
  print(c)
print('FIM!')

for c in range (0, 7, 2): # Print de 0 a 6 de 2 em 2
  print(c)
print('FIM!')

n = int(input('Digite um numero: ')) # Vai de 0 a n
for c in range (0, n+1): # n+1 apenas para deixar igual a n
  print(c)
print('FIM!')

for c in range(0, 3): # Vai perguntar três vezes | Lembrando índice 0 a 2
  number = int(input('Digite um valor: '))
print('FIM!')

s = 0
for c in range(0, 3): # Vai perguntar três vezes | Lembrando índice 0 a 2
  number = int(input('Digite um valor: '))
  s += n # Cada valor do input, adiciona a s
print('O somatório de todos os valores foi {}'.format(s))

