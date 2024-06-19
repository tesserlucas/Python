palavra = ('APRENDER','PROGRAMAR','ENSINAR','PYTHON','CRUSO','PRATICAR',
          'MERCADO','PROGRAMADOR' )
for c in palavra:
    print(f'\nNa palavra {c} temos ', end='')
    for letra in c: #para cada letra na palavra c
        if letra.lower() in 'aeiou': 
            print(letra, end=' ') 