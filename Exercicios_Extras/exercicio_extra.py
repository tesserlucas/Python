marido = str(input('Qual é o nome completo do homem ? ')).strip()
esposa = str(input('Qual é o nome completo da mulher ? ')).strip()
contar = len((marido + esposa).replace(" ",""))
print('O nome do {} tem {} letras'.format(marido,len((marido.replace(" ","")))))
print('O nome da {} tem {} letras'.format(esposa,len((esposa.replace(" ","")))))
print('O total de letras entre \033[34m{}\033[m e \033[35m{}\033[m é de \033[31m{} letras\033[m'.format(marido,esposa,contar))
if contar % 2 == 0:
    print('O resultado é um número PAR')
    print('O Homem perde')
else:
    print('O resultado é um número ÍMPAR')
    print('A mulher perde')
