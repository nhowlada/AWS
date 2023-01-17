# unload.py
import datetime

unload = f"""unload ('SELECT * FROM cards_ingest.tran_fact_stage')
to 's3://nhowlada-unload-redshift-10000002/users_{str(datetime.datetime.now())}.csv'
CREDENTIALS 'aws_access_key_id=AKIAY3QAEFK4LQGEN62M;aws_secret_access_key=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'
parallel off
csv;"""