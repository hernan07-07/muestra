import streamlit as st
import pandas as pd
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="GrupoTONUCOS Gestor", layout="wide")

# Fondo gris claro (truco de CSS para el diseño de tarjetas)
st.markdown("""
<style>
.stApp {
    background-color: #f0f2f6;
}
.total-card {
    background-color: white;
    border: 2px solid black;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
}
.total-card-highlight {
    background-color: black;
    color: white;
    border: 2px solid black;
    border-radius: 10px;
    padding: 10px;
    text-align: center;
}
.mesa-header {
    background-color: black;
    color: white;
    padding: 10px;
    border-radius: 5px;
    margin-top: 20px;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
}
</style>
""", unsafe_allow_html=True)

# Encabezado (Logo centrado)
logo_path = "path/to/your/logo.png" # Reemplazar con la ruta real o imagen local
try:
    logo = Image.open(logo_path)
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.image(logo, use_column_width=True)
except FileNotFoundError:
    # Marcador de posición si no se encuentra el logo
    c1, c2, c3 = st.columns([1, 2, 1])
    with c2:
        st.markdown("<div style='text-align: center; padding: 20px; border: 1px solid #ddd; border-radius: 5px; background-color: white; color: black;'>[Logotipo GrupoTONUCOS]</div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black; font-weight: bold;'>BODA JUAN Y MARTA</h1>", unsafe_allow_html=True)

# Panel de totales (resaltando el TOTAL)
total_cols = st.columns(5)
with total_cols[0]:
    st.markdown("<div class='total-card-highlight'><p style='font-size: 14px; color: white;'>TOTAL</p><p style='font-size: 24px; font-weight: bold; color: white;'>11</p></div>", unsafe_allow_html=True)
with total_cols[1]:
    st.markdown("<div class='total-card'><p style='font-size: 14px; color: black;'>MAYOR</p><p style='font-size: 24px; font-weight: bold; color: black;'>6</p></div>", unsafe_allow_html=True)
with total_cols[2]:
    st.markdown("<div class='total-card'><p style='font-size: 14px; color: black;'>ADOL.</p><p style='font-size: 24px; font-weight: bold; color: black;'>3</p></div>", unsafe_allow_html=True)
with total_cols[3]:
    st.markdown("<div class='total-card'><p style='font-size: 14px; color: black;'>MENOR</p><p style='font-size: 24px; font-weight: bold; color: black;'>2</p></div>", unsafe_allow_html=True)
with total_cols[4]:
    st.markdown("<div class='total-card'><p style='font-size: 14px; color: black;'>BEBÉ</p><p style='font-size: 24px; font-weight: bold; color: black;'>0</p></div>", unsafe_allow_html=True)

# Sección "AÑADIR REGISTRO" - MODIFICADA SEGÚN EL BOCETO
with st.expander("➕ AÑADIR REGISTRO", expanded=True):
    st.markdown("<h4 style='color: black;'>NUEVO INVITADO</h4>", unsafe_allow_html=True)
    
    # Definir anchos de columna para una sola línea
    # Los anchos son: Mesa, Nombre, Categoría, Observaciones, Botón
    col1, col2, col3, col4, col5 = st.columns([1, 4, 3, 2, 1])
    
    with col1:
        # Usamos widgets sin etiquetas para imitar el aspecto de una fila de datos
        # Placeholder actúa como etiqueta en línea
        mesa_in = st.number_input("", value=0, min_value=0, step=1, placeholder="Mesa")
    with col2:
        nombre_in = st.text_input("", placeholder="APELLIDO y nombre")
    with col3:
        categoria_in = st.selectbox("", options=["MAYOR", "ADOLESCENTE", "MENOR", "BEBÉ"], index=0)
    with col4:
        # El campo de observaciones es más pequeño
        obs_in = st.text_input("", placeholder="OBSERVACIONES")
    with col5:
        # Botón con icono de guardar/añadir al final de la línea
        add_btn = st.button("💾", key="add_guest_btn")

st.markdown("<hr>", unsafe_allow_html=True)

# Sección inferior (Buscador y botón de guardar)
c1, c2, c3 = st.columns([4, 1, 1])
with c1:
    st.text_input("🔍 BUSCAR INVITADO", placeholder="Nombre...")
with c3:
    st.button("💾 GUARDAR CAMBIOS")

# Muestra de registros ya cargados para demostrar consistencia
# Mesa 1
st.markdown("<div class='mesa-header'><span>🪑 MESA 1</span><span>1 PERS.</span></div>", unsafe_allow_html=True)
c1, c2, c3, c4, c5 = st.columns([1, 4, 3, 2, 1])
with c1: st.text_input("", value="1", disabled=True)
with c2: st.text_input("", value="MARTINA", disabled=True)
with c3: st.text_input("", value="ADOLESCENTE", disabled=True)
with c4: st.text_input("", value="", disabled=True)
with c5: st.button("🗑️", key="del_1")

# Mesa 2
st.markdown("<div class='mesa-header'><span>🪑 MESA 2</span><span>7 PERS.</span></div>", unsafe_allow_html=True)
c1, c2, c3, c4, c5 = st.columns([1, 4, 3, 2, 1])
with c1: st.text_input("", value="2", disabled=True)
with c2: st.text_input("", value="MARINTINE NARO", disabled=True)
with c3: st.text_input("", value="MENOR", disabled=True)
with c4: st.text_input("", value="Cumple", disabled=True)
with c5: st.button("🗑️", key="del_2")

# Nota: Reemplazar logo_path con la ruta real o imagen local para cargar el logotipo.