n = input('Digite algo: ')
print("É número ? {}".format(n.isnumeric()))
print("Está em maiúsculas ?", n.isupper())
print('Está em minúsculas ?', n.islower())
print('É alfabético ?', n.isalpha())
print(type(n))
print('Está capitalizada ?', n.istitle())
