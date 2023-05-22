from datetime import date

anoAtleta = int(input('Informe seu ano de nascimento: '))


if date.today().year - anoAtleta <= 9:
  print('Sua categoria é \033[32mMIRIM\033[m')
elif date.today().year - anoAtleta > 9 and date.today().year - anoAtleta <=14:
  print('Sua categoria é \033[32mINFANTIL\033[m')
elif date.today().year - anoAtleta > 14 and date.today().year - anoAtleta <= 19:
  print('Sua categoria é \033[32mJUNIOR\033[m')
elif date.today().year - anoAtleta == 20:
  print('Sua categoria é \033[32mSÊNIOR\033[m')
else:
  print('Sua categoria é \033[32mMASTER\033[m')