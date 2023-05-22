

for c in range(0, 1):
  frase = str(input('Digite uma frase: ')).strip().upper()
  if frase == frase[::-1]:
    print('Sua frase ao contrário é {}'.format(frase[::-1]))
    print('Sua frase é um palimdromo!')



