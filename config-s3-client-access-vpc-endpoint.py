import boto3

control_client = boto3.client(
    service_name='s3control',
    endpoint_url='https://control.vpce-abc123-abcdefgh.s3.us-east-1.vpce.amazonaws.com'
)