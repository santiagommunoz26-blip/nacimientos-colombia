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
        page_icon=None,
        layout="wide",
        initial_sidebar_state="expanded",
    )

    st.markdown(
        """
        <style>
            .block-container {
                padding: 2rem 2rem 3rem;
                background: radial-gradient(circle at top left, #1E293B 0%, #111827 100%);
                color: #E2E8F0;
            }
            .stApp {
                background: #0F172A;
                color: #E2E8F0;
            }
            h1, h2, h3, p, span, label, a {
                color: #E2E8F0 !important;
            }
            .stMetric {
                background-color: #1E293B !important;
                border-radius: 1rem !important;
                padding: 1rem !important;
                box-shadow: 0 18px 40px rgba(15, 23, 42, 0.45) !important;
                color: #F8FAFC !important;
            }
            .stDownloadButton button,
            .stButton button {
                background-color: #F97316 !important;
                color: #ffffff !important;
                border: none !important;
            }
            .stDownloadButton button:hover,
            .stButton button:hover {
                background-color: #EA580C !important;
            }
            div[data-testid="stDataFrame"] table {
                color: #E2E8F0 !important;
                border-color: #334155 !important;
                background-color: #0F172A !important;
            }
            div[data-testid="stDataFrame"] th {
                color: #F8FAFC !important;
                background-color: #1E293B !important;
            }
            div[data-testid="stDataFrame"] td {
                background-color: #111827 !important;
            }
            .stSidebar {
                background-color: #111827 !important;
                color: #E2E8F0 !important;
            }
            .stSidebar h1, .stSidebar h2, .stSidebar h3, .stSidebar p, .stSidebar span, .stSidebar label, .stSidebar a {
                color: #E2E8F0 !important;
            }
            .stCheckbox label, .stSlider label {
                color: #E2E8F0 !important;
            }
            .stCheckbox input[type="checkbox"] {
                accent-color: #38BDF8 !important;
            }
            .stSlider > div[data-testid="stSlider"] input {
                accent-color: #38BDF8 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def mostrar_encabezado(fuente: str, url_fuente: str) -> None:
    """Muestra el encabezado principal con título y fuente."""
    st.markdown(
        f"""
        <div style="padding: 1.5rem 1.8rem; border-radius: 1.4rem; background: linear-gradient(135deg, #7C3AED 0%, #0EA5E9 100%); box-shadow: 0 24px 60px rgba(15, 23, 42, 0.35);">
            <h1 style="margin: 0 0 0.4rem; font-size: 2.6rem; color: white;">Nacimientos en Colombia</h1>
            <p style="margin: 0; font-size: 1rem; line-height: 1.6; color: rgba(255,255,255,0.92);">
                Análisis de nacimientos registrados en Colombia durante los últimos 10 años.
                Fuente oficial: <strong><a href="{url_fuente}" target="_blank" style="color: #E0F2FE; text-decoration: underline;">{fuente}</a></strong>
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.divider()


def mostrar_barra_lateral(anios_disponibles: List[int]) -> Tuple[Tuple[int, int], bool, bool]:
    """Muestra los controles en la barra lateral y devuelve las opciones seleccionadas."""
    with st.sidebar:
        st.header("Controles")
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
        st.caption("Datos: DANE – Estadísticas Vitales")
        st.caption("Proyecto académico universitario")

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
