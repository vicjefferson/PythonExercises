brasileirao = 'Palmeiras', 'Internacional', 'Fluminense','Corinthians','Flamengo','Athletico-PR','Atlético-MG','Fortaleza','São Paulo','América-MG','Botafogo','Santos','Goiás','Bragantino','Coritiba','Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude'

print(f'Os 5 primeiros colocados são: {brasileirao[:5]}\n')
print(f'Os últimos 4 colocados são: {brasileirao[-4:]}\n')
print(f'Os times em ordem alfabética são: {sorted(brasileirao)}\n')

if 'São Paulo' not in brasileirao:
  print('São Paulo não está na serie A')
else:
  print(f"São Paulo está na {brasileirao.index('São Paulo') + 1}ª posição")
