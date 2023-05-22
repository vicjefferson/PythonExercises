c = 0
while True:
  tabuada = int(input('Quer ver a tabuada de qual valor [<0 STOP]? '))
  if tabuada < 0:
    break
  else:
    for c in range (1, 11):
      print(f'{tabuada} x {c} = {tabuada * c}')
print('PROGRAMA TABUADA ENCERRAO. Volte sempre!')