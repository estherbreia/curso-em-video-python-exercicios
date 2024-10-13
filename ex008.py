print('Escreve um programa que leia um valor em metro e o exiba convertido em centimetros e milimetros')
m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000
print('Metros: {}m \nCentimetros: {:.0f}cm \nMilimetros: {:.0f}mm'.format(m, cm, mm))



