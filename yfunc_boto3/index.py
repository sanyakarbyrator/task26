import boto3
import datetime
import requests

def handler(event, context):
    s3 = boto3.client(
        's3',
        aws_access_key_id='ТВОЙ_КЛЮЧ',
        aws_secret_access_key='ТВОЙ_СЕКРЕТ',
        endpoint_url='https://storage.yandexcloud.net'
    )

    url = 'https://nginx.ddns.net/'
    response = requests.get(url)
    status = response.status_code
    timestamp = datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    body = f"{timestamp} {url} {status}"

    s3.put_object(
        Bucket='ahecker-logs',
        Key=f'logs/{timestamp}.txt',
        Body=body
    )

    return {'status': status}
