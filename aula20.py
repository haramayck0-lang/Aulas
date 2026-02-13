#operadores lógicos
#and, or, not
#and - todas as condições precisam ser verdadeiras
#se qualquer condição for falsa, o resultado será falso
#a expressão inteira será avaliada naquele valor
#São considerados falsy: 0, 0.0, '', False, [], (), {}, None
#usado para representar um valor

entrada = input('[E]entrar [S]air: ')

if entrada == 'E' :
    senha_digitada = input('Senha: ')
    if senha_digitada == '1234':
        print('Entrar')
    else:
        print('Senha incorreta')
else:
    print('Sair')