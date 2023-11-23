import os
import openpyxl
import pandas as pd

# -- SCHEMA OF THE DATABASE
schema_db = 'netflix'.lower()


# -- FILE PATHS
absolute_path = os.path.abspath('.').replace('\\', '/')
source_filepath = os.path.join(absolute_path, 'data', 'dataset')
destination_filepath = os.path.join('.', 'data', 'sql-query')

# MAPPING TABLE
mapping_table = {
    'int64': 'int',
    'float64': 'real',
    'object': 'text'
}



files = os.listdir(source_filepath)
# files = list(filter(lambda x: x.endswith('.csv') or x.endswith('.xlsx'), files))
print(files)

xl_files = list(filter(lambda x: x.endswith('.xls') or x.endswith('.xlsx'), files))
csv_files = list(filter(lambda x: x.endswith('.csv'), files))

print(xl_files)
print(csv_files)


# -- GENERATE SQL SCRIPT
def create_csv_to_sql(schema_db, mapping_table, files):
    type_mapping = f'CREATE SCHEMA {schema_db.lower()};\n'

    for file in files:

        absolute_path = os.path.abspath(os.path.join('.', 'data', 'dataset', file)).replace('\\', '/')

        table_name = f'{schema_db}.{schema_db}_' + file.replace('.csv', '')
        type_mapping += f'CREATE TABLE IF NOT EXISTS {table_name} (\n'

        df = pd.read_csv(f'./data/dataset/{file}', encoding='utf-8')
        # print(df)

        temp_mapping = ''
        for col in df.columns:
            temp_mapping += f'\t{col} {mapping_table[str(df[col].dtypes)]},\n'

        type_mapping += temp_mapping[:-2]+'\n'
        type_mapping += f""");\nCOPY {table_name} FROM '{absolute_path}' WITH CSV HEADER DELIMITER ',' ENCODING 'UTF-8';\n\n"""

        print(type_mapping)

    return type_mapping


# --  WRITE SQL SCRIPT
with open(destination_filepath + f'\create_{schema_db}_tables.sql','w+') as file:
    file.write(create_csv_to_sql(schema_db, mapping_table, csv_files))

#print(create_csv_to_sql(schema_db, mapping_table, csv_files))


openpyxl.load_workbook(os.join.path('.', 'data', 'dataset'))