lista = []
numerosDigitados = 0
while True:
  valor = (int(input(f'Digite um valor: ')))
  lista.append(valor)
  numerosDigitados+=1
  resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
  while resp not in 'SN':
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
  if resp == 'N':
      break

lista.sort(reverse=True)
print(f'Você diigtou {numerosDigitados} elementos')
print(f'Lista em ordem decrescente: {lista}')

if 5 in lista:
  print(f'O número 5 está na posição: {lista.index(5)+1}')
else:
  print('O numéro 5 não está na lista')