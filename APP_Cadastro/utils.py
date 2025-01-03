import requests

def APICEP(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    dados_API_CEP = response.json()

    cidade = dados_API_CEP.get('localidade')
    estado = dados_API_CEP.get('uf')
    bairro = dados_API_CEP.get('bairro')
    if bairro is None:
        bairro = 'Centro'
    dados_API_CEP = {
        'cidade': cidade,
        'estado': estado,
        'bairro': bairro
    }
    
    return dados_API_CEP