# Crie um programa onde o usuário possa digitar sete valores numericos
# e cadastre-os em uma lista única que mantenha separado os valores
# pares e impares. No final, mostre os valores pares e impares em ordem crescente.

geral = [[], []]

for i in range(0,7):
  n = int(input(f'Digite o {i+1} valor: '))
  if n % 2 == 0:
    geral[0].append(n)
  else:
    geral[1].append(n)

geral[0].sort()
geral[1].sort()

print(f'Os valores pares digitados foram: {geral[0]}')
print(f'Os valores impares digitados foram: {geral[1]}')