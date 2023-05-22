# Sorteando um item na lista
# from random import choice (caso queira apenas este módulo | troque random.choice por choice)
import random

primeiroAluno = str(input(('Primeiro aluno: ')))
segundoAluno = str(input(('Segundo aluno: ')))
terceiroAluno = str(input(('Terceiro aluno: ')))
quartoAluno = str(input(('Quarto aluno: ')))

listaDeAlunos = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
escolhido = random.choice(listaDeAlunos)

print('O aluno sorteado foi {}'.format(escolhido))