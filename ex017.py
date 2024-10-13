#Exercício 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo e mostre o comprimento da hipotenusa')

import math
print('HIPOTENUSA')
print('Considerar um triângulo retangulo')
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente: '))
hi = math.hypot(co, ca)
print('O comprimento da Hipotenusa é: {:.2f}' .format(hi))