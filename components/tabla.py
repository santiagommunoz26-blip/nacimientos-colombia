"""
tabla.py
--------
Componente que renderiza la tabla de datos con variaciones anuales.
"""

import streamlit as st
import pandas as pd


def mostrar_tabla(df: pd.DataFrame) -> None:
    """
    Muestra la tabla de datos con variación anual y opción de descarga.

    Args:
        df (pd.DataFrame): DataFrame con columnas de variación ya calculadas.
    """
    st.subheader("📋 Datos por año")

    # Formatear el dataframe para visualización
    df_display = df.copy()
    df_display["Nacimientos"] = df_display["Nacimientos"].apply(lambda x: f"{x:,}")
    df_display["Variación"] = df_display["Variación"].apply(
        lambda x: f"+{x:,}" if x > 0 else f"{x:,}"
    )
    df_display["Variación %"] = df_display["Variación %"].apply(
        lambda x: f"+{x:.2f}%" if x > 0 else f"{x:.2f}%"
    )
    df_display = df_display.rename(columns={"Variación %": "Variación %"})

    st.dataframe(
        df_display.set_index("Año"),
        use_container_width=True,
    )

    # Botón de descarga CSV
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="⬇️ Descargar datos en CSV",
        data=csv,
        file_name="nacimientos_colombia_dane.csv",
        mime="text/csv",
    )
