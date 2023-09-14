# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento
# de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO 
# nas eleições.


def voto(nascimento):
    from datetime import date
    year = date.today().year
    idade = year - nascimento

    if idade < 16:
        return f'Com {idade} anos, VOTO OBRIGATÓRIO!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, VOTO OPICIONAL!'
    else:
        return f'Com {idade} anos, VOTO OBRIGATÓRIO'

print(voto(2000))
