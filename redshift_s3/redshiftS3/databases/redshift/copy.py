# copy.py
# arn:aws:iam::608811887288:role/Redshift_to_s3
copy_command ="""copy product_cost
from 's3://nhowlada-unload-redshift-10000002/product/products.csv'
CREDENTIALS 'aws_access_key_id=AKIAY3QAEFK4LQGEN62M;aws_secret_access_key=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'
region us-east-2;"""

copy_command2 =f"""copy product_cost
from 's3://nhowlada-unload-redshift-10000002/products.csv'
CREDENTIALS 'aws_access_key_id=AKIAY3QAEFK4LQGEN62M;aws_secret_access_key=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';"""