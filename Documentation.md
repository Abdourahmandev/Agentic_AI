# Agentic_AI Documentation

## Project Overview
Agentic_AI is a repository dedicated to learning how to build and deploy Agentic AI systems using LangChain and LangGraph. The project demonstrates best practices for environment setup, dependency management, and workflow for agentic AI development.

## Environment Setup

### Creating a Conda Environment in the Project Directory
To ensure reproducibility and isolation, create a conda environment inside the project directory:

```sh
conda create -p ./env python
```

- This will create a new environment in the `env` folder within your project directory.

### Activating the Environment

```sh
conda activate ./env
```

- Use this command to activate the environment for development and running scripts.

## Best Practices
- **Do not commit the `env` folder to version control.** Add `env/` to your `.gitignore` file.
- Use `requirements.txt` or `environment.yml` to specify dependencies for easy setup by collaborators.

## Next Steps
- Install required packages (e.g., LangChain, LangGraph) after activating the environment.
- Follow the README for further instructions on building and deploying agentic AI workflows.

---
For more details, see the `README.md` file.

