def maior (*num): 
    tam = len(num) 
    m = max(num)
    print('-='*30)
    print('Analisando os valores passado...')
    print(f'Recebi os valores {num} e são ao todos {tam} números')
    print(f'O maior valor informado foi {m}')
    print('-='*30)

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(5)
maior(0)