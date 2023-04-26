import boto3

# Retrieve the website configuration
s3 = boto3.client('s3')
result = s3.get_bucket_website(Bucket='BUCKET_NAME')