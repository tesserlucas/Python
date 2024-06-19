nome = str(input('Qual o seu nome completo ? ')).strip().title()
n = nome.split()
print("Seu primeiro nomme é {}".format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
