lista = []

while True:
  valor = (int(input('Digite um valor: ')))
  if valor in lista:
    print("Valor duplicado! não irei adicionar!")
  else:
    lista.append(valor)
    print('Valor adicionado!')
  resp = str(input("Deseja continuar? [S/N] ")).strip().upper()
  if resp == 'N':
    break


print('-='*30)
lista.sort()
print(f'Você digitou os valores {lista}')