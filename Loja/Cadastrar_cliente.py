class Cliente:
    def __init__(self, nome, idade, rg, email):
        self.nome = nome
        self.idade = idade
        self.rg = rg
        self.email = email

    def boas_vindas(self):
        return f'Seja bem vindo em nossa loja online {self.nome}'


p1 = Cliente('Guilherme', 25, '471.440.758-96', 'gr1077882gmail.com')
print(p1.boas_vindas())


