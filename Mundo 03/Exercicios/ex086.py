# Crie um programa que crie uma matriz 3x3 e preencha com valores lifos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = terCol = maiorSeg = 0

for l in range(3):
    for c in range(3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-='*30)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            terCol += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maiorSeg:
                maiorSeg = matriz[l][c]

print(f'A soma dos valores pares é {pares}')
print(f'A sina dis valores da terceira coluna é {terCol}')
print(f'O maior valor da segunda linha é {maiorSeg}')