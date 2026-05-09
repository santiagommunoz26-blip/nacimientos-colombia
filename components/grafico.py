"""
grafico.py
----------
Componente encargado de construir el gráfico de líneas interactivo con Plotly.
"""

import plotly.graph_objects as go
import pandas as pd
import numpy as np


# Paleta de colores de la aplicación
COLOR_LINEA = "#FB7185"
COLOR_TENDENCIA = "#34D399"
COLOR_FONDO = "#0F172A"
COLOR_GRILLA = "#334155"


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
        fillcolor="rgba(251, 113, 133, 0.16)",
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
        line=dict(color=COLOR_LINEA, width=4),
        marker=dict(
            size=10,
            color=COLOR_LINEA,
            line=dict(width=2, color="#0F172A"),
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
            font=dict(size=20, color="#F8FAFC"),
            x=0.02,
        ),
        xaxis=dict(
            title=dict(text="Año", font=dict(size=13, color="#E2E8F0")),
            tickmode="linear",
            dtick=1,
            tickfont=dict(size=12, color="#E2E8F0"),
            showgrid=True,
            gridcolor=COLOR_GRILLA,
            linecolor="#475569",
            zerolinecolor="#475569",
        ),
        yaxis=dict(
            title=dict(text="Número de nacimientos", font=dict(size=13, color="#E2E8F0")),
            tickformat=",",
            tickfont=dict(color="#E2E8F0"),
            showgrid=True,
            gridcolor=COLOR_GRILLA,
            linecolor="#475569",
            zerolinecolor="#475569",
        ),
        font=dict(color="#E2E8F0"),
        plot_bgcolor=COLOR_FONDO,
        paper_bgcolor=COLOR_FONDO,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color="#E2E8F0"),
        ),
        hovermode="x unified",
        margin=dict(l=60, r=30, t=80, b=60),
    )

    return fig
