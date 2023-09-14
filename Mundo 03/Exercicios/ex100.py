# Faça um program que tenha uma lista chamada números e duas funções cahmadas sorteia() e somaPar().
# A primeira função vai sprtear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma denre todos os valres PARES sorteados pela função anterior.

from random import randint

sorteados = list()

def sorteia():
    for i in range(5):
        x = randint(0, 10)
        sorteados.append(x)
    print(f'Sorteando 5 valores da lista: {sorteados}')

def somaPar():
    pares = 0
    for valor in sorteados:
        if valor % 2 == 0:
            pares += valor
    print(f'Somando os valores pares de {sorteados}, temos {pares}')


sorteia()
somaPar()