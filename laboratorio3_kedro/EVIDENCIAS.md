# Evidencias sugeridas

## 1. Verificacion del entorno

Captura:

- `python --version`
- `poetry --version`

## 2. Instalacion del proyecto

Captura:

- `poetry install`

Archivos que deben existir:

- `pyproject.toml`
- `poetry.lock`
- `requirements.txt`
- `.venv/`

## 3. Ejecucion del pipeline

Primera captura:

- `poetry run kedro run`
- con `image_path: "data/01_raw/imagen_oscura.png"`

Segunda captura:

- `poetry run kedro run`
- con `image_path: "data/01_raw/imagen_clara.png"`

Salida esperada:

- `data/08_reporting/resultado_analisis.json`

## 4. Pruebas unitarias

Captura:

- `poetry run pytest`

## 5. Reflexion

Adjunta el archivo:

- `REFLEXION_BREVE.md`
