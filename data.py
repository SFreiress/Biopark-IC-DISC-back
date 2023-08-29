# Exercício de Programação: Manipulação de Datas com Orientação a Objetos
# Neste exercício, você irá criar uma classe chamada Data que representa 
# datas no formato dia/mês/ano. Além disso, você implementará métodos de sobrescrita,
#  como __add__, __sub__ e __eq__, para realizar operações de adição e subtração de datas, além de comparar igualdade entre datas.
# A classe Data possui os seguintes atributos:
# dia: um inteiro representando o dia (valor entre 1 e 30).
# mês: um inteiro representando o mês (valor entre 1 e 12).
# ano: um inteiro representando o ano.
# Você deverá implementar os seguintes métodos na classe:
# 1. __str__: Este método deve retornar uma string no formato "dd/mm/aaaa"
# 2. __add__(self, other): Este método deve permitir a adição de datas. 
# O parâmetro other será outra instância da classe Data. 
# O método deve retornar uma nova instância de Data resultante da adição das datas.
# 3. __sub__(self, other): Este método deve permitir a subtração de datas. 
# O parâmetro other será outra instância da classe Data. 
# O método deve retornar uma nova instância de Data resultante da subtração das datas.
# 4. __eq__(self, other): Este método deve comparar se duas instâncias da classe Data são iguais. 
# O parâmetro other será outra instância da classe Data. O método deve retornar True se as datas forem iguais e False caso contrário.
# Você deve testar a sua classe e os métodos implementados criando instâncias da classe Data 
# e realizando operações de adição, subtração e comparação entre datas. 
# Certifique-se de lidar adequadamente com as mudanças de meses e anos durante as operações de adição e subtração.

class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"
    
    def __add__(self, other):
        dia_novo = self.dia + other.dia
        mes_novo = self.mes + other.mes
        ano_novo = self.ano + other.ano

        if dia_novo > 30:
            dia_novo -= 30
            dia_novo += 1

        if mes_novo > 12:
            mes_novo -= 12
            ano_novo += 1

        return Data(dia_novo, mes_novo, ano_novo)
    
    def __sub__(self, other):
        dia_novo = self.dia - other.dia
        mes_novo = self.mes - other.mes
        ano_novo = self.ano - other.ano

        if dia_novo <= 0:
            dia_novo += 30
            mes_novo -= 1

        if mes_novo <= 0:
            mes_novo += 12
            ano_novo -= 1

        return Data(dia_novo, mes_novo, ano_novo)
    
    def __eq__(self, other):
        return (self.dia == other.dia and
                self.mes == other.mes and
                self.ano == other.ano)
        

data1 = Data(25, 8, 2023)
data2 = Data(2, 9, 2023)
data3 = Data(10, 12, 1983)

data4 = data1 + data2
data5 = data1 - data2

print(data4)
print(data5)

print(data1 == data2)
print(data1 == data3)