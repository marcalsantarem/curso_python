nome = 'Marçal Santarém'
altura = 1.75
peso = 120
imc = 120 / altura ** 2 # IMC = peso / altura ao quadrado

# print(nome, 'tem', altura, 'de altura,')
# print('pesa', peso, 'quilos e seu IMC é')
# print(imc)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
