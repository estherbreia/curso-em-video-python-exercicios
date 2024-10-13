print('Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.')
s = float(input('Salário atual: R$ '))
aum = s+(s * 15 / 100)
print('Salário com aumento (15%): R$ {:.2f}'.format(aum))