decisao = ('sim')
while decisao == ('sim'):
    num = int(input('Digite o número da tabuada que deseja: '))
    x = 1
    print('Tabuada do número:', num)
    while x <= 10:
        print(num,'x', x, '=', num * x)
        x = x+1
        print('Deseja calcular outra tabuada? ')
    decisao = str(input('Digite "sim" para continuar e "nao" para sair: '))
print('Obrigado pela colaboração')
