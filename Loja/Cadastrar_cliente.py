from rich import print

class Cliente:
    def __init__(self, nome, idade, rg, email):
        self.nome = nome
        self.idade = idade
        self.rg = rg
        self.email = email

    def boas_vindas(self):
        return f'\nSeja bem vindo em nossa loja online {self.nome}\n'


p1 = Cliente('Guilherme', 25, '471.440.758-96', 'gr1077882gmail.com')
print(p1.boas_vindas())

def mostrar_p():
    print(f'{'Produtos da loja':^30}')
    lista = [
    {'nome': 'Iphone Pro Max', 'valor': '12.000,00'},
    {'nome': 'Processador','valor': '299,00'},
    {'nome': 'Placa Mãe', 'valor': '799,00'},
    {'nome': 'Pc gamer', 'valor': '1.980,00'},
    {'nome': 'Tecaldo', 'valor': '78,99'}
]
    for n, c in enumerate(lista):
        print(f'{n+1} = {c['nome']:<17} R${c['valor']}')

mostrar_p()

while True:
    try:
        r = int(input('\nInforme o produto interessado ou digite (999 para encerear)? '))
    except (TypeError, ValueError):
        print('[bold italic red]Valor inválido, tente novamente, por favor![/]')
    else:
        break
    print('-' *45)
    