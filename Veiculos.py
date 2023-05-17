'''
Crie uma classe base chamada Veiculo com os seguintes atributos:
• marca: marca do veículo (string)
• modelo: modelo do veículo (string)
• ano: ano de fabricação do veículo (int)

A classe Veiculo deve ter os seguintes métodos:
• acelerar(): exibe a mensagem "Acelerando o veículo!"
• frear(): exibe a mensagem "Freando o veículo!"

Crie três classes derivadas da classe Veiculo:
• Carro: com os atributos adicionais:
• cor: cor do carro (string) A classe Carro deve ter os seguintes métodos adicionais:
• ligar_radio(): exibe a mensagem "Ligando o rádio do carro!"
• abrir_porta(): exibe a mensagem "Abrindo a porta do carro!"

• Moto: com os atributos adicionais:
• cilindrada: cilindrada da moto (string) A classe Moto deve ter os seguintes métodos
adicionais:
• empinar(): exibe a mensagem "Empinando a moto!"
• buzinar(): exibe a mensagem "Buzinando a moto!"

• Caminhao: com os atributos adicionais:
• carga_maxima: capacidade máxima de carga do caminhão (string) A classe
Caminhao deve ter os seguintes métodos adicionais:
• carregar(): exibe a mensagem "Carregando o caminhão!"
• descarregar(): exibe a mensagem "Descarregando o caminhão!"

'''

class Veiculo():
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano


    def acelerar(self):
        print('Acelerando o veículo!')

    def frear(self):
        print('Freando o veículo!')


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self._cor = cor

    def ligar_radio(self):
        print('Ligando rádio')

    def abrir_porta(self):
        print('Abrindo porta')


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self._cilindrada = cilindrada

    def empinar(self):
        print('Empinando a moto!')

    def buzinar(self):
        print('Buzinando a moto!')


class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_max):
        super().__init__(marca, modelo, ano)
        self._carga_max = carga_max

    def carregar(self):
        print("Carregando o caminhão!")

    def descarregar(self):
        print("Descarregando o caminhão!")


carro = Carro("Ford", "Mustang", 2022, "Vermelho")
print("Carro:")
print("Marca:", carro._marca)
print("Modelo:", carro._modelo)
print("Ano:", carro._ano)
print("Cor:", carro._cor)
carro.acelerar()
carro.frear()
carro.ligar_radio()
carro.abrir_porta()

print()

moto = Moto("Honda", "CBR500R", 2021, "500cc")
print("Moto:")
print("Marca:", moto._marca)
print("Modelo:", moto._modelo)
print("Ano:", moto._ano)
print("Cilindrada:", moto._cilindrada)
moto.acelerar()
moto.frear()
moto.empinar()
moto.buzinar()

print()

caminhao = Caminhao("Volvo", "FH16", 2020, "30 toneladas")
print("Caminhão:")
print("Marca:", caminhao._marca)
print("Modelo:", caminhao._modelo)
print("Ano:", caminhao._ano)
print("Carga Máxima:", caminhao._carga_max)
caminhao.acelerar()
caminhao.frear()
caminhao.carregar()
caminhao.descarregar()