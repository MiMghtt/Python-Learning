import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))

    print(response.status_code)

    print(response.json())

    dados_cep = response.json()
    print(dados_cep['logradouro'])



if __name__ == '__main__':
    retorna_dados_cep('01001000')
