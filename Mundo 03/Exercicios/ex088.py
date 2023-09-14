# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre
# 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random as rd
from time import sleep

print('-' * 30)
print('JOGO DA MEGA SENA')
print('-' * 30)

nJogos = int(input("Quantos jogos bocê quer que eu sorteie? "))
print(f'-=-=-= SORTEANDO {nJogos} JOGOS -=-=-=')

for i in range(nJogos):
    jogo = list()
    for j in range(6):
        x = rd.randint(1, 60)
        if x not in jogo:
          jogo.append(x)
    jogo.sort()
    sleep(1)
    print(f'Jogo {i+1}: {jogo}')

print(f'-=-=-= < BOA SORTE! > -=-=-=')