# list_bucket.py

import boto3

# response = s3_client.create_bucket(Bucket='my-another-bucket-20000000000233', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

def get_buckets(params=None):
    """
    
    """
    # access and secret validator
    if params is None:
        raise "Must have access and sceret key in the file"

    if params['aws_access_key_id'] is None:
        raise "Must have access key in file!"
    
    if params['aws_secret_access_key'] is None:
        raise "Must have secret key in file!"

    # create a s3 client object
    s3 = boto3.client('s3', aws_access_key_id=params['aws_access_key_id'], aws_secret_access_key=params['aws_secret_access_key'])
    response = s3.list_buckets()
    # Output the bucket names
    print('Existing buckets:')
    buckets = [bucket["Name"] for bucket in response['Buckets']]
    
    return buckets

def get_bucket(params=None):
    """
    
    """
    bucket_name = params['bucket']
    access_key = params['aws_access_key_id']
    secret_key = params['aws_secret_access_key']
    # access and secret validator
    if params is None:
        raise "Must have access and sceret key in the file"

    if params['aws_access_key_id'] is None:
        raise "Must have access key in file!"
    
    if params['aws_secret_access_key'] is None:
        raise "Must have secret key in file!"

    # create a s3 client object
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
    response = s3.list_buckets()

    # Existing buckets:
    buckets = [bucket["Name"] for bucket in response['Buckets']]
    
    if bucket_name is not None and len(bucket_name.strip())>0:
        if bucket_name in buckets:
            return True

    return False