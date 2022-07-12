class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def soma(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def multi(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
def contador_de_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

if __name__ == '__main__':
    print(Calculadora(25, 5).multi())
