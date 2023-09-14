# Crie um programa que tenha a função leiaint(), que vai fucionar de forma semelhante a função input() do Python,
# só que fazendo a validação para aceitar apenas valor numérico.
# EX: n = leiaint('Digite um n')

def leiaint(num):
    x = input(num)
    print(f'Valor de {x}')
    while x not in '01234567890':
        print('ERRO! Digite um valor inteiro')
        x = input(num)
    return x

n = leiaint('Digite: ')
print(f'Vc digitou {n}')