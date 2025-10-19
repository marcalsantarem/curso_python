# EXERCICIO 
# 
# Criar cálculo para o IMC e exibir a mensagem
#
# nome = 'Marçal Santarém'
# altura = 1.75
# peso = 120
# imc = ...
#
# Marçal Santarém tem 1.75 de altura,
# pesa 120 quilos e seu IMC é
# ?????????

nome = 'Marçal Santarém'
altura = 1.75
peso = 120
imc = 120 / altura ** 2 # IMC = peso / altura ao quadrado

print(nome, 'tem', altura, 'de altura, pesa', peso, 'quilos e seu IMC é', imc)
