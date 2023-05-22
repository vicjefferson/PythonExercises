aluguel = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos km percorridos? '))
custo = 60 * aluguel + 0.15 * km
print('O Carro alugado por {} dias e com {} km percorridos, custou R${}'.format(aluguel, km, custo))