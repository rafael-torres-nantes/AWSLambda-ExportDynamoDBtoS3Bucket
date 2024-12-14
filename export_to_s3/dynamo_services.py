import boto3
import json
from botocore.exceptions import ClientError

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# RUN LOCALY
from utils.check_aws import AWS_SERVICES

aws_services = AWS_SERVICES()

session = aws_services.login_session_AWS()
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

class DynamoDBClass:
    def __init__(self, dynamodb_table_name):
        # Define o nome da tabela no DynamoDB
        self.dynamodb_table_name = dynamodb_table_name

        # Inicia a sessão do DynamoDB
        self.dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

        # Inicia a sessão do DynamoDB
        self.s3_client = session.client('s3', region_name='us-west-2')

    # Serviço de DynamoDB para registro de log
    def export_dynamodb_to_s3(self, bucket_name, s3_filename):
        """
        Exporta todos os itens da tabela DynamoDB para um arquivo no S3.
        
        :param bucket_name: Nome do bucket S3.
        :param s3_filename: Nome do arquivo a ser salvo no S3.
        :return: None
        """
        # Acessa a tabela do DynamoDB
        table = self.dynamodb.Table(self.dynamodb_table_name)

        try:
            # Scan para obter todos os itens da tabela
            response = table.scan()
            items = response.get('Items', [])

            # Continuar o scan caso existam mais itens (paginação)
            while 'LastEvaluatedKey' in response:
                response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                items.extend(response.get('Items', []))

            # Converte os itens para JSON
            json_data = json.dumps(items, indent=4, default=int)

            # Salva o JSON em um arquivo temporário local
            temp_filename = '/tmp/dynamodb_export.json'
            with open(temp_filename, 'w') as f:
                f.write(json_data)

            # Faz o upload do arquivo para o S3
            self.s3_client.upload_file(temp_filename, bucket_name, s3_filename)
            print(f"Exportação para S3 concluída: s3://{bucket_name}/{s3_filename}")

        except ClientError as e:
            print(f"Erro ao exportar a tabela do DynamoDB para o S3: {e}")
            raise  # Propaga o erro para que ele seja tratado na função Lambda
        except Exception as e:
            print(f"Erro inesperado: {e}")
            raise  # Propaga o erro para que ele seja tratado na função Lambda