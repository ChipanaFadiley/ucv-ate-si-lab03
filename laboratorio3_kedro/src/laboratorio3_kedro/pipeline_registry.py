"""Registro de pipelines del proyecto."""

from kedro.pipeline import Pipeline

from laboratorio3_kedro.pipelines.histogram.pipeline import create_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Registra el pipeline de histogramas como pipeline por defecto."""
    histogram_pipeline = create_pipeline()

    return {
        "__default__": histogram_pipeline,
        "histogram": histogram_pipeline,
    }
