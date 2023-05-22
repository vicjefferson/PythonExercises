# O CLASSICOOOOO, porém do jeito if

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

n1 = (nota1 + nota2) / 2
n2 = (nota3 + nota4) / 2

mediaParcial = ((2 * n1) + (3 * n2)) / 5

if mediaParcial >= 7:
  print('\033[32mAPROVADO, MEU CONSAGRADO!!!\033[m Sua MP é igual a {}.'.format(mediaParcial))
elif mediaParcial > 3 and mediaParcial < 7:
  provaFinal = 10 - mediaParcial
  print('\033[37mXIIII\033[m, Vai ter que fazer a prova final e precisa de, no mínimo, {}.'.format(provaFinal))
else:
  print('\033[31mREPROVADO!!!\033[m')