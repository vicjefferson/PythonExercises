lista = []

for i in range(0, 5):
  n = int(input('Digite um valor: '))
  if i == 0 or n > lista[-1]: #Append se o n for o primeiro ou o último elemento da lista
    lista.append(n)
    print('Adicionado ao final da lista')
  else:
    pos = 0
    while pos < len(lista): #varrendo as posições da lista
      if n <= lista[pos]:
        lista.insert(pos, n)
        print(f'adiocionado na posição {pos} da lista')
        break
      pos +=1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')


