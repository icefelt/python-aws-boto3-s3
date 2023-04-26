# Define the configuration rules
cors_configuration = {
    'CORSRules': [{
        'AllowedHeaders': ['Authorization'],
        'AllowedMethods': ['GET', 'PUT'],
        'AllowedOrigins': ['*'],
        'ExposeHeaders': ['ETag', 'x-amz-request-id'],
        'MaxAgeSeconds': 3000
    }]
}

# Set the CORS configuration
s3 = boto3.client('s3')
s3.put_bucket_cors(Bucket='BUCKET_NAME',
                   CORSConfiguration=cors_configuration)