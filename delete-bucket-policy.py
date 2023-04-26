# Delete a bucket's policy
s3 = boto3.client('s3')
s3.delete_bucket_policy(Bucket='BUCKET_NAME')