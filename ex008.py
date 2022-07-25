# Exercicio 8 escreva um programa que leia um valor em metros e converta em outras unidades de medida

metros = int(input('escreva uma distancia em metros:'))

print('a medida de {}.0m corresponde a:'.format(metros))
print('{}km'.format(metros/1000))
print('{}hm'.format(metros/100))
print('{}dam'.format(metros/10))
print('{}dm'.format(metros*10))
print('{}cm'.format(metros*100))
print('{}mm'.format(metros*1000))