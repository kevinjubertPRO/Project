import os
"""
This python script to generate an sql script to create sql table 
from the copy of .csv file in the source folder
"""

import pandas as pd


# -- FILE PATHS
absolute_path = os.path.abspath('.').replace('\\', '/')
source_filepath = os.path.join(absolute_path, 'data', 'dataset')
destination_filepath = os.path.join('.', 'data', 'sql-query')

files = os.listdir(source_filepath)
files = list(filter(lambda x: x.endswith('.csv'), files))

# -- SQL TABLE
sql_table_name = 'netflix'

# MAPPING TABLE
type_mapping_dict = {
    'int64': 'int',
    'float64': 'real',
    'object': 'text'
}


# -- GENERATE SQL SCRIPT
type_mapping = f'CREATE SCHEMA {sql_table_name};\n'

for file in files:

    absolute_path = os.path.abspath(os.path.join('.', 'data', 'dataset', file)).replace('\\', '/')

    table_name = f'{sql_table_name}.{sql_table_name}_' + file.replace('.csv', '')
    type_mapping += f'CREATE TABLE {table_name} (\n'

    df = pd.read_csv(os.path.join('.', 'data', 'dataset', file), encoding='utf-8')

    temp_mapping = ''
    for col in df.columns:
        temp_mapping += f'\t{col.replace(" ","_")} {type_mapping_dict[str(df[col].dtypes)]},\n'

    type_mapping += temp_mapping[:-2]+'\n'
    type_mapping += f""");\nCOPY {table_name} FROM '{absolute_path}' WITH CSV HEADER DELIMITER ',';\n\n"""

print(type_mapping)


# --  WRITE SQL SCRIPT
with open(destination_filepath + '\create_netflix_tables.sql','w+') as file:
    file.write(type_mapping)