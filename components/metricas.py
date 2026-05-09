"""
metricas.py
-----------
Componente que renderiza las tarjetas de métricas clave en Streamlit.
"""

import streamlit as st


def mostrar_metricas(stats: dict) -> None:
    """
    Muestra las tarjetas de métricas en la parte superior del dashboard.

    Args:
        stats (dict): Diccionario con estadísticas calculadas.
    """
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📊 Promedio anual",
            value=f"{stats['promedio']:,}",
        )

    with col2:
        st.metric(
            label="📈 Año con más nacimientos",
            value=f"{stats['anio_maximo']}",
            delta=f"{stats['maximo']:,}",
        )

    with col3:
        st.metric(
            label="📉 Año con menos nacimientos",
            value=f"{stats['anio_minimo']}",
            delta=f"-{stats['maximo'] - stats['minimo']:,}",
            delta_color="inverse",
        )

    with col4:
        st.metric(
            label="👶 Total del período",
            value=f"{stats['total_periodo']:,}",
        )
