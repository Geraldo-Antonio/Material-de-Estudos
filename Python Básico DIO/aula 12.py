import requests


def retorna_dados_cep(cep):
    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    print(response.status_code)
    print(response.text)
    dados_cep = response.json()
    print(dados_cep["uf"])
    return dados_cep


def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    retorna_dados_cep("01001000")
    print(retorna_response("https://www.youtube.com"))
