num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

numeros = [num1, num2, num3]
numeros.sort()

print('O maior número é o {}'.format(numeros[2]))
print('O menor número é o {}'.format(numeros[0]))
