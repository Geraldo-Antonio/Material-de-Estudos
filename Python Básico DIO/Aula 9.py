import shutil

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


def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_notas = arquivo.read()
    aluno_notas = aluno_notas.split('\n')
    lista_media = []
    for aluno in aluno_notas:
        notas = aluno.split(',')
        aluno_nome = notas[0]
        notas.pop(0)
        media = lambda notas: sum([int(x) for x in notas]) / 4
        print('O aluno, {}, obeteve tais notas, {}, sua média final foi, {}.'.format(aluno_nome, notas, media(notas)))
        lista_media.append({aluno_nome: media(notas)})
    return lista_media


def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/')


def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/')


if __name__ == '__main__':
    print(media_notas('notas.txt'))
    #copia_arquivo('.\\Python Básico DIO\\notas.txt')
