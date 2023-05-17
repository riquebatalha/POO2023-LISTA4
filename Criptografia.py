'''
Desenvolva uma classe base chamada Criptografia que contenha os métodos cifrar e decifrar. Essa
classe servirá como base para as subclasses CifraCesar e CifraXor, que implementarão algoritmos
de criptografia específicos.
A classe Criptografia terá os seguintes métodos:
• Método cifrar(texto): Este método receberá um texto como entrada e retornará o texto
cifrado de acordo com o algoritmo de criptografia. Cada subclasse irá implementar sua
própria lógica de cifragem.
• Método decifrar(texto_cifrado): Este método receberá um texto cifrado como entrada e
retornará o texto original decifrado de acordo com o algoritmo de criptografia
correspondente.
A classe CifraCesar herda da classe Criptografia e implementa o algoritmo de criptografia conhecido
como Cifra de César. A Cifra de César desloca cada letra do texto original um número fixo de posições
no alfabeto para cifrar e decifrar o texto.
A classe CifraXor herda da classe Criptografia e implementa o algoritmo de criptografia usando a
operação XOR (OU exclusivo). Nesse algoritmo, cada caractere do texto original é combinado com uma
chave usando a operação XOR para obter o texto cifrado. A operação XOR também é usada para decifrar
o texto cifrado, combinando-o novamente com a mesma chave.
Os métodos cifrar e decifrar de cada subclasse devem ser implementados de acordo com a lógica
específica de cada algoritmo de criptografia.
'''

class Criptografia:
    def cifrar(self, texto):
        pass

    def decifrar(self, texto_cifrado):
        pass

class CifraCesar(Criptografia):
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento

    def cifrar(self, texto):
        texto_cifrado = ""
        for letra in texto:
            if letra.isalpha():
                codigo = ord(letra.upper())
                codigo_cifrado = (codigo - 65 + self.deslocamento) % 26 + 65
                texto_cifrado += chr(codigo_cifrado)
            else:
                texto_cifrado += letra
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        texto_decifrado = ""
        for letra in texto_cifrado:
            if letra.isalpha():
                codigo = ord(letra.upper())
                codigo_decifrado = (codigo - 65 - self.deslocamento) % 26 + 65
                texto_decifrado += chr(codigo_decifrado)
            else:
                texto_decifrado += letra
        return texto_decifrado


class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for caractere in texto:
            codigo = ord(caractere)
            codigo_cifrado = codigo ^ self.chave
            texto_cifrado += chr(codigo_cifrado)
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        texto_decifrado = ""
        for caractere in texto_cifrado:
            codigo = ord(caractere)
            codigo_decifrado = codigo ^ self.chave
            texto_decifrado += chr(codigo_decifrado)
        return texto_decifrado


texto_original = "Texto original"
chave_cesar = 3
chave_xor = 42

cifra_cesar = CifraCesar(chave_cesar)
texto_cifrado_cesar = cifra_cesar.cifrar(texto_original)
texto_decifrado_cesar = cifra_cesar.decifrar(texto_cifrado_cesar)

cifra_xor = CifraXor(chave_xor)
texto_cifrado_xor = cifra_xor.cifrar(texto_original)
texto_decifrado_xor = cifra_xor.decifrar(texto_cifrado_xor)

print("Texto original:", texto_original)
print("Texto cifrado (Cifra de César):", texto_cifrado_cesar)
print("Texto decifrado (Cifra de César):", texto_decifrado_cesar)

print()

print("Texto original:", texto_original)
print("Texto cifrado (Cifra XOR):", texto_cifrado_xor)
print("Texto decifrado (Cifra XOR):", texto_decifrado_xor)
