
lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

print('-'*20)
print(f'Tupla: {lanche}')
print(f'Índice 1: {lanche[1]}')
print(f'Do índice 1 até o fim: {lanche[1:]}')
print(f'Iniciando do índice 0 até o 2: {lanche[0:3]}')
print(f'Índice -2: {lanche[-2]}')
print('-'*20)

'''
# tuplas são IMUTÁVEIS
#   lanche[1] = 'Refrigerante'

# printando indice a indice e exibindo índices
for comida in lanche:  # Não conseguimos a posição
  print(f'lanche: {comida}')
print(f'\nTotal de comidas na tupla lanche: {len(lanche)}') # Mostra o tamanho da tupla
print('-'*20)

for cont in range(0, len(lanche)):
  print(lanche[cont])
print('-'*20)

for pos, comida in enumerate(lanche):
  print(f'O lanche {comida} está na posição {pos}')
print('-'*20)

'''

# Usando números em tuplas

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # A ordem da operação influencia no resultado
d = b + a # A ordem da operação influencia no resultado
print(f'A: {a}')
print(f'B: {b}')
print(f'C = A + B: {c}')
print(f'D = B + A: {d}')
print('-'*20)
# Ordenando a tupla | Ao printar, mostra em [ ] ao invés de ( ), pois tuplas são IMUTÁVEIS
print('Tupla A sorteada: ', sorted(a))
print('Tupla B sorteada: ', sorted(b)) 
print('Tupla C or D sorteada: ', sorted(c)) 
print('Tupla lanche sorteada: ', sorted(lanche)) 
print('-'*20)

# comando internos
print(f'O número 5 aparece {c.count(5)} vez(es) em C') # quantas vezes o 5 aparece em C
print(f'O índice do número 5 em C é {c.index(5)}') # informa o índice do número desejado, no caso 5. PS: Pega sempre a primeir ocorrência
print(f'O índice do número 5, a partir da posição 1, em C é {c.index(5, 1)}') # mesmo que acima, porém a partir da posição 1


# for pos, comida in enumerate(lanche):
#  print(f'Lanche: {comida} | Posição: {pos}') # Embora sorteado acima, as posições não mudam 