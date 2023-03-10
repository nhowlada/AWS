# unload.py
import datetime

unload = f"""unload ('SELECT * FROM cards_ingest.tran_fact_stage')
to 's3://nhowlada-unload-redshift-10000002/users_{str(datetime.datetime.now())}.csv'
CREDENTIALS 'aws_access_key_id=;aws_secret_access_key='
parallel off
csv;"""
