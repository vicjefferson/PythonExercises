
# docstrings

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return:  sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

# Interactive help
help(contador)

# Parametros Opcionais
def somar(a=0, b=0, c=0):
    """
    -> Soma 3 valores, caso não sejam informados, o parametro recebe 0.
    """
    s = a + b + c
    print(f'A soma vale {s}')

help(somar)
somar(1, 2, 3)
somar(1, 2)
somar(1)
somar()

# Escopo de variáveis
def teste(b):
    global a 
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')

# Retorno de Valores
def multiplicar(a=0, b=0, c=0):
    """
    -> Multiplica 3 valores, caso não sejam informados, o parametro recebe 0.
    -> :return: s
    """
    s = a + b + c
    return s


m1 = multiplicar(1, 2, 3)
m2 = multiplicar(1, 2)
m3 = multiplicar(1)

print(f'Os resultados foram {m1}, {m2} e {m3}')
