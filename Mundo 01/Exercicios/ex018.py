# Seno, Cosseno e Tangente

import math

ângulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente =math.tan(math.radians(ângulo))

print('O ângulo {} tem SENO de {:.2f}, COSSENO de {:.2f} e TANGENTE de {:.2f}'.format(ângulo, seno, cosseno, tangente))