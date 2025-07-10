import pyodbc

def run_sql_query(query, server='localhost', database='master', username=None, password=None):
    """
    Connects to a SQL Server instance and executes the given SQL query.
    Returns the results as a list of tuples.
    """
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
    )
    if username and password:
        conn_str += f"UID={username};PWD={password};"
    else:
        conn_str += "Trusted_Connection=yes;"
    
    with pyodbc.connect(conn_str) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        try:
            results = cursor.fetchall()
            return results
        except pyodbc.ProgrammingError:
            # No results to fetch (e.g., for INSERT/UPDATE)
            return None

# Example usage:
# results = run_sql_query("SELECT name FROM sys.databases")
# print(results)
