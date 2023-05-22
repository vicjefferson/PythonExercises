frase = 'Curso em vídeo Python'

print(frase[15]) # Mostra o caractere no índice 15
print(frase[9:13]) # Começa no índice 9 e termina no índice 12
print(frase[9:21]) # Começa no índice 9 e termina no índice 20, ps: índice 21 não existe
print(frase[9:21:2]) # Começa no índice 9 e termina no índice 21 pulando de 2 em 2
print(frase[:5]) # Começa do caractere 0 (C) e termina no índice 4
print(frase[15:]) # Começa do índice 15 e vai até o último
print(frase[9::3]) # Começa no índice 9 e vai até o último e pulando 3 em 3

# ANALISE

len(frase) # Mostra o tamanho da string
frase.count('o') # Conta quantas vezes a letra o minúscula aparece em frase
frase.count('o') # Mesmo que o anterior, porém com fatiamento
frase.find('deo') # Quantas vezes encontrou deo e indica onde o índice começa
'curso' in frase # Existe a palavra curso em frase > Retorna True or False

# TRANSFORMAÇÃO

frase.replace('Python','Android') # Onde houver a plavra python, substitue por android
frase.upper() # Ficar em maiúscula > Retorna CURSO EM VÍDEO PYTHON
frase.lower() # Ficar em minúscula > Retorna curso em vídeo python
frase.capitalize() # Retorna Curso em video python
frase.title() # Faz um captalize palavra por palavra >>> Curso Em Video Python

novaFrase = '   Aprenda Python  ' # 3 espaços iniciais e 2 finais

novaFrase.strip() # Remove os espaços inúteis >>> os 3 primeiros e os 2 ultimos
novaFrase.rstrip() # Remove os espaços inúteis à direita
novaFrase.lstrip() # Remove os espaços inúteis à esquerda

# DIVISÃO

frase.split() # ESTUDAR!!! Divide as palavras colocando em uma nova lista e cada palavra tem um índice >>> palavra 'Curso' = índice 0 | palavra 'em' = índice 1 e ...

# JUNÇÃO

'-'.join(frase) # Pegando o output anterior, o join vai retornar 'Curso-em-Video-Python' 

