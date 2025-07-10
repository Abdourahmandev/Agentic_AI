# Agentic_AI
This repository is dedicated to learning how to build and deploy Agentic AI systems using LangChain and LangGraph.

## Set up the virtual environment

Prompt: Create a virtual environment with conda in the project directory and use the default python version
Command: conda create -p ./env python

### Activate the environment
Command: conda activate ./env

## Best Practices
- Do not commit the `env` folder to version control. Add `env/` to your `.gitignore` file.
- Use `requirements.txt` or `environment.yml` to specify dependencies for easy setup by collaborators.

## Next Steps
- Install required packages (e.g., LangChain, LangGraph) after activating the environment.
- See `Documentation.md` for more details and best practices.

# Agentic_AI Project

## Overview
This project explores the `AdventureWorks2022` SQL Server database, focusing on the `HumanResources` schema. The project includes automated scripts for schema exploration, context export, and documentation generation.

## Recent Updates
- Added `HumanRessourcesDocs.txt` in `SQLServer_Explorer` with detailed documentation of the HumanResources schema.
- Automated extraction of table names, columns, row counts, primary keys, and views.
- Confirmed that no foreign key relationships, stored procedures, functions, or triggers exist in the HumanResources schema.
- All results are exported to `context.txt` for reproducibility.

## Directory Structure
- `SQLServer_Explorer/`
  - `test_run_sql.py`: Script to run SQL queries and export results.
  - `context.txt`: Stores all extracted schema and data context.
  - `HumanRessourcesDocs.txt`: Human-readable documentation of the HumanResources schema.

## How to Reproduce
1. Ensure you have access to the `AdventureWorks2022` database on SQL Server.
2. Run `test_run_sql.py` to extract schema information and update `context.txt`.
3. Review `HumanRessourcesDocs.txt` for a summary of the schema.

## Notes
- All scripts are designed to be idempotent and append new findings without overwriting previous context.
- For further schema exploration, modify `test_run_sql.py` with new queries as needed.

