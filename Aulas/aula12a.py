nome = str(input('Digite o nome: '))
if nome == 'Lucas':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == 'Paula':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Mariana Marina':
    print('Que belo nome feminino')
else:
    print('Seu nome é comum')
print('Tenha um Bom Dia {}'.format(nome))
