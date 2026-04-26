# Laboratorio 3 Kedro

En este laboratorio se desarrolló un proyecto en Python para el análisis de imágenes en escala de grises. Para ello se utilizó Kedro como framework para organizar el flujo de trabajo, OpenCV para la lectura de imágenes y el cálculo del histograma, y Pytest para la ejecución de pruebas unitarias.

El proyecto implementa la clase ImageAnalyzer, la cual permite calcular el histograma de una imagen y clasificarla como clara u oscura en función de la distribución de intensidades de sus píxeles.

## Estructura del proyecto

- `conf/base`: contiene los parametros y la configuracion del catalogo.
- `data/01_raw`: contiene las imagenes de entrada.
- `data/08_reporting`: guarda el resultado final del analisis en formato JSON.
- `src/laboratorio3_kedro`: contiene el codigo fuente del proyecto.
- `tests`: contiene las pruebas unitarias.

## Ejecucion y pruebas unitarias

```powershell
poetry install
poetry run kedro run
poetry run pytest -v
```

## Resultado

Al ejecutar el pipeline, se genera el archivo resultado_analisis.json, el cual contiene la ruta de la imagen analizada, la clasificación obtenida (clara u oscura) y los valores del histograma calculado.