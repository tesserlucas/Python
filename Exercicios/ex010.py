largura=float(input('Digite a largura em metros: '))
altura=float(input('Digite a altura metros : '))
area = largura*altura
tinta = area*1/2
print('Sua parede tem dimensões {}x{} e uma area de {} m²'.format(largura, altura, area))
print('Você irá precisar de {:.2f} litros de tinta para pintar a parede'.format(tinta))
