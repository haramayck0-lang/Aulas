hora = input('Qual é a hora atual? ')
if hora.isdigit():
    hora = int(hora)
    if 0 <= hora < 24:
        if hora < 11:
            print('Bom dia!')
        elif hora < 18:
            print('Boa tarde!')
        else:
            print('Boa noite!')
    else:
        print('Por favor, digite um número inteiro entre 0 e 23 para a hora.')
else:
    print('Por favor, digite um número inteiro para a hora.')