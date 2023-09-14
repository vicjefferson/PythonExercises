# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# OBS: Use cores

def manual(user_input):
    help(user_input)

user = input('Função ou Biblioteca: ')
manual(user)