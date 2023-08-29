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
        self.valor = valor

    def para_romano(self):
        if not 1 < self.valor:
            return "Valor não pode ser negativo."
        
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
    
        num_roman = ''
        i = 0
        while self.valor > 0:
            for _ in range(self.valor // values[i]):
                num_roman += symbols[i]
                self.valor -= values[i]
            i += 1 
        return num_roman

    def para_decimal(self):
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]

        num_dec = ''
        i = 0
        while self.valor > 0:
            for _ in range(self.valor // symbols[i]):
                num_dec += values[i]
                self.valor -= symbols[i]
            i += 1
        return num_dec

    @classmethod
    def de_romano(cls, romano):
        pass

numero1 = NumeroRomano(5000)
romano1 = numero1.para_romano()
decimal1= numero1.para_decimal()

print(f"Número decimal: {numero1.valor}")
print(f"Número romano: {romano1}")
print(f"Conversão para decimal: {decimal1}")

numero2 = NumeroRomano.de_romano("MCMXCIV")
decimal2 = numero2.para_decimal()

print(f"Número romano: {numero2.valor}")
print(f"Conversão para decimal: {decimal2}")