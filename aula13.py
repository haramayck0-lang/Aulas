nome = input('Digite seu nome: ')
altura = float(input('Digite sua altura: '))   
peso = 59
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)