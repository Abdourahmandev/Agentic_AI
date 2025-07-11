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

safe_write('\n---\nExploring data in HumanResources.Shift table:')

# Get all data from Shift table
try:
    query = "SELECT * FROM AdventureWorks2022.HumanResources.Shift;"
    results = run_sql_query(query)
    if not results:
        safe_write('No data found in Shift table.')
    else:
        # Write column headers
        col_query = "SELECT COLUMN_NAME FROM AdventureWorks2022.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'HumanResources' AND TABLE_NAME = 'Shift';"
        columns = [col[0] for col in run_sql_query(col_query)]
        safe_write(' | '.join(columns))
        for row in results:
            safe_write(' | '.join(str(item) for item in row))
        # Optionally, summarize the meaning of each column
        safe_write('\nColumn meanings:')
        safe_write('- ShiftID: Unique identifier for each shift.')
        safe_write('- Name: Name of the shift (e.g., Day, Night).')
        safe_write('- StartTime: Time the shift starts.')
        safe_write('- EndTime: Time the shift ends.')
        safe_write('- ModifiedDate: Last modification date.')
except Exception as e:
    safe_write(f'ERROR: {e}')

safe_write('\n---\nExploring data in HumanResources.Department table:')

# Get all data from Department table
try:
    query = "SELECT * FROM AdventureWorks2022.HumanResources.Department;"
    results = run_sql_query(query)
    if not results:
        safe_write('No data found in Department table.')
    else:
        # Write column headers
        col_query = "SELECT COLUMN_NAME FROM AdventureWorks2022.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'HumanResources' AND TABLE_NAME = 'Department';"
        columns = [col[0] for col in run_sql_query(col_query)]
        safe_write(' | '.join(columns))
        for row in results:
            safe_write(' | '.join(str(item) for item in row))
        # Optionally, summarize the meaning of each column
        safe_write('\nColumn meanings:')
        safe_write('- DepartmentID: Unique identifier for each department.')
        safe_write('- Name: Name of the department.')
        safe_write('- GroupName: Group to which the department belongs.')
        safe_write('- ModifiedDate: Last modification date.')
except Exception as e:
    safe_write(f'ERROR: {e}')

safe_write('\n---\nExploring data in HumanResources.Employee table:')

# Get all data from Employee table
try:
    query = "SELECT * FROM AdventureWorks2022.HumanResources.Employee;"
    results = run_sql_query(query)
    if not results:
        safe_write('No data found in Employee table.')
    else:
        # Write column headers
        col_query = "SELECT COLUMN_NAME FROM AdventureWorks2022.INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'HumanResources' AND TABLE_NAME = 'Employee';"
        columns = [col[0] for col in run_sql_query(col_query)]
        safe_write(' | '.join(columns))
        for row in results:
            safe_write(' | '.join(str(item) for item in row))
        # Optionally, summarize the meaning of each column
        safe_write('\nColumn meanings:')
        safe_write('- BusinessEntityID: Unique identifier for each employee.')
        safe_write('- NationalIDNumber: National ID number of the employee.')
        safe_write('- LoginID: Login ID for the employee.')
        safe_write('- OrganizationNode: Hierarchy node for organization structure.')
        safe_write('- OrganizationLevel: Level in the organization hierarchy.')
        safe_write('- JobTitle: Employee job title.')
        safe_write('- BirthDate: Date of birth.')
        safe_write('- MaritalStatus: Marital status.')
        safe_write('- Gender: Gender of the employee.')
        safe_write('- HireDate: Date of hire.')
        safe_write('- SalariedFlag: Whether the employee is salaried.')
        safe_write('- VacationHours: Number of vacation hours.')
        safe_write('- SickLeaveHours: Number of sick leave hours.')
        safe_write('- CurrentFlag: Whether the employee is currently employed.')
        safe_write('- rowguid: Unique identifier for the row.')
        safe_write('- ModifiedDate: Last modification date.')
except Exception as e:
    safe_write(f'ERROR: {e}')

safe_write('\n---\nSummary of HumanResources.Employee table:')
safe_write('The Employee table contains information about each employee in the organization. Key fields include:')
safe_write('- BusinessEntityID: Unique identifier for each employee.')
safe_write('- NationalIDNumber: Employee national identification number.')
safe_write('- LoginID: Employee login credentials.')
safe_write('- OrganizationNode/OrganizationLevel: Used to represent the employee’s position in the company hierarchy.')
safe_write('- JobTitle: The job title held by the employee.')
safe_write('- BirthDate, MaritalStatus, Gender: Demographic information.')
safe_write('- HireDate: Date the employee was hired.')
safe_write('- SalariedFlag: Indicates if the employee is salaried.')
safe_write('- VacationHours, SickLeaveHours: Tracks leave balances.')
safe_write('- CurrentFlag: Indicates if the employee is currently employed.')
safe_write('- rowguid: Unique row identifier for replication.')
safe_write('- ModifiedDate: Last time the record was updated.')
safe_write('This table is central for HR analytics, workforce planning, and organizational structure analysis.')

safe_write('\n---\nSummary of HumanResources.EmployeeDepartmentHistory table:')
safe_write('This table tracks the history of employee assignments to departments and shifts. Key fields:')
safe_write('- BusinessEntityID: Employee identifier.')
safe_write('- DepartmentID: Department identifier.')
safe_write('- ShiftID: Shift identifier.')
safe_write('- StartDate, EndDate: Assignment period.')
safe_write('- ModifiedDate: Last update.')
safe_write('Useful for analyzing employee movement, departmental changes, and shift assignments over time.')

safe_write('\n---\nSummary of HumanResources.EmployeePayHistory table:')
safe_write('This table records changes in employee pay rates. Key fields:')
safe_write('- BusinessEntityID: Employee identifier.')
safe_write('- RateChangeDate: Date of pay change.')
safe_write('- Rate: Pay rate.')
safe_write('- PayFrequency: Frequency of pay (e.g., monthly, biweekly).')
safe_write('- ModifiedDate: Last update.')
safe_write('Useful for compensation analysis, payroll auditing, and tracking pay progression.')

safe_write('\n---\nSummary of HumanResources.JobCandidate table:')
safe_write('This table stores information about job candidates. Key fields:')
safe_write('- JobCandidateID: Unique candidate identifier.')
safe_write('- BusinessEntityID: Associated employee (if hired).')
safe_write('- Resume: Candidate resume (XML format).')
safe_write('- ModifiedDate: Last update.')
safe_write('Useful for recruitment analytics, candidate tracking, and resume management.')
