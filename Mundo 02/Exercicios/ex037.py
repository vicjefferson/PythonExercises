
num = int(input('Digite um numero inteiro qualquer: '))
print(''' 
Digite a base de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal
-> '''))
opcao = int(input('Sua opção: '))
if opcao == 1:
  print(bin(num)[2:1])
elif opcao == 2:
  print(oct(num)[2:1])
elif opcao == 3:
  print(hex(num)[2:1])
else:
  print('Opção Inválida')
