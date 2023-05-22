print('-=-' * 10)
print('Analisador de triângulos')
print('-=-' * 10)

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 +seg3 and seg3 <seg1 + seg2:
  print('Os segmentos acima podem formar um triângulo')
  if seg1 == seg2 and seg2 == seg3:
    print('Este triângulo é \033[32mEquilátero\033[m')
  elif seg1 == seg2 and seg1 != seg3 or seg2 == seg3 and seg3 != seg1 or seg3 == seg1 and seg1 != seg2:
    print('Este triângulo é \033[32mIsósceles\033[m')
  else:
    print('Este triângulo é \033[32mEscaleno\033[m')
else:
  print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo')