# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno 
# retagular(largura e comprimento) e mostre a área do terreno.

def area(b, h):
    a = b * h
    print(f'A área do terreno {b}x{h} é de {a:.2f}m²')


print('Controle de Terrenos')
print('-'*20)

largura     = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

area(largura, comprimento)