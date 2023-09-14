dados = dict() # Declarar dicionário
data = {'nome':'Pedro', 'idade':25}

print(data['nome'])
print(data['idade'])

# adicionar elementos ao dicionario
data['sexo'] = 'M'
# remover elemento
del data['idade']

#EX@

filme = {
    'titulo':'Star Wars',
    'ano':1977,
    'diretor':'Geroge Lucas'
}

# Item vs. Chave vs. Elemento
print(filme.values()) # Star Wars | 1977 | George Lucas -> valores
print(filme.keys())   # titulo    | ano  | diretor      -> Chaves
print(filme.items())  # MOSTRA AMBOS

for k, v in filme.items():
    print(f'O {k} é {v}')

# JUNTANDO LISTAS TUPLAS E DICT
locadora = [filme]
print(locadora[0]['ano'])

# Criar um dicionario dentro de uma lista

brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['sigla'])