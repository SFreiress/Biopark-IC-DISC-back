# Manipulação de Números Romanos com Orientação a Objetos
# Neste exercício, você criará uma classe chamada NumeroRomano que permitirá manipular números romanos 
# e realizar conversões entre números decimais e romanos.
# A classe NumeroRomano possui os seguintes métodos:
# __init__(self, valor): O construtor deve receber um número decimal inteiro e armazená-lo como um atributo `valor` da instância.
# para_romano(self): Este método deve retornar uma string contendo a representação do número decimal em algarismos romanos.
# para_decimal(self): Este método deve retornar o valor decimal correspondente ao número romano armazenado na instância.
# Você também deve implementar um método de classe chamado de_romano(cls, romano) que receberá uma string contendo um número romano 
# e retornará uma instância de NumeroRomano correspondente.

class NumeroRomano:
    def __init__(self, valor):
        self.decimal = valor
        self.romano = ''

    def para_romano(self):
        romanos = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

        romano = ''
        decimal_romano = self.decimal

        for valor, simbolo in romanos.items():
            while decimal_romano >= valor:
                romano += simbolo
                decimal_romano -= valor

        self.romano = romano
        return romano

    def para_decimal(self):
        romanos = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        decimal = 0
        valor_prev = 0

        for simbolo in reversed(self.romano):
            valor = romanos[simbolo]
            if valor < valor_prev:
                decimal -= valor
            else:
                decimal += valor
            valor_prev = valor

        return decimal

    @classmethod
    def de_romano(cls, romano):
        romanos = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        decimal = 0
        valor_prev = 0

        for simbolo in reversed(romano):
            valor = romanos[simbolo]
            if valor < valor_prev:
                decimal -= valor
            else:
                decimal += valor
            valor_prev = valor
            retorno = NumeroRomano(decimal)
            retorno.para_romano()

        return retorno

numero1 = NumeroRomano(1983)
romano1 = numero1.para_romano()
decimal1 = numero1.para_decimal()

print(f"Número decimal: {numero1.decimal}")
print(f"Conversão para número romano: {romano1}")

numero2 = NumeroRomano.de_romano("MCMXCIV")
decimal2 = numero2.para_decimal()

print(f"Número romano: {numero2.romano}")
print(f"Conversão para decimal: {decimal2}")