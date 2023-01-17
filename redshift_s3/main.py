import redshiftS3.utilities as utilities
from redshiftS3.databases import redshift
from redshiftS3.utilities import config
from redshiftS3 import s3

copy_right = True
unload_right = False
bucket_list = False
table_record = False
bucket_single = False

# Read configuration from the .ini
params_redshift = config.get_config(path='redshiftS3/config/', filename='redshift.ini', section='redshift')
params_s3 = config.get_config(path='redshiftS3/config/', filename='s3.ini', section='s3_nhowlada')


# Fetch record from redshift table
if table_record:
    # get data from the redshift
    respose = utilities.get_extract(redshift.sel_tran_fact_stage, params_redshift)
    # print(respose.fetchall())


# get the buxcket list from s3
if bucket_list:
    buckets = s3.get_buckets(params=params_s3)
    # print(buckets)

# Unload data from Redshift to s3 
if unload_right:
    bucket = s3.get_bucket(params=params_s3)
    bucket_name = params_s3['bucket']

    if bucket:
        print("Bucket exist!")
        print(f"Unloading data to the existing bucket {bucket_name}")
        respose = utilities.get_unload(redshift.unload, params_redshift)
        print(f"Unloading done to the bucket {bucket_name}")

    else:
        print("Bucket does not exist!")
        print(f"Creating new bucket {bucket_name}")
        new_bucket = s3.create_bucket(params=params_s3)
        
        if new_bucket:
            print(f"Bucket Created {bucket_name}")
        else:
            print(f"Erro, while bucket Creating {bucket_name}")

# Copy data from s3 to Redshift
if copy_right:
    print(redshift.copy_command)
    respose = utilities.get_copy(redshift.copy_command, params_redshift)

#print(buckets['Buckets'])

# create a bucket
# check bucket name exist or not
# if bucket not exist then create a new one otherwise use the existing one

# unload ('select * from venue')
# to 's3://mybucket/tickit/unload/venue_' 
# iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'
# parallel off;



  


