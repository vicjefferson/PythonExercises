from datetime import date

maiores = 0 # Considerando maior de idade 21 anos
menores = 0
for i in range(0, 7):
  anoPessoa = int(input('Digite sua data de nascimento: '))
  if date.today().year - anoPessoa >= 21:
    maiores +=1
  else:
    menores +=1
print('{} pessoas atingiram a maior idade e {} ainda não chegaram.'.format(maiores, menores))
