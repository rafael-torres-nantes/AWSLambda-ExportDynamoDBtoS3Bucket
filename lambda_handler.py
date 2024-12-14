import os
from dotenv import load_dotenv
from export_to_s3.dynamo_services import DynamoDBClass

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Nome da tabela DynamoDB e bucket S3 onde os logs serão registrados
DYNAMODB_TABLE = os.getenv('DYNAMODB_TABLE')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

# --------------------------------------------------------------------
# Função Lambda que exporta a tabela do DynamoDB para o S3
# --------------------------------------------------------------------
def lambda_handler(event, context):
    """
    Função Lambda que exporta a tabela DynamoDB para o S3.
    
    :param event: Dados do evento recebido (não utilizado neste contexto).
    :param context: Contexto de execução da Lambda (não utilizado).
    :return: Status do processamento (sucesso ou erro).
    """
    try:
        # Inicializa o serviço DynamoDB
        dynamodb_service = DynamoDBClass(DYNAMODB_TABLE)
        
        # Exporta a tabela para o S3
        dynamodb_service.export_dynamodb_to_s3(S3_BUCKET_NAME, 'teste.json')

        return {'statusCode': 200, 'body': 'Exportação para S3 realizada com sucesso'}

    except Exception as e:
        # Captura e retorna erros
        print(f"Erro ao exportar tabela: {e}")
        return {'statusCode': 500, 'body': f'Erro: {e}'}