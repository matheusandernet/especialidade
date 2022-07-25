# Exercicio 4 faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

qualquer_coisa = (input('digite uma palavra:'))
print('o tipo primitivo desse valor é', (type(qualquer_coisa)))
print('Só tem espaços?', qualquer_coisa.isspace())
print('É um numero?', qualquer_coisa.isnumeric())
print('É alfabetico?', qualquer_coisa.isalpha())
print('É alfanumerico?', qualquer_coisa.isalnum())
print('Esta em letra maiuscula?', qualquer_coisa.isupper())
print('Esta em letra minuscula?', qualquer_coisa.islower())
