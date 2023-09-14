# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é maior.

def maior(*n):
    maior = 0
    print('-='*20)
    print(f'{n} Foram informados {len(n)} valores')
    for i in range(len(n)):
        if i == 0:
            maior = n[i]
        else:
            if n[i] > maior:
                maior = n[i]
    print(f'O maior valor foi {maior}')

maior(2, 9, 5)
maior(2, 5)