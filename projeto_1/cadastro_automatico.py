import json
import os
import random
from faker import Faker

fake = Faker('pt_BR')  # Faker configurado para português do Brasil

arquivo = 'usuarios.json'

# Função para carregar dados existentes
def carregar_dados():
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf8') as file:
            return json.load(file)
    return []

# Função para salvar dados
def salvar_dados(dados):
    with open(arquivo, 'w', encoding='utf8') as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)

# Função para criar um cadastro aleatório no formato desejado
def gerar_cadastro():
    nome = fake.first_name()
    idade = int(random.randint(18, 65))
    salario = int(random.randint(1500, 10000))
    cpf = fake.cpf().replace('.', '').replace('-', '')
    pais = 'Brasil'
    cidade = fake.city()
    estado = fake.estado_sigla()
    return {
        "nome": nome,
        "idade": idade,
        "salário": salario,
        "cpf": cpf,
        "país": pais,
        "cidade": cidade,
        "estado": estado
    }

# Quantidade de cadastros que deseja criar
qtd_cadastros = int(input("Quantos cadastros deseja gerar? "))

# Carrega dados já existentes
dados_usuarios = carregar_dados()

# Gera e adiciona cadastros novos
for _ in range(qtd_cadastros):
    novo = gerar_cadastro()
    dados_usuarios.append(novo)

# Salva tudo no arquivo JSON
salvar_dados(dados_usuarios)

print(f'{qtd_cadastros} cadastros gerados e salvos no arquivo {arquivo}')
