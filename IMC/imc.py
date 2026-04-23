# Calculo do IMC, massa corporal

class Imc:
    t = 'Calculo de massa corporal'
    def __init__(self, n, p, a):
        self.nome = n
        self.peso = p
        self.altura = a
    
    def calc(self):
        return f'{self.altura / (self.peso ^ 2)}'

    
p1 = Imc('Guilherme', 65, 177)
print(f'{p1.calc()}')
