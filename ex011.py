# Exercicio 11 faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de ttinta necessária para pintá-la, sabendo que cada lito da tinta pinta uma area de 2m2

largura = float(input('largura da parede:'))
altura = float(input('altura da parede'))
area=altura*largura
tinta=area/2
print('Sua parede tem a dimenssão de {}x{} e sua area é de {}'.format(largura,altura,area))
print('Para pintar essa parede, você precisaria de {}l de tinta.'.format(tinta))
