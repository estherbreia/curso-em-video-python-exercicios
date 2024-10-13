print('Faça um programa que leia a largura e altura de uma parede em metros, '
      'calcule sua área e a quantidade de tinta necessária para pinta-la.'
      '\nSabendo que cada 1 litro de tinta pinta uma área de 2m².')
l = float(input('Largura em Metros: '))
a = float(input('Altura em Metros: '))
area = l * a
print('Área: {:.3f} m² \nTinta: {:.2f} litros'.format(area, area/2))
