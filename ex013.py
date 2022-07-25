# Exercicio 13 faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('qual o salário do funcionário?'))

print('um funcionário que ganhava R${}, com 15% de aumento vai ganhar {:.2f}'.format(salario, salario / 100 * 115))
