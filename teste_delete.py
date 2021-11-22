import requests

headers = {'Authorization': 'Token f880d513b87904cfb290ccb967e43a931cba1fac'}

url_base_fornecedores = 'http://127.0.0.1:8000/api/v1/fornecedores/'

resultado = requests.delete(url=f'{url_base_fornecedores}6/', headers=headers)

assert resultado.status_code == 204

assert len(resultado.text) == 0