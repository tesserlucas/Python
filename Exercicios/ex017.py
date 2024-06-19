from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo me graus: '))
a = radians(angulo)
sen = sin(a)
cose = cos(a)
tg = tan(a)
print('O seno de {} é {:.2f}\nO cosseno de {} é {:.2f}\nA tangente de {} é {:.2f}'.format (angulo,sen,angulo,cose,angulo,tg))