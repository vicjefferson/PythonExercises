from random import randint

print('=-='*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*10)

comp = randint(0, 10)
soma = vitorias = 0


  
while True:
  num = int(input('Digite um valor: '))
  poi = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
  soma = num + comp
  if soma % 2 == 0 and poi == 'P':
    print(f'Você jogou {num} e o computador {comp}. Total de {soma} DEU PAR')
    print('Você VENCEU!\nVamos jogar novamente ...')
    vitorias += 1
  elif soma % 2 == 0 and poi =='I':
    print(f'Você jogou {num} e o computador {comp}. Total de {soma} DEU PAR')
    print('Você PERDEU!')
    break
  elif soma % 2 != 0 and poi == 'I':
    print(f'Você jogou {num} e o computador {comp}. Total de {soma} DEU IMPAR')
    print('Você VENCEU!\nVamos jogar novamente ...')
    vitorias += 1
  else:
    print(f'Você jogou {num} e o computador jogou {comp}. Total de {soma} DEU IMPAR')
    print('Você PERDEU!')
    break

print('=-='*20)
print(f'GAME OVER! Você venceu {vitorias} vez(es)')
