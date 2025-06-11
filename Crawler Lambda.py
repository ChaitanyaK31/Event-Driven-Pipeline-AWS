import boto3

def lambda_handler(event, context):

    region = 'us-east-1'
    crawler_name = 'crawler-projectedp'

    glue_client = boto3.client('glue', region_name=region)

    glue_client.start_crawler(Name=crawler_name)
   

