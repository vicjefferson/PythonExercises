# Sorteando item na lista

import random

primeiroAluno = input('Primeiro aluno: ')
segundoAluno = input('Segundo aluno: ')
terceiroAluno = input('Terceiro aluno: ')
quartoAluno = input('Quarto aluno: ')

listaDeAlunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
escolhido = random.shuffle(listaDeAlunos)

print('A ordem de apresentação será: ')
print(listaDeAlunos)
