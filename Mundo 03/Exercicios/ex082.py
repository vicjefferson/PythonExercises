lista      = []
listaPar   = []
listaimpar = []

while True:
  lista.append(int(input(f'Digite um valor: ')))
  resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
  while resp not in 'SN':
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
  if resp == 'N':
      break

for i in range(len(lista)):
  #print(lista[i])
  if lista[i] % 2 == 0:
    listaPar.append(lista[i])
  else:
    listaimpar.append(lista[i])

print(f'Lista original: {lista}\nLista Par: {listaPar}\nLista Ímpar: {listaimpar}')