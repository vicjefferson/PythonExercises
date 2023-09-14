def soma(x, y):
    print(x+y)

soma(5, 7)
soma(y=5, x=7)
# soma(3, 9, 5) -> !!! NAO PODE

# EMPACOTAMENTO
def contador(*num): # * == desempacotar | parametros infinitos
    print(num)

# Abaixo python criará uma TUPLA na saída
contador(2, 1, 7)
contador(8, 0)
contador(7, 9, 0, 7, 4, 6)

def contador1(*num): # * == desempacotar | parametros infinitos
    for valor in num:
       print(f'{valor} ', end='')
    print('FIM')

# Mostrará os numeros na tela
contador1(2, 1, 7)
contador1(8, 0)
contador1(7, 9, 0, 7, 4, 6)

def contador2(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador2(2, 5, 8, 2)