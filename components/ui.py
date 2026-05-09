"""
ui.py
-----
Funciones de presentaci\u00f3n de la interfaz para la aplicación Streamlit.
"""

from typing import List, Tuple

import streamlit as st


def inicializar_aplicacion() -> None:
    """Configura la página y aplica estilos de interfaz."""
    st.set_page_config(
        page_title="Nacimientos en Colombia – DANE",
        page_icon="👶",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>
            .block-container {
                padding: 2rem 2rem 3rem;
                background-color: #F4F8FC;
            }
            .stApp {
                background: linear-gradient(180deg, #ffffff 0%, #eef6fc 100%);
            }
            h1, h2, h3, p, span, label, a {
                color: #1D3557 !important;
            }
            .stMetric {
                background-color: #ffffff !important;
                border-radius: 1rem !important;
                padding: 1rem !important;
                box-shadow: 0 16px 30px rgba(0, 0, 0, 0.06) !important;
            }
            .stDownloadButton button,
            .stButton button {
                background-color: #457B9D !important;
                color: #ffffff !important;
                border: none !important;
            }
            .stDownloadButton button:hover,
            .stButton button:hover {
                background-color: #1D3557 !important;
            }
            div[data-testid="stDataFrame"] table {
                color: #1D3557 !important;
                border-color: #e5e7eb !important;
            }
            div[data-testid="stDataFrame"] th {
                color: #1D3557 !important;
                background-color: #F8FAFC !important;
            }
            div[data-testid="stDataFrame"] td {
                background-color: #ffffff !important;
            }
            footer {
                visibility: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def mostrar_encabezado(fuente: str, url_fuente: str) -> None:
    """Muestra el encabezado principal con título y fuente."""
    st.title("👶 Nacimientos en Colombia")
    st.markdown(
        f"Análisis de nacimientos registrados en Colombia durante los últimos 10 años. "
        f"Fuente oficial: **[{fuente}]({url_fuente})**"
    )
    st.divider()


def mostrar_barra_lateral(anios_disponibles: List[int]) -> Tuple[Tuple[int, int], bool, bool]:
    """Muestra los controles en la barra lateral y devuelve las opciones seleccionadas."""
    with st.sidebar:
        st.header("⚙️ Controles")
        st.markdown("Personaliza la visualización según tus preferencias.")

        rango = st.slider(
            "Rango de años",
            min_value=min(anios_disponibles),
            max_value=max(anios_disponibles),
            value=(min(anios_disponibles), max(anios_disponibles)),
            step=1,
        )

        mostrar_tendencia = st.toggle("Mostrar línea de tendencia", value=True)
        mostrar_tabla_datos = st.toggle("Mostrar tabla de datos", value=True)

        st.divider()
        st.caption("📌 Datos: DANE – Estadísticas Vitales")
        st.caption("🎓 Proyecto académico universitario")

    return rango, mostrar_tendencia, mostrar_tabla_datos


def mostrar_grafico(fig, pendiente: float, mostrar_tendencia: bool) -> None:
    """Presenta el gráfico principal y el texto de acompañamiento."""
    st.plotly_chart(fig, use_container_width=True)

    if mostrar_tendencia:
        direccion = "disminuyendo" if pendiente < 0 else "aumentando"
        st.info(
            f"📊 **Tendencia:** El número de nacimientos ha venido **{direccion}** "
            f"aproximadamente **{abs(pendiente):,.0f} nacimientos por año** en el período seleccionado."
        )

    st.divider()
