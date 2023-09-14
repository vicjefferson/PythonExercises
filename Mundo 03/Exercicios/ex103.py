# Faça um program que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
# e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def leiaInt(msg):
    ok    = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok    = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')