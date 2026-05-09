"""
analisis.py
-----------
Funciones de análisis estadístico sobre los datos de nacimientos.
"""

import pandas as pd
import numpy as np


def calcular_estadisticas(df: pd.DataFrame) -> dict:
    """
    Calcula estadísticas descriptivas básicas.

    Args:
        df (pd.DataFrame): DataFrame con columnas ['Año', 'Nacimientos'].

    Returns:
        dict: Diccionario con estadísticas clave.
    """
    nacimientos = df["Nacimientos"]

    anio_max = int(df.loc[nacimientos.idxmax(), "Año"])
    anio_min = int(df.loc[nacimientos.idxmin(), "Año"])

    return {
        "promedio": int(nacimientos.mean()),
        "maximo": int(nacimientos.max()),
        "minimo": int(nacimientos.min()),
        "anio_maximo": anio_max,
        "anio_minimo": anio_min,
        "total_periodo": int(nacimientos.sum()),
    }


def calcular_variacion_anual(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega columnas de variación absoluta y porcentual año a año.

    Args:
        df (pd.DataFrame): DataFrame con columnas ['Año', 'Nacimientos'].

    Returns:
        pd.DataFrame: DataFrame con columnas adicionales de variación.
    """
    df = df.copy()
    df["Variación"] = df["Nacimientos"].diff()
    df["Variación %"] = df["Nacimientos"].pct_change() * 100
    df["Variación"] = df["Variación"].fillna(0).astype(int)
    df["Variación %"] = df["Variación %"].fillna(0).round(2)
    return df


def calcular_tendencia(df: pd.DataFrame) -> tuple:
    """
    Calcula la línea de tendencia lineal (regresión simple).

    Args:
        df (pd.DataFrame): DataFrame con columnas ['Año', 'Nacimientos'].

    Returns:
        tuple: (años para tendencia, valores ajustados, pendiente, intercepto)
    """
    x = df["Año"].values
    y = df["Nacimientos"].values
    coeficientes = np.polyfit(x, y, 1)
    pendiente, intercepto = coeficientes
    y_tendencia = np.polyval(coeficientes, x)
    return x, y_tendencia, round(pendiente, 2), round(intercepto, 2)
