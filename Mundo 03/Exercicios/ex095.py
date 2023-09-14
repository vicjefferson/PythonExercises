# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo
# um sistema de visualização de detalhes do aproveitamento de cada jogador.

time      = []
jogador   = {}
gols      = []
total     = 0

while True:
  jogador.clear()
  jogador['nome'] = str(input('Nome do jogador: '))
  partidas        = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

  for i in range(partidas):
      gol = int(input(f'Quantos gols na partida {i+1}? '))
      gols.append(gol)
      total += gol
    
  jogador['gols']  = gols[:]
  jogador['total'] = total
  time.append(jogador.copy())
  gols.clear()
  total = 0

  while True:
    resp = str(input('Cadastrar uma nova pessoa? [S/N] ')).upper()
    if resp in 'SN':
        break
    print('ERRO! Digite apenas S ou N.')
  if resp == 'N':
    break

print('-='*27)

print(f'cod ', end='')
for i in jogador.keys():
   print(f'{i:<15}', end='')
print()

print('-='*27)

for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
       print(f'{str(d):<15}', end='')
    print()

while True:
   busca = int(input('Cod do jogador que desejar visualizar (999 para parar): '))
   if busca == 999:
      break
   if busca >= len(time):
      print(f'ERRO! Não existe jogador com código {busca}')
   else: 
      print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]} -- ')
      for i, g in enumerate(time[busca]['gols']):
         print(f'   No jogo {i+1} fez {g} gols')
print('-'*30)
print('  <<< VOLTE SEMPRE >>>')