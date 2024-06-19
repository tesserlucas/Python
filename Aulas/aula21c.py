#Exemplo com escopo de variáveis

def funcao(b):
    global a #Esse global é para que a variável 'A' seja reconhecida fora da função.
    a = 8 #Aqui o a é uma variável global, ou seja, existe fora da função.
    b = b + 4 #Aqui o b é uma variável local, ou seja, só existe dentro da função.
    c= 2 #Aqui o c é uma variável local, ou seja, só existe dentro da função.
    print(f'A dentro vale {a}') #vai imprimir 8, pois a variável a foi alterada dentro da função.
    print(f'B dentro vale {b}') #vai imprimir 6, pois a variável b foi alterada dentro da função.
    print(f'C dentro vale {c}') #vai imprimir 2, pois a variável c foi criada dentro da função.

a = 2
funcao(a)
print(f'A fora vale {a}') #vai imprimir 8 pois foi usado o camando global dentro da função.a