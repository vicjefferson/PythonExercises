
idadegrupo = 0
maiorIdadeHomem = 0
nomeVelho = ''
totMulher20 = 0

for p in range(1, 5): # Informações sobre 5 pessoas
   print('-------- {}º  PESSOA --------'.format(p))
   nome = str(input('Nome: ')).strip()
   idade = int(input('Idade: '))
   sexo = str(input('Sexo [M/F]: ')).strip()
   idadegrupo += idade
   if p == 1 and sexo in 'Mm':
      maiorIdadeHomem = idade
      nomeVelho = nome
   if sexo in 'Mm' and idade > maiorIdadeHomem:
      maiorIdadeHomem = idade
      nomeVelho = nome
   if sexo in 'Ff' and idade < 20:
      totMulher20 += 1

mediaIdade = idadegrupo / 4

print('A média da idade do grupo é {}'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorIdadeHomem, nomeVelho))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(totMulher20))
