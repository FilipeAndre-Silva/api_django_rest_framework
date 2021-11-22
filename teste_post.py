import requests

headers = {'Authorization': 'Token f880d513b87904cfb290ccb967e43a931cba1fac'}

url_base_fornecedores = 'http://127.0.0.1:8000/api/v1/fornecedores/'

novo_fornecedor = {
    'descricao': 'Fornecedor New',
    'email': 'fornecedornew@gmail.com',
    'telefone': '8198876654'
}

resultado = requests.post(url=url_base_fornecedores, headers=headers, data=novo_fornecedor)

assert resultado.status_code == 201

assert resultado.json()['descricao'] == novo_fornecedor['descricao']