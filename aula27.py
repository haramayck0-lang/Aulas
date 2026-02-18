try:
    numero = int(input('Digite um número: '))
    if numero == 0:
        print('O número é zero')
    elif numero % 2 == 0:
        print('Número par')
    else:
        print('Número ímpar')
except ValueError:
    print('Esse número não é inteiro')