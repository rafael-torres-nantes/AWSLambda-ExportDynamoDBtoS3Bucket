# 📤 AWS Lambda - Exportação de Dados do DynamoDB para S3

## Índice

* [📚 Contextualização do projeto](#-contextualização-do-projeto)
* [🛠️ Tecnologias/Ferramentas utilizadas](#%EF%B8%8F-tecnologiasferramentas-utilizadas)
* [🖥️ Funcionamento do sistema](#%EF%B8%8F-funcionamento-do-sistema)
* [📁 Estrutura do projeto](#estrutura-do-projeto)
* [📌 Como executar o projeto](#como-executar-o-projeto)

## 📚 Contextualização do projeto

Este projeto tem como objetivo exportar dados de uma tabela do DynamoDB para um bucket S3. A aplicação foi desenvolvida para ser executada como uma função Lambda na AWS, facilitando a automação do processo de exportação de dados.

## 🛠️ Tecnologias/Ferramentas utilizadas

[<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">](https://www.python.org/)
[<img src="https://img.shields.io/badge/Boto3-0073BB?logo=amazonaws&logoColor=white">](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[<img src="https://img.shields.io/badge/Dotenv-ECD53F?logo=dotenv&logoColor=white">](https://pypi.org/project/python-dotenv/)

## 🖥️ Funcionamento do sistema

A aplicação é composta por três principais componentes:

1. **Serviço DynamoDB**: Implementado na classe [`DynamoDBClass`](export_to_s3/dynamo_services.py), responsável por exportar os dados da tabela DynamoDB para um arquivo JSON e fazer o upload para o S3.
2. **Função Lambda**: Definida em [`lambda_handler.py`](lambda_handler.py), que inicializa o serviço DynamoDB e chama o método de exportação.
3. **Utilitários**: Funções auxiliares para verificação de credenciais AWS e importação de variáveis de ambiente, localizadas em [`utils/check_aws.py`](utils/check_aws.py) e [`utils/import_credentials.py`](utils/import_credentials.py).

## 📁 Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

```
.
├── .env
├── .env.example
├── .gitignore
├── export_to_s3/
│   ├── __pycache__/
│   ├── dynamo_services.py
│   ├── lambda_handler.py
│   └── main.py
├── readme.md
└── utils/
    ├── __pycache__/
    ├── check_aws.py
    └── import_credentials.py
```

## 📌 Como executar o projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Instale as dependências:**
   ```bash
   pip install boto3 python-dotenv
   ```

3. **Configure as variáveis de ambiente:**
   Crie um arquivo `.env` baseado no `.env.example` e preencha com suas credenciais AWS e informações da tabela DynamoDB e bucket S3.

4. **Execute a função Lambda localmente:**
   ```bash
   python export_to_s3/lambda_handler.py
   ```

Isso iniciará o processo de exportação dos dados da tabela DynamoDB para o bucket S3 especificado.
