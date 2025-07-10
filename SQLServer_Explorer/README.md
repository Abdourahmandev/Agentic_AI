# SQLServer_Explorer

This module is dedicated to exploring and interacting with SQL Server databases. Use the included Jupyter notebook and Python script to connect, query, and analyze data from your SQL Server instances.

## Contents
- `SQL_Explorer.ipynb`: Jupyter notebook for SQL Server exploration and analysis.
- `run_sql.py`: Python script with a reusable function to connect to a SQL Server instance and execute SQL queries.
- `requirements.txt`: List of required dependencies for SQL Server exploration.
- `requirements2.txt`: Additional dependencies for advanced SQL Server connectivity and analysis.
- `prompt.md`: Organized prompts for setting up and using the SQLServer_Explorer tools.

## Getting Started
1. Install dependencies from `requirements.txt` and `requirements2.txt`:
   ```sh
   pip install -r requirements.txt
   pip install -r requirements2.txt
   ```
2. Open the notebook in VS Code or Jupyter.
3. Use `run_sql.py` to connect and run queries from your scripts or import the function into your notebook.

## Requirements
- Python 3.x
- Jupyter Notebook
- `pyodbc`, `pandas`, `sqlalchemy`, `ipython-sql` (see requirements files)

## Example Usage
See the notebook for code examples and workflow, or use the following in your Python scripts:

```python
from run_sql import run_sql_query
results = run_sql_query("SELECT name FROM sys.databases")
print(results)
```
