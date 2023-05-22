# refazer desafio 9

#for c in range(0, 10):
#  n = int(input('Escolha um número para ver sua tabuada: '))
#  for v in range(0, 11):
#    print('{} x {} = '.format(n, v), n*v)
#  break
#print('--- FIM ---')

# usando apenas 3 linhas
num = int(input('Escolha um número para ver sua tabuada: '))
for i in range(1, 11): # Vai de 1 a 10
  print('{} x {:2} = {}'.format(num, i, num+i))
  
