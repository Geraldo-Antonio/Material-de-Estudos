class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        nota = int(input("Digite um valor de 0 a 10: "))
        if nota > 10:
            raise InputError("O valor da nota não pode ser maior que 10.")
        if nota < 10:
            raise InputError("O valor da nota não pode ser menor que 10.")
    except ValueError:
        print("Valor ínvalido.")
    except InputError as ex:
        print(ex)
    else:
        break