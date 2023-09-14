estado = dict()
brasil = list()

for c in range(0, 2):
    estado['uf']    = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # .copy() substitui o [:] que usava em lista para copiar, pois é um dict()

for e in brasil:                 # for para lista
    for k, v in e.items():       # for para dicionario
        print(f'O campo {k} tem valor {v}')

