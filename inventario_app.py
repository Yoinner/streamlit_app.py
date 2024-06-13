import streamlit as st
import pandas as pd

# Enlace de Google Sheets
google_sheets_url = 'https://docs.google.com/spreadsheets/d/1Y0MQArGYk4k0UD1PQwIvcbgGdpSLZQGP/edit?usp=sharing&ouid=104131502310043866764&rtpof=true&sd=true'

# Convertir el enlace de Google Sheets a un enlace exportable en formato CSV
csv_export_url = google_sheets_url.replace('/edit?usp=sharing', '/gviz/tq?tqx=out:csv')

# Función para cargar datos desde Google Sheets sin usar cache
def load_data(url):
    return pd.read_csv(url)

data = load_data(csv_export_url)

# Función para buscar productos
def buscar_productos(query):
    return data[data['Nombre del Producto'].str.contains(query, case=False, na=False)]

# Título de la aplicación
st.title('Inventario del Almacén')

# Fondo de la aplicación
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        background-image: url('https://www.toptal.com/designers/subtlepatterns/patterns/memphis-mini-dark.png');
        color: black;
    }
    .stTextInput > div > div > input {
        background-color: #add8e6; /* Azul claro para resaltar el campo de búsqueda */
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Campo de búsqueda
query = st.text_input('Buscar producto...', '')

# Mostrar resultados de búsqueda
if query:
    resultados = buscar_productos(query)
    if not resultados.empty:
        for idx, row in resultados.iterrows():
            st.markdown(f"""
                **Nombre del Producto:** {row['Nombre del Producto']}  
                **Cantidad Disponible:** {row['Stock Actual']}  
                **Precio de Compra:** {row['Precio de Compra']}  
                **Precio de Venta:** {row['Precio de Venta']}  
                **Ubicación:** {row['Ubicación']}  
                ---
            """)
    else:
        st.write("No se encontraron productos.")
