import math

salario = float(input('Digite o valor do salário do funcionário: R$ '))

if salario > 1.250:
  novoSalario = salario + (salario * 10 / 100)
  print('Seu salario com aumento é igual a R$ {}'.format(novoSalario))
else:
  novoSalario = salario + (salario * 15 / 100)
  print('Seu salario com aumento é igual a R$ {}'.format(novoSalario))
print('Obrigado por usar meu aplicativo')