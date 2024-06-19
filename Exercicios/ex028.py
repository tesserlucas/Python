v = int(input('Qual a velocidade do carro ? '))
multa = (v - 80) * 7
print('Ele passou pelo radar a {} KM/h'.format(v))
if v > 80:
    print('Ele foi multado')
    print('O valor da multa foi de R$ {}'.format(multa))
else:
    print('Ele passou na velocidade correspondente da via')