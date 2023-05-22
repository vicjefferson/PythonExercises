
pesoMaior = 0
pesoMenor = 0

for i in range(1, 6): # 5 pessoas ao total
  peso = float(input('Peso da {}º pessoa: '.format(i)))
  for c in range(i):
    if i >= pesoMaior:
      pesoMaior = peso
    else:
      pesoMenor = peso
    

print('O maior peso lido foi de {}'.format(pesoMaior))
print('O menor peso lido foi de {}'.format(pesoMenor))


