import json
import requests
import random
import datetime

from environ import Env
from gerador.core import gerapessoa

env = Env()

QUANTIDADE_PESSOAS = 100
POINT = env('POINT')


def criar_dados():
    criar_pessoas()


def criar_pessoas():
    for index in range(QUANTIDADE_PESSOAS):
        cidadao = gerapessoa()
        endereco = requests.post(
            POINT + '/endereco/',
            json={
                "rua": cidadao['endereco']['logradouro'],
                "numero": cidadao['endereco']['numero'],
                "cidade": cidadao['endereco']['cidade'],
                "estado": cidadao['endereco']['uf'],
                "cep": cidadao['endereco']['cep']
            },
            headers={'Content-Type': 'application/json'}
        )

        def _idade(data_nascimento):
            ano_nasceu = int(data_nascimento.split('/')[-1])
            ano_atual = datetime.datetime.now().year
            return ano_atual - ano_nasceu

        dados = {
            "nome": cidadao['nome'],
            "cpf": cidadao['documentos']['cpf'],
            "idade": _idade(cidadao['nascimento']),
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
            print ('Pessoa Criada: {}'.format(index + 1))
        else:
            print('Erro ao criar pessoa')

if __name__ == "__main__":
    criar_dados()
