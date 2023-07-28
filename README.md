# Jupyter for Devops Demo Project
A demo project to show how to use Jupyter as a runbook for DevOps

# Prerequisite

```
Python >= 3.8
Docker Compose
conda
```

Reference:

- [Miniconda Installation](https://docs.conda.io/en/latest/miniconda.html)

# Installation

```
VENV=jupyter-devops
conda create --name ${VENV} -y jupyterlab   
```

# Startup

```
conda run -n ${VENV} jupyter lab --port 8089
```

Then it will launch the Jupyter Lab in the browser with URL of http://localhost:8089 . Open __README__.ipynb and follow the instruction to explore how to manipulate a Drupal site with Jupyter.

