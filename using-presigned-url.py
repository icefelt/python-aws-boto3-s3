import requests    # To install: pip install requests

'''
The user can download the S3 object by entering the presigned URL in a browser. 
A program or HTML page can download the S3 object by using the presigned URL as part of an HTTP GET request.
The following code demonstrates using the Python requests package to perform a GET request.
'''

url = create_presigned_url('BUCKET_NAME', 'OBJECT_NAME')
if url is not None:
    response = requests.get(url)