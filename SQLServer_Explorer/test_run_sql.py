from run_sql import run_sql_query

context_path = 'context.txt'

def safe_write(msg):
    with open(context_path, 'a', encoding='utf-8') as f:
        f.write(msg + '\n')
        f.flush()

with open(context_path, 'w', encoding='utf-8') as f:
    f.write('---\nExploring AdventureWorks2022.HumanResources schema\n')

queries = [
    # 1. List all tables in HumanResources schema
    ("Tables in HumanResources schema:", "SELECT TABLE_NAME FROM AdventureWorks2022.INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'HumanResources' AND TABLE_TYPE = 'BASE TABLE';"),
    # 2. Count of tables in HumanResources
    ("Number of tables in HumanResources:", "SELECT COUNT(*) FROM AdventureWorks2022.INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'HumanResources' AND TABLE_TYPE = 'BASE TABLE';"),
    # 3. List all columns for each table
    ("Columns in each HumanResources table:", "SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE FROM AdventureWorks2022.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'HumanResources';"),
    # 4. List all primary keys in HumanResources
    ("Primary keys in HumanResources:", "SELECT KU.TABLE_NAME, KU.COLUMN_NAME FROM AdventureWorks2022.INFORMATION_SCHEMA.TABLE_CONSTRAINTS AS TC JOIN AdventureWorks2022.INFORMATION_SCHEMA.KEY_COLUMN_USAGE AS KU ON TC.CONSTRAINT_TYPE = 'PRIMARY KEY' AND TC.CONSTRAINT_NAME = KU.CONSTRAINT_NAME WHERE KU.TABLE_SCHEMA = 'HumanResources';"),
    # 5. List all foreign keys in HumanResources
    ("Foreign keys in HumanResources:", "SELECT f.name AS FK_name, OBJECT_NAME(f.parent_object_id) AS TableName, COL_NAME(fc.parent_object_id,fc.parent_column_id) AS ColumnName, OBJECT_NAME (f.referenced_object_id) AS RefTableName, COL_NAME(fc.referenced_object_id,fc.referenced_column_id) AS RefColumnName FROM AdventureWorks2022.sys.foreign_keys AS f INNER JOIN AdventureWorks2022.sys.foreign_key_columns AS fc ON f.object_id = fc.constraint_object_id WHERE OBJECT_SCHEMA_NAME(f.parent_object_id) = 'HumanResources';"),
    # 6. List all indexes in HumanResources
    ("Indexes in HumanResources:", "SELECT t.name AS TableName, ind.name AS IndexName, ind.type_desc AS IndexType FROM AdventureWorks2022.sys.indexes ind INNER JOIN AdventureWorks2022.sys.tables t ON ind.object_id = t.object_id WHERE SCHEMA_NAME(t.schema_id) = 'HumanResources';"),
    # 7. Row count for each table
    ("Row count for each table:", "SELECT t.name AS TableName, SUM(p.rows) AS RowCounts FROM AdventureWorks2022.sys.tables t INNER JOIN AdventureWorks2022.sys.schemas s ON t.schema_id = s.schema_id INNER JOIN AdventureWorks2022.sys.partitions p ON t.object_id = p.object_id WHERE s.name = 'HumanResources' AND p.index_id IN (0,1) GROUP BY t.name ORDER BY t.name;"),
    # 8. List all unique constraints
    ("Unique constraints in HumanResources:", "SELECT t.name AS TableName, i.name AS IndexName FROM AdventureWorks2022.sys.indexes i INNER JOIN AdventureWorks2022.sys.tables t ON i.object_id = t.object_id WHERE i.is_unique = 1 AND SCHEMA_NAME(t.schema_id) = 'HumanResources';"),
    # 9. List all default constraints
    ("Default constraints in HumanResources:", "SELECT t.name AS TableName, c.name AS ColumnName, d.name AS DefaultConstraintName, d.definition FROM AdventureWorks2022.sys.default_constraints d INNER JOIN AdventureWorks2022.sys.columns c ON d.parent_object_id = c.object_id AND d.parent_column_id = c.column_id INNER JOIN AdventureWorks2022.sys.tables t ON t.object_id = d.parent_object_id WHERE SCHEMA_NAME(t.schema_id) = 'HumanResources';"),
    # 10. List all check constraints
    ("Check constraints in HumanResources:", "SELECT t.name AS TableName, cc.name AS CheckConstraintName, cc.definition FROM AdventureWorks2022.sys.check_constraints cc INNER JOIN AdventureWorks2022.sys.tables t ON cc.parent_object_id = t.object_id WHERE SCHEMA_NAME(t.schema_id) = 'HumanResources';"),
    # 11. List all triggers
    ("Triggers in HumanResources:", "SELECT t.name AS TableName, tr.name AS TriggerName FROM AdventureWorks2022.sys.triggers tr INNER JOIN AdventureWorks2022.sys.tables t ON tr.parent_id = t.object_id WHERE SCHEMA_NAME(t.schema_id) = 'HumanResources';"),
    # 12. List all views in HumanResources
    ("Views in HumanResources:", "SELECT TABLE_NAME FROM AdventureWorks2022.INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'HumanResources';"),
    # 13. List all stored procedures in HumanResources
    ("Stored procedures in HumanResources:", "SELECT name FROM AdventureWorks2022.sys.procedures WHERE SCHEMA_NAME(schema_id) = 'HumanResources';"),
    # 14. List all functions in HumanResources
    ("Functions in HumanResources:", "SELECT name FROM AdventureWorks2022.sys.objects WHERE type IN ('FN', 'IF', 'TF') AND SCHEMA_NAME(schema_id) = 'HumanResources';"),
    # 15. List all columns with identity property
    ("Identity columns in HumanResources:", "SELECT t.name AS TableName, c.name AS ColumnName FROM AdventureWorks2022.sys.columns c INNER JOIN AdventureWorks2022.sys.tables t ON c.object_id = t.object_id WHERE c.is_identity = 1 AND SCHEMA_NAME(t.schema_id) = 'HumanResources';"),
]

