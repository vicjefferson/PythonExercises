
print('-=-' * 10)
print('   VERIFICAR NÚMERO PRIMO   ')
print('-=-' * 10)

number = int(input('Digite um número -> '))
total = 0

for c in range(1, number + 1):
  if number % c == 0:
    print('\033[33m', end='')
    total += 1
  else:
    print('\033[31m', end='')
  print('{} '.format(c), end='')
print('\n\033[mO número {} foi dividido {} vezes.'.format(number, total), end= ' ')
if total == 2:
  print('E por isso É PRIMO!')
else:
  print('E por isso NÃO É PRIMO!')
