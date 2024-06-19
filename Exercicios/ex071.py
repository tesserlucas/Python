n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
n3 = int(input('3º número: '))
n4 = int(input('4º número: '))
t = (n1,n2,n3,n4) # isso seria a tupla
print(t)
print(f'O número 9 apareceu {t.count(9)} vezes')
if 3 in t: # significa que se o 3 estiver dentro de t ele imprimi a posição se não diz que não foi digitado o 3
    print(f'O primeiro valor 3 foi digitado na posição {t.index(3)+1}')
else: 
    print('Nenhum valor 3 foi digitado')
print('Os valores pares são: ' , end='')
for n in t:
    if n % 2 == 0:
        print(n, end=' ')
