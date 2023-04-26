# Define the website configuration
website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
}

# Set the website configuration
s3 = boto3.client('s3')
s3.put_bucket_website(Bucket='BUCKET_NAME',
                      WebsiteConfiguration=website_configuration)