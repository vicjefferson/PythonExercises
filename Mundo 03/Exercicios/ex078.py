num = []
maior = menor = 0
posmaior = posmenor = 0

for i in range(0, 5):
  num.append(int(input("Valor: ")))
  if num[i] > maior:
    maior = num[i]
    posmaior = i+1
    print(f'Indice maior atual: {posmaior}')
  if i == 0:
    menor = num[i]
    posmenor = i+1
  if num[i] < menor:
    menor = num[i]
    posmenor = i+1

num.sort()
print(f'O menor valor digitado foi {num[0]}, na {posmenor}ª posição')
print(f'O maior valor digitado foi {num[4]}, na {posmaior}ª posição')