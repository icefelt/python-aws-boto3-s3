# Disable thread use/transfer concurrency
config = TransferConfig(use_threads=False)

s3 = boto3.client('s3')
s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME', Config=config)