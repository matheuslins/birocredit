import json
import requests
import random
from environ import Env
from cidadaobr import CidadaoBrasileiro


env = Env()

QUANTIDADE_PESSOAS = 1
POINT = env('POINT')


def criar_dados():
    criar_pessoas()


def criar_pessoas():
    for _ in range(QUANTIDADE_PESSOAS):
        cidadao = CidadaoBrasileiro()
        endereco = requests.post(
            POINT + '/endereco/',
            json={
                "rua": cidadao.endereco.logradouro,
                "numero": cidadao.endereco.numero,
                "cidade": cidadao.endereco.cidade,
                "estado": cidadao.endereco.estado,
                "cep": cidadao.endereco.cep
            },
            headers={'Content-Type': 'application/json'}
        )
        dados = {
            "nome": cidadao.nome,
            "cpf": cidadao.cpf,
            "idade": cidadao.idade,
            "fonte_renda": "Trabalho",
            "endereco": endereco.json()['id']
        }
        pessoa = requests.post(
            POINT + '/pessoas/',
            data=json.dumps(dados),
            headers={'Content-Type': 'application/json'}
        )
        tipos_bens = ['apartamento', 'carro', 'acao', 'casa']
        dados_bem_pessoa = {
            "pessoa": pessoa.json()['id'],
            "tipo": random.choice(tipos_bens),
            "valor": random.randrange(1000, 200000)
        }
        requests.post(
            POINT + '/bens/',
            data=json.dumps(dados_bem_pessoa),
            headers={'Content-Type': 'application/json'}
        )
        # TODO: Criar eventos
        if pessoa.status_code == 201:
            print ('Pessoa Criada')
        else:
            print('Erro ao criar pessoa')

if __name__ == "__main__":
    criar_dados()
