c = 1
numerosDigitados = soma = 0
while c > 0:
  num = int(input('Digite um valor [999 para parar]: '))
  if num == 999:
    c -= 1
    break
  else:
    numerosDigitados += 1
    soma += num
print('Foram digitados, ao todo, \033[32m{}\033[m números.'.format(numerosDigitados), end= ' ')
print('E sua a soma de todos é igual a \033[32m{}\033[m'.format(soma))

#\033[32m -> Verde