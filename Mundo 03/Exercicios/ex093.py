# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e 
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário. Incluindo o total de gols feitos no campeonato.

jogador = {}
gols    = []
total = 0

jogador['nome']     = str(input('Nome do jogador: '))
partidas            = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for i in range(partidas):
    gol = int(input(f'Quantos gols na partida {i+1}? '))
    total += gol
    gols.append(gol)

jogador['gols']  = gols
jogador['total'] = total

print('-='*27)
print(jogador)
print('-='*27)

for k, v in jogador.items():
    print(f' O campo {k} tem valor {v}')

print('-='*27)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i in range(len(gols)):
    print(f'   => Na partida {i+1}, fez {gols[i]} gols.')
print(f'Um total de {total} gols.')
