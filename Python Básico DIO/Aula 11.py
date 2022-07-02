from unittest import main
import os



if __name__ == "__main__":
    lista = [10 , 5]
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
    arquivo = open("notas.txt", "r")
    try:
        divisao = 10/1
        numero = lista[1]
        x = 1
    except ZeroDivisionError:
        print("Não é possivel realizar um divisão por zero")
    except IndexError:
        print("Valor fora da lista")
    except BaseException as error:
        print(f"Valor desconhecido: '{error}'")
    else:
        print("Executa quando não ocorre exeção")
    finally:
        print("Sempre executa")
        print(arquivo.read())