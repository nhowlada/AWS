#!/usr/bin/python

# config.py
from configparser import ConfigParser

__all__=['get_config']


def get_config(path=None, filename='redshift.ini', section='default'):
    # path validator
    if path is None:
        raise "You must provide the path variable!"
    # create a configuration file path
    con_path = path + filename
    
    # create a parser
    parser = ConfigParser()

    # read config file
    parser.read(con_path)

    # get user defined section or default
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db