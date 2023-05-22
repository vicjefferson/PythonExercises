
valorDaCasa = float(input('Informe o valor da casa -> '))
salario = float(input('Informe o salário do comprador -> '))
anos = int(input('Enquantos anos será pago? -> '))

prestacaoMensal = valorDaCasa / (anos * 12)

if prestacaoMensal > (salario * (30/100)):
  print('\033[31mEMPRÉSTIMO NEGADO!!!\033[m Infelizmente você não podera pagar este financiamento.')
else:
  print('\033[32mPARABÉNS!!!\033[m Você poderá pagar este financiamento em {} anos com um total de R${:.2f}/mês'.format(anos, prestacaoMensal))