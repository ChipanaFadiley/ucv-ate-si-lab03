"""Herramientas de analisis de imagenes."""

import cv2
import numpy as np


class ImageAnalyzer:
    """Clase que encapsula la logica de analisis de imagenes."""

    def calcular_histograma(self, imagen: np.ndarray) -> np.ndarray:
        """Calcula el histograma de una imagen en escala de grises."""
        if imagen is None:
            raise ValueError("La imagen no puede ser nula.")

        histograma = cv2.calcHist([imagen], [0], None, [256], [0, 256])
        return histograma.flatten()

    def clasificar_imagen(self, histograma: np.ndarray) -> str:
        """Clasifica la imagen como oscura o clara segun el histograma."""
        intensidad_baja = float(histograma[:128].sum())
        intensidad_alta = float(histograma[128:].sum())

        if intensidad_baja > intensidad_alta:
            return "oscura"
        return "clara"
