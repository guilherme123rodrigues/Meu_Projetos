from rich import print

class Cliente:
    def __init__(self, nome, idade, rg, email):
        self.nome = nome
        self.idade = idade
        self.rg = rg
        self.email = email

    def boas_vindas(self):
        return f'\nSeja bem vindo em nossa loja online {self.nome}.\n'


p1 = Cliente('Guilherme', 25, '471.440.758-96', 'gr1077882gmail.com')
print(p1.boas_vindas())

print(f'{'Aqui temos as seguintes categorias'.center(37, '-')}')

# Lista c/ dicionarios
item = [
    
            #Categoria Moveis
        [
            'Moveis',
            [
                {'nome': 'Guarda-roupa', 'valor': 2_999},
                {'nome': 'Messa', 'valor': 399},
                {'nome': 'Cadeira', 'valor': 299}
            ]
        ],
            
            # Categoria Eletronico
        [
            'Tecnologia',
            [
                {'nome': 'Teclado', 'valor': 99},
                {'nome': 'Mause', 'valor': 39},
                {'nome': 'Monitor 21 polegadas', 'valor': 899}
            ]
        ],
            
            # Categoria Eletrodomestico
        [
            'Eletrodomestico',
            [
                {'nome': 'Micro-ondas', 'valor': 899},
                {'nome': 'Maquina de kavar 12k', 'valor': 2_399},
                {'nome': 'Geladeira', 'valor': 3_299}
            ]
        ]
]
    
for n, cate in enumerate(item):
    print(f'{n+1} = {cate[0]}')

# Loop até o usuário querer sair
while True:

    # Função para análisar se o usuária vai digitar o valor errado, com tratamento de erro ('try/except', e 'if/else')
    # Um loop caso ocorra a digitação incorreta ('while')
    def analisar(p, qnt):
        print('-'*37)
        while True:
            try:
              r = int(input(p))
            except (ValueError, TypeError):
                print('[bold red italic]Valor invalido![/]')
            else:
                if r >= 1 and r <= qnt:
                    print('-'*37)
                    return r
                else:
                    print('[bold red italic]Valor invalido![/]')
            print('-'*37) 
     
    # Mostrar o nome da categoria e dos produtos na tela
    def mostrar(r):
        
        # cat vai receber a lista que está no índice r-1, suponhamos que r esteja com o valor 2, então r vai receber 1.
        cat = item[r-1][0]
        
        print(f'\n{cat.center(37, '-')}')
        
        # Esse faz igual o da variavel ('cat')
        prod = item[r-1][1]
        
        # Vai printar na tela os produtos da lista com os dicionarios
        for itens in prod:
            print(f'{itens['nome']:<25} R${itens['valor']:,.2f}')
        print('-'*37)

    # Vai chamar a variavel pra fazer o análise de erro, para o usúario não digitar errado
    resp = analisar('Qual categoria você quer ver? ', 3)
    
   # Vai printar na tela, a categorio e seus produtos
    mostrar(resp)
    
    # Vai análisar se o usuário quer ou não continuar, e ja vai verificar se vai ter digitação incorreta
    p = analisar('Quer continuar vendo as outras categorias [1 para (SIM)] ou [2 para (NÃO)]? ', 2)
  
    # Chegando aqui, ele vai ver se o usuário quer ou não continuar  
    if not p == 1:
        break
    else:
        print('-'*37)
