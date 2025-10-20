
# Desafio 115

## 1. Requisitos

- [install uv](https://docs.astral.sh/uv/getting-started/installation/)

## 2. Adicionar/Remover pacotes

- `uv add <package>` (add dependencies to the project)
- `uv remove <package>` (remove dependencies from the project)
- `uv add --dev pytest` (add a development dependency)

## 3. Como iniciar

1. `uv sync`
2. `uv run src\main.py`

## 4. Docker comandos

- `docker build <imagename> .` (create image from Dockerfile)
- `docker run -it <imagename>` (run image)
- `docker compose build` (create images defined by docker-compose)
- `docker compose run -it <servicename>` (execute a service of docker-compose in interactive mode)

## 5. UV venv activate

- `.venv\Scripts\activate` - activate uv venv
- `.venv\Scripts\deactivate` - deactivate uv venv
