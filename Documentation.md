# Agentic_AI Documentation

## Project Overview
Agentic_AI is a step-by-step guide for building and exploring agentic AI systems and SQL Server databases. This project demonstrates best practices for environment setup, dependency management, SQL schema exploration, and documentation.

## Step-by-Step Tutorial

### 1. Clone the Repository
Clone the project to your local machine:
```sh
git clone <your-repo-url>
```

### 2. Create and Activate a Conda Environment
Create a new environment inside the project directory for isolation and reproducibility:
```sh
conda create -p ./env python
conda activate ./env
```

### 3. Install Dependencies
Install required Python packages:
```sh
pip install -r requirements.txt
```

### 4. Set Up SQL Server Access
Ensure you have access to the AdventureWorks2022 database on your SQL Server instance. Update connection details in `run_sql.py` if needed.

### 5. Explore the Database
Run the provided scripts to extract schema and data context:
```sh
python SQLServer_Explorer/test_run_sql.py
```
- Results will be saved in `SQLServer_Explorer/context.txt`.
- Human-readable documentation is generated in `HumanRessourcesDocs.txt`.

### 6. Review Documentation
- See `README.md` for project overview and structure.
- See `HumanRessourcesDocs.txt` for schema documentation and analysis.

### 7. Version Control Best Practices
- Do not commit the `env` folder. Add `env/` to `.gitignore`.
- Use `requirements.txt` for dependencies.
- Commit and push changes regularly:
```sh
git add .
git commit -m "Update"
git push
```

## How to Use context.txt
- The `context.txt` file contains all extracted schema, data summaries, and analysis results.
- Use it as a reference for database structure, table meanings, and data patterns.
- You can append new findings or summaries to this file by running or modifying the provided scripts.
- For custom analysis, add your own summaries or query results to `context.txt` for reproducibility and sharing.

## How to Prompt GitHub Copilot for Best Results
- Be specific: Clearly state your goal, the table or schema you want to explore, and the type of analysis you need.
- Reference context: Mention relevant details from `context.txt` or documentation files to give Copilot the right context.
- Ask for summaries: Request concise explanations, data patterns, or code snippets for your use case.
- Example prompt: "Summarize the Employee table in HumanResources and suggest useful analytics."
- For code: Ask for step-by-step scripts, query examples, or automation tips.

---
For more details, see the `README.md` and `HumanRessourcesDocs.txt` files.

