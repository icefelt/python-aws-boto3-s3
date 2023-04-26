import boto3

s3_client = boto3.client(
    service_name='s3',
    endpoint_url='https://accesspoint.vpce-abc123-abcdefgh.s3.us-east-1.vpce.amazonaws.com'
)