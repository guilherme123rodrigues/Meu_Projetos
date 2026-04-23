# Calculo do IMC, massa corporal

class Imc:
    t = 'Calculo de massa corporal'
    def __init__(self, n, p, a):
        self.nome = n
        self.peso = p
        self.altura = a / 100 # converte cm -> metros
    
    def calc(self):
        imc = float(f'{self.peso / (self.altura ** 2):.2f}')
        print('-'*45)
        print(f'Seu IMC(Indíce de massa corporal) é de {imc}')

        if imc < 18.5:
            return '\033[1;31mSeu IMC está Abixo do Peso\033[m'
        elif 18.5 <= imc <= 24.9:
            return '\033[1;32mSeu IMC está no peso Normal\033[m'
        elif 25.0 <= imc <= 29.9:
            return '\033[1;33mSeu IMC está Sobrepeso\033[m'
        elif 30.0 <= imc <= 34.9:
            return '\033[1;31mSeu IMC está Obesidade grau I\033[m'
        elif 35.0 <= imc <= 39.9:
            return '\033[1;31mSeu IMC está Obesidade grau II\033[m'
        else:
            return '\033[1;31mseu IMC está Obesidade grau III\033[m'
    
    
p1 = Imc('Guilherme', 95, 177)
print(f'{p1.calc()}')
print('-'*45)