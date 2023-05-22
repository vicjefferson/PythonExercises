from datetime import date

nasc = int(input('Informe seu ano de nascimento: '))

if (date.today().year - nasc) < 18:
  print('Você \033[33mainda vai se alistar\033[m ao serviço miliar.')
elif (date.today().year - nasc) > 18:
  print('Já \033[33mpassou da hora de se alistar\033[m ao serviço miliar.')
else:
  print('Você \033[33mtem de se alistar\033[m ao serviço miliar este ano.')