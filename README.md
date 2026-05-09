# 👶 Nacimientos en Colombia – Dashboard DANE

Dashboard interactivo desarrollado con **Streamlit** y **Plotly** que visualiza los nacimientos registrados en Colombia entre 2014 y 2023, según datos del DANE (Estadísticas Vitales).

---

## 📁 Estructura del proyecto

```
nacimientos_colombia/
│
├── app.py                  ← Punto de entrada principal (aquí se corre la app)
│
├── data/
│   ├── __init__.py
│   └── datos_nacimientos.py   ← Datos del DANE y funciones de carga
│
├── utils/
│   ├── __init__.py
│   └── analisis.py            ← Funciones de análisis estadístico
│
├── components/
│   ├── __init__.py
│   ├── grafico.py             ← Gráfico de líneas con Plotly
│   ├── metricas.py            ← Tarjetas de métricas clave
│   └── tabla.py               ← Tabla de datos con descarga CSV
│
├── requirements.txt           ← Dependencias del proyecto
└── README.md                  ← Este archivo
```

---

## 🚀 Cómo correrlo localmente

### Paso 1 – Instalar Python
Asegúrate de tener **Python 3.9 o superior** instalado.
Puedes descargarlo en: https://www.python.org/downloads/

### Paso 2 – Abrir una terminal en la carpeta del proyecto
En Windows: clic derecho dentro de la carpeta → "Abrir en terminal" (o PowerShell).

### Paso 3 – Instalar las dependencias
```bash
pip install -r requirements.txt
```

### Paso 4 – Correr la aplicación
```bash
streamlit run app.py
```

Se abrirá automáticamente en tu navegador en `http://localhost:8501`

---

## 🌐 Cómo publicarlo en internet (Streamlit Community Cloud) – GRATIS

### Paso 1 – Crear cuenta en GitHub
Ve a https://github.com y crea una cuenta gratuita.

### Paso 2 – Crear un repositorio nuevo
1. Haz clic en el botón verde **"New"** o **"New repository"**.
2. Dale un nombre, por ejemplo: `nacimientos-colombia`.
3. Déjalo en **Público** y haz clic en **"Create repository"**.

### Paso 3 – Subir los archivos
En la página de tu repositorio vacío:
1. Haz clic en **"uploading an existing file"**.
2. Arrastra **todos los archivos y carpetas** del proyecto.
3. Haz clic en **"Commit changes"**.

> ⚠️ Asegúrate de subir también las carpetas `data/`, `utils/` y `components/` con sus archivos `__init__.py`.

### Paso 4 – Crear cuenta en Streamlit Community Cloud
Ve a https://share.streamlit.io e inicia sesión con tu cuenta de GitHub.

### Paso 5 – Desplegar la app
1. Haz clic en **"New app"**.
2. Selecciona tu repositorio `nacimientos-colombia`.
3. En **"Main file path"** escribe: `app.py`
4. Haz clic en **"Deploy!"**

En unos minutos tendrás una URL pública como:
`https://nacimientos-colombia-tunombre.streamlit.app`

---

## ✨ Funcionalidades

- 📈 Gráfico de líneas interactivo (zoom, hover, exportar imagen)
- 📉 Línea de tendencia lineal activable/desactivable
- 🎚️ Filtro de rango de años con slider
- 📊 Tarjetas con métricas clave (promedio, máximo, mínimo, total)
- 📋 Tabla de datos con variación anual absoluta y porcentual
- ⬇️ Descarga de los datos en formato CSV

---

## 📚 Fuente de datos

**DANE – Departamento Administrativo Nacional de Estadística**
Estadísticas Vitales – Nacimientos
https://www.dane.gov.co/index.php/estadisticas-por-tema/salud/nacimientos-y-defunciones
