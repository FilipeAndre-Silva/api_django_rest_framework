import requests

headers = {'Authorization': 'Token f880d513b87904cfb290ccb967e43a931cba1fac'}

url_base_fornecedores = 'http://127.0.0.1:8000/api/v1/fornecedores/'

resultado = requests.get(url=url_base_fornecedores, headers=headers)

print(resultado.json())

assert resultado.status_code == 200

assert resultado.json()['count'] == 4

assert resultado.json()['results'][0]['descricao'] == 'vitaflocos'