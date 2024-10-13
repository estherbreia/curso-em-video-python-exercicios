#Exercício 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno e cosseno e tangente desse ângulo')

import math
ang = float(input('Digite um ângulo de uma circunferência (0º a 360º): '))
angrd = math.radians(ang)
seno = math.sin(angrd)
cos = math.cos(angrd)
tang = math.tan(angrd)
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}'.format(seno , cos , tang ))