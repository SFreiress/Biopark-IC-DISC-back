class NumeroRomano:
    def __init__(self, valor):
        self.valor = valor

    def para_romano(self):
        if not 1 <= self.valor <= 3999:
            return "Valor fora do intervalo válido (1-3999)"

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
        
        roman_num = ''
        i = 0
        while self.valor > 0:
            for _ in range(self.valor // values[i]):
                roman_num += symbols[i]
                self.valor -= values[i]
            i += 1
        return roman_num

# Exemplo de uso
numero = NumeroRomano(3549)
print(f"O número {numero.valor} em algarismos romanos é: {numero.para_romano()}")
