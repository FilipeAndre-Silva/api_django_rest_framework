import requests


class TestFornecedor:
    url_base_fornecedores = 'http://127.0.0.1:8000/api/v1/fornecedores/'
    headers = {'Authorization': 'Token f880d513b87904cfb290ccb967e43a931cba1fac'}

    def test_get_fornecedores(self):
        resultado = requests.get(url=self.url_base_fornecedores, headers=self.headers)

        assert resultado.status_code == 200
        assert resultado.json()['count'] == 7
        assert resultado.json()['results'][0]['descricao'] == 'vitaflocos'

    def test_get_fornecedor(self):
        resultado = requests.get(url=f'{self.url_base_fornecedores}3', headers=self.headers)

        assert resultado.status_code == 200
        assert resultado.json()['descricao'] == 'vitaflocos'