listagem = 'Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.80, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90

print('='*50)
print('{: ^50}'.format('LISTAGEM DE PREÇOS'))
print('-'*50)

for i in range(18):
  if i == 0 or i % 2 == 0:
    a = 40 - len(listagem[i])
    b = '.' * a
    print(f'{listagem[i]}' f'{b}' 'R${: >8}'.format(listagem[i+1]))
print('-'*50)

# f'R$ {listagem[i+1]:.2f}')