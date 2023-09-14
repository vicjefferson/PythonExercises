# Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer
# como parâmetro e mostre uma mensagem com tamanho adaptável.
# EX: escreva('Olá, Mundo!')
# SAÍDA: 
# -------------
#  Olá, mundo!
# -------------

def escreva(msg):
    print('~'* (len(msg) + 4))
    print(F'  {msg}')
    print('~'* (len(msg) + 4))


escreva('Olá, mundo!')
escreva('TESTANDO O TAMANHO')
escreva('OI')