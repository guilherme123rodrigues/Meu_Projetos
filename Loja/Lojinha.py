from rich import print
from rich.panel import Panel
from time import sleep

class Cliente:
    def __init__(self, nome, idade, rg):
        self.nome = nome
        self.idade = idade
        self.rg = rg


    def boas_vindas(self):
        return Panel(f'Seja bem vindo em nossa loja online {self.nome}', width= 50)

    def tchau(self):
        return Panel(f'Volte sempre {self.nome}! ;)', width = 40)


# Função para análisar se o usuária vai digitar o valor errado, com tratamento de erro ('try/except', e 'if/else')
# Um loop caso ocorra a digitação incorreta ('while')
def analisar(p, qnt):
    linha(37)
    while True:
        try:
            r = int(input(p))
        except (ValueError, TypeError):
            print('[bold red italic]Valor invalido![/]')
        else:
            if r >= 1 and r <= qnt:
                linha(37)
                return r
            else:
                print('[bold red italic]Valor invalido![/]')
        linha(37) 
    

def registro():
    
    print(Panel('Site para pessoas c/ ou mais de 18 anos'.center(50), width=50))
    l = []
    
    while True:
        try:
            idade = int(input('Idade: '))
        except (ValueError, TypeError):
            print('[bold red italic]valor inválido![/]')
        else:
            if idade < 18:
                print(Panel('Infelizmente esse site é apenas para pessoas com ou mais de 18 anos.\n' \
                'Volte quando tiver com 18 ou mais, tchau!', width = 50))
                break
            else:
                break
            
    if idade >= 18:

        nome = str(input('Nome: ')).strip().title()

        while True:
            try:
                cpf = str(input('CPF: ')).strip()
            except (ValueError, TypeError):
                print('[bold red italic]Valor inválido![/]')
            else:
                if len(cpf) != 11:
                    print(Panel(f'O CPF tem que conter 11 digios, você digitou {len(cpf)} digito(s)', width= 50))
                else:
                    break
            sleep(2.5)

        l = [nome, idade, cpf]
        return l
    else:
        f = False
        return f

# Função para printar linhas de separação
def linha(tamanho=37):
    print('-'*tamanho)


# Mostrar o nome da categoria e dos produtos na tela
def mostrar(r):
        
    # cat vai receber a lista que está no índice r-1, suponhamos que r esteja com o valor 2, então r vai valer 1, por causa da subração de 2-1.
    cat = item[r-1][0]
        
    print(Panel(f'{cat.center(80)}', width= 80))
        
    # Esse faz igual o da variavel ('cat')
    prod = item[r-1][1]
        
    # Vai printar na tela os produtos da lista com os dicionarios
    c = 1
    linha(80)
    for itens in prod:
        if c != 2:
            print(f'{itens['nome']:<25} R${itens['valor']:,.2f}', end = '\t| ')
            c += 1
        else:
            print(f'{itens['nome']:<25} R${itens['valor']:,.2f}')
            c -= 1
    print()
    linha(80)

dados = registro()

if dados == False:
    sleep(3.5)
    exit
else:
    p1 = Cliente(dados[0], dados[1], dados[2])
    print(p1.boas_vindas())

    print(Panel(f'{'Aqui temos as seguintes categorias'.center(50)}', width=(50)))

    # Lista c/ dicionarios
    item = [
            
                    #Categoria Moveis
                [
                    'Moveis',
                    [
                        {'nome': 'Guarda-louça', 'valor': 1_999},
                        {'nome': 'Cama de solteiro', 'valor': 1_399},
                        {'nome': 'Cadeira gamer', 'valor': 799},
                        {'nome': 'Sofá', 'valor': 2_500},
                        {'nome': 'Mesa de jantar', 'valor': 1_800},
                        {'nome': 'Cadeira', 'valor': 300},
                        {'nome': 'Guarda-roupa', 'valor': 2_200},
                        {'nome': 'Cama casal', 'valor': 2_000},
                        {'nome': 'Estante', 'valor': 900},
                        {'nome': 'Rack TV', 'valor': 850},
                        {'nome': 'Mesa de escritório', 'valor': 1_200},
                        {'nome': 'Poltrona', 'valor': 1_100},
                        {'nome': 'Armário', 'valor': 2_000}
                    ]
                ],
                    
                    # Categoria Eletronico
                [
                    'Tecnologia',
                    [
                        {'nome': 'Placa mãe', 'valor': 1_199},
                        {'nome': 'Tapete para computador', 'valor': 39},
                        {'nome': 'Monitor 21 polegadas', 'valor': 899},
                        {'nome': 'Notebook', 'valor': 4_500},
                        {'nome': 'Smartphone', 'valor': 3_000},
                        {'nome': 'Tablet', 'valor': 2_000},
                        {'nome': 'Precessador', 'valor': 299},
                        {'nome': 'Teclado mecânico', 'valor': 500},
                        {'nome': 'Mouse gamer', 'valor': 300},
                        {'nome': 'Headset', 'valor': 400},
                        {'nome': 'Impressora', 'valor': 700},
                        {'nome': 'SSD 1TB', 'valor': 600}, 
                        {'nome': 'Placa de vídeo', 'valor': 3_500}
                ]
            ],
                    
                    # Categoria Eletrodomestico
                [
                    'Eletrodomesticos',
                    [
                        {'nome': 'Forno a lenha', 'valor': 1_199},
                        {'nome': 'Maquina de lavar 12k', 'valor': 2_399},
                        {'nome': 'Geladeira', 'valor': 3_299},
                        {'nome': 'Freezer', 'valor': 3_500},
                        {'nome': 'Micro-ondas', 'valor': 700},
                        {'nome': 'Máquina de lavar', 'valor': 2_800},
                        {'nome': 'Fogão', 'valor': 1_500},
                        {'nome': 'Air fryer', 'valor': 600},
                        {'nome': 'Liquidificador', 'valor': 200},
                        {'nome': 'Batedeira', 'valor': 400},
                        {'nome': 'Aspirador de pó', 'valor': 900},
                        {'nome': 'Forno elétrico', 'valor': 800}, 
                        {'nome': 'Ventilador', 'valor': 250}
                    
                    ]
                ]
        ]
            
    for n, cate in enumerate(item):
            print(f'{n+1} = {cate[0]}')

        # Loop até o usuário querer sair
    while True:
        # Vai chamar a função pra fazer o análise de erro, para o usúario digitar correamente
        resp = analisar('Qual categoria você quer ver? ', 3)
            
        # Vai printar na tela, a categoria e seus produtos
        mostrar(resp)
            
        # Vai análisar se o usuário quer ou não continuar, e ja vai verificar se vai ter digitação incorreta
        p = analisar('Quer continuar vendo as outras categorias [1 para (SIM)] ou [2 para (NÃO)]? ', 2)
        
        # Chegando aqui, ele vai ver se o usuário quer ou não continuar  
        if not p == 1:
            # chama a função da classe para o encerrameno do sistema
            print(p1.tchau())
            sleep(3.5)
            break