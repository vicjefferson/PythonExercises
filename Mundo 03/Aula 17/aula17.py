valores = []
for cont in range(0, 5):
  valores.append(int(input('Adicione um valor à lista: ')))

for c, v in enumerate(valores):
  print(f'Na posição {c+1} encontrei o valor {v}!')
print('Cheguei ao final domeu código')