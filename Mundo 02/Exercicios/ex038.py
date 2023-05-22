num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro: '))

if num1 > num2:
  print('O \033[33mprimeiro valor\033[m é \033[35mmaior!\033[m')
if num2 > num1:
  print('O \033[33msegundoo valor\033[m é \033[35mmaior!\033[m')
else num1 == num2:
  print('\033[mNão existe\033[m valor maior. Os dois são \033[35miguais\033[m')