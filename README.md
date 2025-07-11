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
Agentic_AI is a step-by-step guide for building, exploring, and documenting agentic AI systems and SQL Server databases. The project demonstrates best practices for environment setup, dependency management, SQL schema exploration, and reproducible documentation.

## Quick Start

1. **Clone the Repository**
   ```sh
   git clone <your-repo-url>
   ```
2. **Create and Activate a Conda Environment**
   ```sh
   conda create -p ./env python
   conda activate ./env
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up SQL Server Access**
   - Ensure you have access to the AdventureWorks2022 database.
   - Update connection details in `run_sql.py` if needed.
5. **Explore the Database**
   ```sh
   python SQLServer_Explorer/test_run_sql.py
   ```
   - Results are saved in `SQLServer_Explorer/context.txt`.
   - Human-readable documentation is generated in `HumanRessourcesDocs.txt`.
6. **Review Documentation**
   - See `README.md` for project overview and structure.
   - See `HumanRessourcesDocs.txt` for schema documentation and analysis.
   - See `context.txt` for extracted schema, data summaries, and analysis results.

## How to Use context.txt
- Reference `context.txt` for database structure, table meanings, and data patterns.
- Append new findings or summaries by running or modifying the provided scripts.
- For custom analysis, add your own summaries or query results to `context.txt` for reproducibility and sharing.

## How to Prompt GitHub Copilot for Best Results
- Be specific: Clearly state your goal, the table or schema you want to explore, and the type of analysis you need.
- Reference context: Mention relevant details from `context.txt` or documentation files to give Copilot the right context.
- Ask for summaries: Request concise explanations, data patterns, or code snippets for your use case.
- Example prompt: "Summarize the Employee table in HumanResources and suggest useful analytics."
- For code: Ask for step-by-step scripts, query examples, or automation tips.

## Version Control Best Practices
- Do not commit the `env` folder. Add `env/` to `.gitignore`.
- Use `requirements.txt` for dependencies.
- Commit and push changes regularly:
   ```sh
   git add .
   git commit -m "Update"
   git push
   ```

## Additional Notes
- All scripts are designed to be reproducible and append new findings without overwriting previous context.
- You can modify or extend the scripts to explore other schemas or run custom queries.

---
For more details, see the `Documentation.md` and `HumanRessourcesDocs.txt` files.

