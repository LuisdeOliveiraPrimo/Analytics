import json
import os

# Nome do arquivo
arquivo = 'usuarios.json'

# Se existir, carrega os dados; se não, cria uma lista vazia
if os.path.exists(arquivo):
    with open(arquivo, 'r', encoding='utf8') as file:
        dados_usuarios = json.load(file)
else:
    dados_usuarios = []

# Cadastro
print('CADASTRO')

nome = input('Nome: ')
idade = input('Idade: ')
salario = input('Salário: ')
cpf = input('CPF: ')
pais = input('País: ')
cidade = input('Cidade: ')
estado = input('Estado: ')

# Dados do novo usuário
novo_usuario = {
    "nome": nome,
    "idade": idade,
    "salário": salario,
    "cpf": cpf,
    "país": pais,
    "cidade": cidade,
    "estado": estado
}

# Adiciona o novo usuário à lista
dados_usuarios.append(novo_usuario)

# Salva novamente no arquivo JSON
with open(arquivo, 'w', encoding='utf8') as file:
    json.dump(dados_usuarios, file, indent=4, ensure_ascii=False)

print('Cadastro salvo com sucesso!')
