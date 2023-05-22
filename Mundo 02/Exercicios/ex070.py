print('-'*30)
print('{: ^30}'.format('LOJA BARATÃO'))
print('-'*30)

total = caro = 0
pdrMaisBarato = ' '
index = 1000000000000


while True:
  produto = str(input("Nome do Produto: "))
  preco   = float(input("Preço: R$ "))

  total += preco

  if preco > 1000:
    caro +=1
  if preco < index:
    index = preco
    pdrMaisBarato = produto

  resp = ' '
  while resp not in 'SN':
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  if resp == 'N':
    break

print(f'O total gasto na compra foi R$ {total:10.2f}') # 10 digitos ao todo e duas casa decimais  
print(f'Há {caro} que custam mais que R$ 1000.00')
print(f'O produto mais barato foi {pdrMaisBarato}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))