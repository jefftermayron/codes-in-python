a = 0
while (a == 0):
    login = input('Digite o seu login: ')
    senha = input('Digite sua senha: ')
    contagem = 0
    print('login em:')
    for contagem in range(1,11):
        print(contagem)
    if login == 'usuario' and senha == 'usuario':
        print('Bem vindo', login)
        a = 1
    else:
        print('Login falhou, tente novamente')
        a = 0
print('Oque você está pensando hoje?')
pensamento = input('')
print('Estou pensando em:', pensamento)
