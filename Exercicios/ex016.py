import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = math.hypot(co,ca)
'Comentário: hypot função para calcular a hipotenusa'
print('O valor do Cateto oposto é {} e do Cateto adjacente é {} a medida da hipotenusa vale {:.2f}'.format(co, ca, hi))
