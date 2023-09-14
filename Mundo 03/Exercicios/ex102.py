# Faça um programa que tenah uma função fatorial() que receba dois parâmetros: o primeiro que indica o numero
# a calcular e o outro chamado show, que será um valor lógico(opicional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial

def fatorial(n, show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x ', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))