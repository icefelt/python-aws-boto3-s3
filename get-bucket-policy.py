import boto3

# Retrieve the policy of the specified bucket
s3 = boto3.client('s3')
result = s3.get_bucket_policy(Bucket='BUCKET_NAME')
print(result['Policy'])