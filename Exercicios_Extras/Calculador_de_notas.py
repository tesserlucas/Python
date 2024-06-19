#print('Calculadora de Notas - UNISINOS')
#notaGA = float(input('Nota Grau A: '))
#media = (18 - notaGA)/2
#print(f'Para ser aprovado voce precisa tirar {media} no GB')

media = 0
for c in range(0,10):
    n = float(input(f'{c+1}ºNota: '))
    media = media + n
print(media)