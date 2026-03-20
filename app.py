# --- CSS: FIX DEFINITIVO PARA LETRAS BLANCAS EN CELULAR ---
st.markdown("""
    <style>
    .stApp { background-color: #cfd8dc; }
    .block-container { padding-top: 0rem !important; max-width: 95% !important; }
    header { visibility: hidden; }
    
    /* CURSOR VISIBLE */
    input { caret-color: #ff0000 !important; } /* Cursor Rojo para que se vea bien */

    /* RESALTAR CAMPO ACTIVO */
    .stTextInput input:focus, .stNumberInput input:focus {
        border: 2px solid #1e88e5 !important;
        box-shadow: 0 0 8px rgba(30, 136, 229, 0.6) !important;
    }

    /* 🚨 FIX LETRAS BLANCAS EN DESPLEGABLE (CELULAR) 🚨 */
    
    /* 1. Forzar fondo del contenedor */
    div[data-baseweb="popover"], div[role="listbox"], ul {
        background-color: #ffffff !important;
    }

    /* 2. Forzar color de letra NEGRO a CUALQUIER texto dentro de una opción */
    [data-baseweb="option"], [role="option"], [data-baseweb="option"] * {
        color: #000000 !important;
        font-weight: 700 !important;
        background-color: #ffffff !important;
    }

    /* 3. Cuando pasas el dedo (hover/active), invertimos colores para que se note la selección */
    [data-baseweb="option"]:hover, [data-baseweb="option"]:active, 
    [role="option"]:hover, [role="option"]:active {
        background-color: #263238 !important;
    }
    
    /* 4. El texto dentro de la opción resaltada debe ser blanco */
    [data-baseweb="option"]:hover *, [role="option"]:hover * {
        color: #ffffff !important;
    }

    /* 5. Texto de la categoría ya seleccionada en el cuadro principal */
    div[data-baseweb="select"] * {
        color: #000000 !important;
    }

    /* Diseño de tarjetas y headers */
    .total-card { 
        background-color: #263238; color: #ffffff; padding: 5px; 
        border-radius: 4px; text-align: center; border: 1px solid #000;
    }
    .mesa-header { 
        background-color: #000; color: #fff; padding: 4px 10px; 
        font-weight: bold; margin-top: 2px !important; border-radius: 4px; 
        display: flex; justify-content: space-between; align-items: center; 
    }
    </style>
""", unsafe_allow_html=True)