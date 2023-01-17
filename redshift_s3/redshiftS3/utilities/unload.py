# Unload.py

#!/usr/bin/python
# extract.py
import datetime
import psycopg2
import sqlalchemy as sa
import pandas as pd
from .config import get_config

__all__=['get_unload']

def get_unload(query, params):
    '''
    Functions unload data from Resdshift database using UNLOAD command
            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''

    
    # Connect to the Redshift database server
    engine = sa.create_engine(f"redshift+psycopg2://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}")

    # Create a connection
    try:
        connection = engine.connect();
        print(" Redshift connected!")
    except:
        print(" Redshift not connected!")

    # Uload a table from the readshift to s3
    try:
        res = connection.execute(query)
    except:
        print("Something Worng to retriveing data from the redshift!")

    # # Insert into a New Table
    # res = df.to_sql("tran_fact_stage",engine,"cards_ingest",if_exists='append', index=False)
    # print(f" Records inserted: {res}")
    # connection.close()
    return res