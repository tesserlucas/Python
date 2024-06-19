while True:
    print("="*35)
    n = int(input('Quer ver a tabuada de qual valor ? '))
    print("="*35)
    if n < 0:
        break
    for c in range (1,11):
        print(f'{n} x {c} = {n*c}') 
print('\033[31m')
print('~'*20)
print('Tabuada Finalizada')
print('~'*20)
print('\033[m')
