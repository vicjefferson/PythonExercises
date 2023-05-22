l = float(input('Digite a largura da parede -> '))
h = float(input('Digite a altura da parede -> '))

area = l * h
litrosT = 2

print('Será necessário {} l de tinta para pintar toda a parede!'.format(area/litrosT))