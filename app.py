"""
app.py
------
Punto de entrada principal de la aplicación Streamlit.
Dashboard de nacimientos en Colombia Datos DANE (2014-2023).

Para ejecutar:
    streamlit run app.py
"""

import streamlit as st

from components import (
    crear_grafico_lineas,
    inicializar_aplicacion,
    mostrar_encabezado,
    mostrar_barra_lateral,
    mostrar_grafico,
    mostrar_metricas,
    mostrar_tabla,
)
from data import obtener_dataframe, obtener_rango, FUENTE, URL_FUENTE
from utils import calcular_estadisticas, calcular_variacion_anual, calcular_tendencia

inicializar_aplicacion()
mostrar_encabezado(FUENTE, URL_FUENTE)

rango, mostrar_tendencia, mostrar_tabla_datos = mostrar_barra_lateral(
    list(obtener_dataframe()["Año"])
)

# Procesamiento de datos

df_filtrado = obtener_rango(rango[0], rango[1])
stats = calcular_estadisticas(df_filtrado)
df_con_variacion = calcular_variacion_anual(df_filtrado)
_, y_tendencia, pendiente, _ = calcular_tendencia(df_filtrado)

# Visualización

st.divider()
col_principal, col_resumen = st.columns([2, 1])

with col_principal:
    fig = crear_grafico_lineas(
        df=df_filtrado,
        mostrar_tendencia=mostrar_tendencia,
        y_tendencia=y_tendencia if mostrar_tendencia else None,
    )
    mostrar_grafico(fig, pendiente, mostrar_tendencia)

with col_resumen:
    st.subheader("Resumen rápido")
    mostrar_metricas(stats)
    st.divider()
    st.markdown(
        """
        **Observaciones**
        - Ajusta el rango de años en la barra lateral.
        - Activa o desactiva la línea de tendencia.
        - Descarga los datos al final de la página.
        """
    )

if mostrar_tabla_datos:
    st.divider()
    st.markdown("### Datos detallados")
    mostrar_tabla(df_con_variacion)
