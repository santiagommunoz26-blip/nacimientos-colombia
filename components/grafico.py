"""
grafico.py
----------
Componente encargado de construir el gráfico de líneas interactivo con Plotly.
"""

import plotly.graph_objects as go
import pandas as pd
import numpy as np


# Paleta de colores de la aplicación
COLOR_LINEA = "#E63946"
COLOR_TENDENCIA = "#457B9D"
COLOR_FONDO = "#FAFAFA"
COLOR_GRILLA = "#E0E0E0"


def crear_grafico_lineas(
    df: pd.DataFrame,
    mostrar_tendencia: bool = True,
    y_tendencia: np.ndarray = None,
) -> go.Figure:
    """
    Crea el gráfico de líneas de nacimientos con Plotly.

    Args:
        df (pd.DataFrame): DataFrame con columnas ['Año', 'Nacimientos'].
        mostrar_tendencia (bool): Si se debe mostrar la línea de tendencia.
        y_tendencia (np.ndarray): Valores de la línea de tendencia.

    Returns:
        go.Figure: Figura de Plotly lista para renderizar.
    """
    fig = go.Figure()

    # --- Área bajo la curva (efecto visual) ---
    fig.add_trace(go.Scatter(
        x=df["Año"],
        y=df["Nacimientos"],
        fill="tozeroy",
        fillcolor="rgba(230, 57, 70, 0.07)",
        line=dict(color="rgba(0,0,0,0)"),
        showlegend=False,
        hoverinfo="skip",
    ))

    # --- Línea principal de nacimientos ---
    fig.add_trace(go.Scatter(
        x=df["Año"],
        y=df["Nacimientos"],
        mode="lines+markers",
        name="Nacimientos",
        line=dict(color=COLOR_LINEA, width=3),
        marker=dict(
            size=9,
            color=COLOR_LINEA,
            line=dict(width=2, color="white"),
        ),
        hovertemplate=(
            "<b>Año %{x}</b><br>"
            "Nacimientos: <b>%{y:,.0f}</b><br>"
            "<extra></extra>"
        ),
    ))

    # --- Línea de tendencia (opcional) ---
    if mostrar_tendencia and y_tendencia is not None:
        fig.add_trace(go.Scatter(
            x=df["Año"],
            y=y_tendencia,
            mode="lines",
            name="Tendencia",
            line=dict(color=COLOR_TENDENCIA, width=2, dash="dash"),
            hovertemplate=(
                "<b>Tendencia %{x}</b><br>"
                "Proyectado: <b>%{y:,.0f}</b><br>"
                "<extra></extra>"
            ),
        ))

    # --- Configuración del layout ---
    fig.update_layout(
        title=dict(
            text="Nacimientos en Colombia (2014 – 2023)",
            font=dict(size=20, color="#1D3557"),
            x=0.02,
        ),
        xaxis=dict(
            title=dict(text="Año", font=dict(size=13, color="#1D3557")),
            tickmode="linear",
            dtick=1,
            tickfont=dict(size=12, color="#1D3557"),
            showgrid=True,
            gridcolor=COLOR_GRILLA,
            linecolor="#A8B4CC",
            zerolinecolor="#A8B4CC",
        ),
        yaxis=dict(
            title=dict(text="Número de nacimientos", font=dict(size=13, color="#1D3557")),
            tickformat=",",
            tickfont=dict(color="#1D3557"),
            showgrid=True,
            gridcolor=COLOR_GRILLA,
            linecolor="#A8B4CC",
            zerolinecolor="#A8B4CC",
        ),
        font=dict(color="#1D3557"),
        plot_bgcolor=COLOR_FONDO,
        paper_bgcolor="white",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color="#1D3557"),
        ),
        hovermode="x unified",
        margin=dict(l=60, r=30, t=80, b=60),
    )

    return fig
