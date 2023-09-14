# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo 
# e realize a contagem. Seu programa tem que realizar três contagens através da função criada.
# A) de 1 até 10, de 1 em 1.
# B) de 10 até 0, de 2 em 2.
# C) uma contagem personalizada.

from time import sleep

def contador():
    print('-='*30)
    print('Contagem de 1 até 10 de 1 em 1')
    for i in range(10):
        print(i+1, end=' ')
    print()

    print('-='*30)
    print('Contagem de 10 até 1 de 2 em 2')
    c = 10
    for i in range(6):
        print(c, end=' ')
        c -= 2
    print()

    print('Agora é a sua vez de personalizar a contagem')
    inicio_input = int(input('Inicio: '))
    fim_input    = int(input('Fim:    '))
    passo_input  = int(input('Passo:  '))

    print('-='*30)

    if passo_input != 0:
        if inicio_input < fim_input:
            print(f'Contagem de {inicio_input} até {fim_input} de {passo_input} em {passo_input}')
            for i in range(fim_input - inicio_input):
                if inicio_input <= fim_input:
                    print(inicio_input, end= ' ', flush=True) #Buffer de tela off, numeros aparecem um a um
                    inicio_input += passo_input
            if fim_input < 0:
                print(fim_input)
        elif inicio_input > fim_input:
            print(f'Contagem de {inicio_input} até {fim_input} de {passo_input} em {passo_input}')
            for i in range(inicio_input - fim_input):
                if inicio_input >= fim_input:
                    print(inicio_input, end=' ', flush=True)
                    inicio_input -= passo_input
        elif inicio_input == fim_input:
            print('INICIO E FIM SÃO IGUAIS.')
    else: 
        print('Passo tem que ser != de 0')
    



contador()