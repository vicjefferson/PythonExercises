s = 0 # Se ficasse dentro daria erro

for i in range(1, 7):
  n = int(input('Digite o {}º valor: '.format(i)))
  if n % 2 == 0:
    s += n

print('A soma dos números pares é igual a {}'.format(s)) 

