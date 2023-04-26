# To consume less downstream bandwidth, decrease the maximum concurrency
config = TransferConfig(max_concurrency=5)

# Download an S3 object
s3 = boto3.client('s3')
s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME', Config=config)