try:
    # Remove USE statement, fully qualify all objects
    safe_write('Using fully qualified AdventureWorks2022 schema.')
    for idx, (desc, query) in enumerate(queries, 1):
        safe_write(f"\nQuery {idx}: {desc}")
        try:
            results = run_sql_query(query)
            if not results:
                safe_write("No results.")
            else:
                for row in results:
                    safe_write(str(row))
        except Exception as e:
            safe_write(f"ERROR: {e}")
except Exception as e:
    safe_write(f"Script failed: {e}")

# Get all table names in HumanResources
query_tables = "SELECT TABLE_NAME FROM AdventureWorks2022.INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'HumanResources' AND TABLE_TYPE = 'BASE TABLE';"
tables = run_sql_query(query_tables)
table_names = [t[0] for t in tables]

safe_write('\n---\nColumns for each table in HumanResources:')
for table in table_names:
    safe_write(f'\nTable: {table}')
    try:
        col_query = f"""
        SELECT COLUMN_NAME, DATA_TYPE
        FROM AdventureWorks2022.INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA = 'HumanResources' AND TABLE_NAME = '{table}'
        """
        cols = run_sql_query(col_query)
        for col, dtype in cols:
            safe_write(f'- {col}: {dtype}')
    except Exception as e:
        safe_write(f'ERROR: {e}')

# Look for relationships (foreign keys) between tables
safe_write('\n---\nForeign key relationships in HumanResources:')
try:
    fk_query = '''
    SELECT OBJECT_NAME(f.parent_object_id) AS TableName,
           COL_NAME(fc.parent_object_id,fc.parent_column_id) AS ColumnName,
           OBJECT_NAME (f.referenced_object_id) AS RefTableName,
           COL_NAME(fc.referenced_object_id,fc.referenced_column_id) AS RefColumnName
    FROM AdventureWorks2022.sys.foreign_keys AS f
    INNER JOIN AdventureWorks2022.sys.foreign_key_columns AS fc
        ON f.object_id = fc.constraint_object_id
    WHERE OBJECT_SCHEMA_NAME(f.parent_object_id) = 'HumanResources';
    '''
    fks = run_sql_query(fk_query)
    if not fks:
        safe_write('No foreign key relationships found.')
    else:
        for row in fks:
            safe_write(str(row))
except Exception as e:
    safe_write(f'ERROR: {e}')
