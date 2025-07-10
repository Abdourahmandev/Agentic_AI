from run_sql import run_sql_query

context_path = 'context.txt'

with open(context_path, 'a', encoding='utf-8') as f:
    f.write('\n---\nExploring AdventureWorks2022.HumanResources schema\n')

# Switch to AdventureWorks2022 database
run_sql_query("USE AdventureWorks2022;")

# 1. List all tables in HumanResources schema
query_tables = '''
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_SCHEMA = 'HumanResources' AND TABLE_TYPE = 'BASE TABLE';
'''
tables = run_sql_query(query_tables)
table_names = [t[0] for t in tables]

with open(context_path, 'a', encoding='utf-8') as f:
    f.write('Tables in HumanResources:\n')
    for t in table_names:
        f.write(f'- {t}\n')

# 2. Get record count for each table (limit to 15 tables)
record_counts = {}
for table in table_names[:15]:
    count_query = f"SELECT COUNT(*) FROM HumanResources.[{table}]"
    count = run_sql_query(count_query)[0][0]
    record_counts[table] = count

with open(context_path, 'a', encoding='utf-8') as f:
    f.write('\nRecord counts for HumanResources tables:\n')
    for table, count in record_counts.items():
        f.write(f"- {table}: {count} records\n")

# 3. Get columns and data types for each table (limit to 15 tables)
columns_info = {}
for table in table_names[:15]:
    col_query = f'''
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'HumanResources' AND TABLE_NAME = '{table}'
    '''
    cols = run_sql_query(col_query)
    columns_info[table] = cols

with open(context_path, 'a', encoding='utf-8') as f:
    f.write('\nColumns and data types for HumanResources tables:\n')
    for table, cols in columns_info.items():
        f.write(f"\n{table}:\n")
        for col, dtype in cols:
            f.write(f"- {col}: {dtype}\n")
