def escrever_texto(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(texto)
    arquivo.close()


def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write('\n'+texto)
    arquivo.close()


def ler_arquivo(arquivo):
    arquivo = open(arquivo, 'r')
    texto = arquivo.read()
    print(texto)


if __name__ == '__main__':
    escrever_texto('Primeira linha')
    atualizar_arquivo('Segunda linha')
    ler_arquivo('teste.txt')
