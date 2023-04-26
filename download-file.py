import boto3

s3 = boto3.client('s3')
s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')

"""
The download_fileobj method accepts a writeable file-like object. 
The file object must be opened in binary mode, not text mode.

s3 = boto3.client('s3')
with open('FILE_NAME', 'wb') as f:
    s3.download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)
"""
