import requests
import jsonpath

# GET Fornecedores
headers = { 'Authorization': 'Token f880d513b87904cfb290ccb967e43a931cba1fac' }
fornecedores = requests.get(url='http://127.0.0.1:8000/api/v1/fornecedores/', headers=headers)

resultados = jsonpath.jsonpath(fornecedores.json(), 'results')
print(resultados)

resultados2 = jsonpath.jsonpath(fornecedores.json(), 'results[0]')
print(resultados2)

resultados3 = jsonpath.jsonpath(fornecedores.json(), 'results[0].descricao')
print(resultados3)

resultados4 = jsonpath.jsonpath(fornecedores.json(), 'results[*].descricao')
print(resultados4)