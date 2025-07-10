import pyodbc

# Default connection settings for SQL Server authentication
DEFAULT_SERVER = "localhost"
DEFAULT_DATABASE = "master"
DEFAULT_USERNAME = "sa"
DEFAULT_PASSWORD = "Rass1987"

def run_sql_query(query):
    """
    Connects to a SQL Server instance and executes the given SQL query.
    Returns the results as a list of tuples.
    """
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={DEFAULT_SERVER};"
        f"DATABASE={DEFAULT_DATABASE};"
        f"UID={DEFAULT_USERNAME};PWD={DEFAULT_PASSWORD};"
    )
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
