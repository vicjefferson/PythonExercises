produto = float(input('Digite o valor do produto -> R$ '))
desconto = produto - produto * 0.05
print('O valor final do produto com 5% de desconto é R${:.2f}'.format(desconto))