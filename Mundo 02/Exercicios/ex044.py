precoNormal = float(input('Qual o valor do produto: '))

a = str(input('''
Como prefere pagar o produto?

1 - À vista: Dinheiro / Cheque
2 - À vista: Cartão
3 - Parcelado Cartão
-> '''))

if a == '1':
  desconto = precoNormal - (precoNormal * 10/100)
  print('O total a pagar com desconto de \033[32m10%\033[m é de \033[32mR${}.'.format(desconto))
elif a == '2':
  desconto = precoNormal - (precoNormal * 5/100)
  print('O total a pagar com desconto de \033[32m5%\033[m é de \033[32mR${}.'.format(desconto))
else:
  b = str(input('''
  Escolha o total de parcelas a pagar: 

  2 - 2x
  3 - 3x
  4 - 4x
  5 - 5x
  6 - 6x
  '''))
  if b == '2':
    precoNormalParcelado = precoNormal / 2
    print('Total a pagar pelo produto é R${} e cada parcela irá custar \033[32mR${}\033[m'.format(precoNormal, precoNormalParcelado))
  else:
    juros = precoNormal + (precoNormal * 20/100)
    print('Cada parcela irá custar \033[32mR${}\033[m'.format(juros))


    



