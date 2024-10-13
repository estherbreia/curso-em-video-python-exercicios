#Exercício 16 - Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira (ex:Digite um número : 6.127. O número 6.127 tem a parte inteira 6)

num = float(input('Digite um número real: '))
num2 = int(num)
print('O número {}, tem a parte inteira {}.'.format(num, num2))

