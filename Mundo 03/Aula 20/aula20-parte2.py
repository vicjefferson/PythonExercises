# USANDO LISTAS NAS DEFs

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos+= 1
    print(lst)


valores = [7, 3, 8, 2, 4]
dobra(valores)