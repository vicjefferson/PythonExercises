# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um 
# dicionário com as seguintes informações:
#
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(opcional)
#
# Adcione também as docstrings da função.

def notas(*notas, sit=False):
    """
    docstring
    
    """
    dic_notas      = dict()

    dic_notas['total'] = len(notas)
    dic_notas['maior'] = max(notas)
    dic_notas['menor'] = min(notas)
    dic_notas['media'] = sum(notas) / len(notas)

    if sit:
       if dic_notas['media'] >= 7:
          dic_notas['situação'] = 'BOA'
       elif dic_notas['media'] <= 3:
          dic_notas['situação'] = 'RUIM'
       else:
          dic_notas['situação'] = 'RAZOÁVEL'

    print(dic_notas)
    


notas(3.5, 2, 6.5)
