import requests

headers = {'Authorization': 'Token f880d513b87904cfb290ccb967e43a931cba1fac'}

url_base_fornecedores = 'http://127.0.0.1:8000/api/v1/fornecedores/'

fornecedor_atualizado = {
    'descricao': 'Fornecedor New att',
    'email': 'fornecedornew@gmail.com',
    'telefone': '8198876654'
}

resultado = requests.put(url=f'{url_base_fornecedores}6/', headers=headers, data=fornecedor_atualizado)

assert resultado.status_code == 200

assert resultado.json()['descricao'] == fornecedor_atualizado['descricao']