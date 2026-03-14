import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import secrets
import os
import streamlit.components.v1 as components

# 1. CONFIGURACIÓN E INTERFAZ
st.set_page_config(page_title="TONUCOS Gestor", layout="wide")

# --- CSS DE DISEÑO COMPACTO E INDUSTRIAL ---
st.markdown("""
    <style>
    .stApp { background-color: #cfd8dc; }
    .block-container { 
        padding-top: 0rem !important; 
        padding-bottom: 0rem !important;
        max-width: 95% !important;
    }
    header { visibility: hidden; }
    
    .logo-container {
        display: flex;
        justify-content: center;
        margin-top: -20px;
    }

    /* Etiquetas Negras y Fuertes */
    label, .stMarkdown p, .stSelectbox label, .stTextInput label {
        color: #000000 !important;
        font-weight: 800 !important;
        font-size: 13px !important;
        margin-bottom: 0px !important;
    }
    
    /* Totales Gris Oscuro */
    .total-card { 
        background-color: #263238;
        color: #ffffff; 
        padding: 5px; 
        border-radius: 4px; 
        text-align: center;
        border: 1px solid #000;
    }
    .total-card b { font-size: 16px; color: #fff; }
    .total-card small { font-size: 9px; text-transform: uppercase; color: #cfd8dc; }

    /* REDUCCIÓN DE ESPACIOS (Lo que pediste) */
    .st-emotion-cache-18ni7ve { margin-top: 0px !important; } /* Espacio entre widgets */
    hr { margin: 5px 0px !important; border-top: 1px solid #263238 !important; } /* Línea separadora fina */

    /* Cabeceras de Mesa pegadas */
    .mesa-header { 
        background-color: #000; color: #fff; padding: 4px 10px; 
        font-weight: bold; margin-top: 2px !important; border-radius: 4px; 
        display: flex; justify-content: space-between; align-items: center; 
        font-size: 13px;
    }
    .pers-label { background-color: #fff; color: #000; padding: 0px 6px; border-radius: 8px; font-size: 10px; }

    /* Inputs más compactos */
    .stTextInput input, .stSelectbox div[data-baseweb="select"], .stNumberInput input {
        border: 2px solid #263238 !important;
        background-color: #ffffff !important;
        height: 32px !important;
    }

    .event-title { text-align: center; font-size: 20px; font-weight: 900; color: #263238; margin-bottom: 5px; }
    #MainMenu, footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- FUNCIONES NÚCLEO ---
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False
    if st.session_state.password_correct: return True
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns([1,1.5,1])
    with c2:
        st.markdown("<h3 style='text-align:center;'>SISTEMA TONUCOS</h3>", unsafe_allow_html=True)
        pw = st.text_input("Contraseña", type="password")
        if st.button("INGRESAR", use_container_width=True):
            if pw == st.secrets["access"]["password"]:
                st.session_state.password_correct = True
                st.rerun()
            else: st.error("Clave Incorrecta")
    return False

def conectar_google_sheet(nombre_archivo):
    try:
        scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        s = st.secrets["gcp_service_account"]
        creds = ServiceAccountCredentials.from_json_keyfile_dict(dict(s), scope)
        client = gspread.authorize(creds)
        return client.open(nombre_archivo).worksheet("Invitados")
    except: return None

def cargar_datos(archivo):
    sheet = conectar_google_sheet(archivo)
    if sheet:
        try:
            df = get_as_dataframe(sheet, evaluate_formulas=True, dtype=str).dropna(how='all')
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            for col in ["ID", "Mesa", "Nombre", "Categoria", "Observaciones", "Asistio"]:
                if col not in df.columns: df[col] = ""
            return df.fillna("")
        except: return pd.DataFrame(columns=["ID", "Mesa", "Nombre", "Categoria", "Observaciones", "Asistio"])
    return pd.DataFrame()

def guardar_datos(df_to_save, archivo):
    sheet = conectar_google_sheet(archivo)
    if sheet:
        sheet.clear()
        set_with_dataframe(sheet, df_to_save)

# --- LOGICA DE LA APP ---
if check_password():
    nombre_evento = st.query_params.get("id", "Boda Juan y Marta").replace("_", " ")

    if 'df' not in st.session_state or st.session_state.get('last_event') != nombre_evento:
        st.session_state.df = cargar_datos(nombre_evento)
        st.session_state.last_event = nombre_evento