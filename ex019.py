# Exercício 19 - Um professsor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.')

from random import choice
print('SORTEIO')
print('Digite o nome dos alunos:')
a = input('1: ')
b = input('2: ')
c = input('3: ')
d = input('4: ')
all = [a, b, c, d]
sorteio = choice(all)
print('O aluno sorteado é: {}'.format(sorteio.upper()))

