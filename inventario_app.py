import streamlit as st
import pandas as pd

# Enlace de Google Sheets
google_sheets_url = 'https://docs.google.com/spreadsheets/d/1Y0MQArGYk4k0UD1PQwIvcbgGdpSLZQGP/edit?usp=sharing'

# Convertir el enlace de Google Sheets a un enlace exportable en formato CSV
csv_export_url = google_sheets_url.replace('/edit?usp=sharing', '/gviz/tq?tqx=out:csv')

# Función para cargar datos desde Google Sheets
@st.cache
def load_data(url):
    return pd.read_csv(url)

data = load_data(csv_export_url)

# Función para buscar productos
def buscar_productos(query):
    return data[data['Nombre del Producto'].str.contains(query, case=False, na=False)]

# Título de la aplicación
st.title('Inventario del Almacén')

# Campo de búsqueda
query = st.text_input('Buscar producto...', '')

# Mostrar resultados de búsqueda
if query:
    resultados = buscar_productos(query)
    if not resultados.empty:
        for idx, row in resultados.iterrows():
            st.write(f"**Nombre del Producto:** {row['Nombre del Producto']}")
            st.write(f"**Stock Actual:** {row['Stock Actual']}")
            st.write(f"**Precio de Compra:** {row['Precio de Compra']}")
            st.write(f"**Precio de Venta:** {row['Precio de Venta']}")
            st.write("---")
    else:
        st.write("No se encontraron productos.")
