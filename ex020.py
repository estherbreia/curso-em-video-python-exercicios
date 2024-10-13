#Exercício 20 - Faça um programa que leia o nome de quatros alunos e mostre a ordem sorteada.

from random import shuffle
print('SORTEIO \nDigite o nome dos alunos:' )
a = str(input('1: '))
b = str(input('2: '))
c = str(input('3: '))
d = str(input('4: '))
all = [a, b, c, d]
shuffle(all)
print('A ordem de apresentação será: {}' .format(all))