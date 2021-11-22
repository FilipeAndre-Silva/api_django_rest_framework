import requests

# GET Fornecedores
headers = { 'Authorization': 'Token f880d513b87904cfb290ccb967e43a931cba1fac' }
fornecedor = requests.get(url='http://127.0.0.1:8000/api/v1/fornecedores/', headers=headers)

print(fornecedor.status_code) # retorna o status code da requisição

print(fornecedor.json()) # retorna no formato dict

print(fornecedor.json()['count']) # acessando a propriedade count da páginação
print(fornecedor.json()['next']) # acessando o link para póxima página

print(fornecedor.json()['results']) # retonar uma lista dos resultados da requisição
print(fornecedor.json()['results'][0]) # acessando o primeiro elemento da lista de resultados
print(fornecedor.json()['results'][0]['descricao'])