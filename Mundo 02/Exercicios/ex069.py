
pessoa = homem = mulher = maior = 0

while True:

  print("-"*20)
  print("CADASTRE UMA PESSOA")
  print("-"*20)

  idade = 0
  sexo = 'X'

  while idade <= 0:
    idade = int(input("Idade: "))
  while sexo != 'M' and sexo != 'F':
    sexo = str(input("Sexo: [M/F] ")).upper()
  
  pessoa+=1

  if idade > 18:
    maior+=1
  if sexo == 'M':
    homem+=1
  if idade < 20 and sexo == 'F':
    mulher+=1
  
  print("-"*20)
  resposta = str(input("Deseja continuar? [S/N] ")).upper()
  if resposta != 'N' and resposta != 'S':
    resposta = print("Deseja continuar? [S/N] ").upper()
  elif resposta == 'N':
    break

print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo há {mulher} mulher(es) com menos de 20 anos')
print(f'Foram cadastradas {pessoa} pessoas, dentre elas {homem} são homens')

# While True:
#   idade = int(input('Idade: ))
#   sexo = ' '
#   while sexo not in 'MF':
#     sexo = str(input('Sexo: [M/F] )).strip().upper()[0] -> pegando só a primeira letra
#   
#   resp = ' '
#   while resp not in 'SN':
#     resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
#   if resp == 'N':
#     break

# print("Acabou!")
