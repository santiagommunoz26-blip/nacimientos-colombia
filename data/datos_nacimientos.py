"""
datos_nacimientos.py
--------------------
Datos de nacimientos en Colombia obtenidos del DANE (Estadísticas Vitales).
Fuente: https://www.dane.gov.co/index.php/estadisticas-por-tema/salud/nacimientos-y-defunciones
"""

import pandas as pd

# Datos anuales de nacimientos registrados en Colombia
NACIMIENTOS_POR_ANIO = {
    2014: 661270,
    2015: 658957,
    2016: 643234,
    2017: 625989,
    2018: 609098,
    2019: 595578,
    2020: 553242,
    2021: 564081,
    2022: 559913,
    2023: 541200,
}

# Información de la fuente
FUENTE = "DANE – Estadísticas Vitales"
URL_FUENTE = "https://www.dane.gov.co/index.php/estadisticas-por-tema/salud/nacimientos-y-defunciones"


def obtener_dataframe() -> pd.DataFrame:
    """
    Convierte el diccionario de datos en un DataFrame de pandas.

    Returns:
        pd.DataFrame: Columnas ['Año', 'Nacimientos']
    """
    df = pd.DataFrame(
        list(NACIMIENTOS_POR_ANIO.items()),
        columns=["Año", "Nacimientos"]
    )
    df = df.sort_values("Año").reset_index(drop=True)
    return df


def obtener_rango(anio_inicio: int, anio_fin: int) -> pd.DataFrame:
    """
    Filtra el DataFrame por rango de años.

    Args:
        anio_inicio (int): Año de inicio del rango.
        anio_fin (int): Año de fin del rango.

    Returns:
        pd.DataFrame: DataFrame filtrado.
    """
    df = obtener_dataframe()
    return df[(df["Año"] >= anio_inicio) & (df["Año"] <= anio_fin)].reset_index(drop=True)
