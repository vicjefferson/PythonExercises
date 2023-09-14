expressao = str(input("Digite a expressão: ")).strip().upper()
print(expressao)
parenteses = 0

for i in range(len(expressao)):
  if expressao[i] == '(' or expressao[i] == ')':
    parenteses+=1

if parenteses % 2 == 0:
  print('Sua expresão está correta!')
else:
  print('Sua expresão NÃO está correta!')