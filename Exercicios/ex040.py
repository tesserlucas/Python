print('-'*30)
print('\033[31mINDICE DE MASSA CORPORAL')
print('\033[m-'*30)
nome = input('Digite o nome da pessoa: ')
peso = float(input('Qual é o peso do {} ? (KG) '.format(nome)))
altura = float(input('Qual é a altura do {} ? (m) '.format(nome)))
imc = peso/(altura**2)
print('{} seu IMC é {:.1f}'.format(nome,imc))
if imc < 18.5:
    print('O {} está abaixo do peso'.format(nome))
elif imc >=18.5 and imc <25:
    print('O {} está com o peso ideal'.format(nome))
elif imc >=25 and imc <30:
    print('O {} está com sobrepeso'.format(nome))
elif imc >= 30 and imc < 40:
    print('O {} está com obesidade'.format(nome))
else:
    print('O {} está com obesidade mórbida'.format(nome))
