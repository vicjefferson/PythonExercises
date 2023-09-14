from random import randint
from time import sleep

ranking = {}

print('Valores sorteados:')
for i in range(4):
    sleep(1)
    x = randint(1, 6)
    print(f'O jogador{i+1} tirou {x}')
    ranking[f'jogador{i+1}'] = x
       
print('Ranking dos jogadores:')
print(sorted(ranking.items(), key=lambda x: x[1], reverse=True))


