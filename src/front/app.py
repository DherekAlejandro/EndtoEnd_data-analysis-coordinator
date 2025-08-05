import streamlit as st
import requests
from PIL import Image
import io
import os


# Nueva paleta de colores moderna y profesional
COLOR_PRIMARIO = '#1A237E'  # Indigo oscuro
COLOR_SECUNDARIO = '#3949AB'  # Indigo medio
COLOR_ACENTO = '#00B8D4'     # Cyan acento
COLOR_FONDO = '#F5F7FA'      # Fondo gris muy claro
COLOR_TEXTO = '#212121'      # Gris oscuro para texto

# Logo de la empresa (puedes reemplazar la URL por la ruta local si tienes el archivo)
LOGO_URL = 'https://soandes.com.co/wp-content/themes/soandes/images/logo-soandes.svg'

st.set_page_config(page_title='IPS Salud Ocupacional de los Andes', page_icon=LOGO_URL, layout='centered')

# Fondo plano y estilos mejorados
st.markdown(f"""
    <style>
        .stApp {{
            background: linear-gradient(135deg, {COLOR_FONDO} 80%, {COLOR_ACENTO} 100%) !important;
        }}
        .block-container {{
            background-color: {COLOR_FONDO} !important;
            border-radius: 16px;
            padding: 2rem 2rem 2rem 2rem;
            box-shadow: 0 2px 16px 0 rgba(26,35,126,0.07);
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {COLOR_PRIMARIO} !important;
        }}
        .st-bb {{
            color: {COLOR_TEXTO} !important;
        }}
        .stButton>button {{
            background-color: {COLOR_SECUNDARIO};
            color: white;
            border-radius: 8px;
            border: none;
            padding: 0.5rem 1.5rem;
            font-weight: 600;
            transition: background 0.2s;
        }}
        .stButton>button:hover {{
            background-color: {COLOR_ACENTO};
            color: {COLOR_PRIMARIO};
        }}
        .stFileUploader {{
            background-color: #fff !important;
            border-radius: 8px;
        }}
    </style>
""", unsafe_allow_html=True)


st.image(LOGO_URL, width=220)
st.markdown(f"<h1 style='text-align:center; color:{COLOR_PRIMARIO}; margin-bottom:0;'>IPS Salud Ocupacional de los Andes</h1>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align:center; color:{COLOR_SECUNDARIO}; margin-top:0;'>Procesamiento de Imágenes Médicas</h3>", unsafe_allow_html=True)

st.markdown(f'''<hr style="border:1px solid {COLOR_PRIMARIO}; margin-bottom:2rem;">''', unsafe_allow_html=True)


# Configura la URL del backend según entorno
BACKEND_URL = os.getenv('BACKEND_URL', 'https://fastapi-backend-h2xu.onrender.com/')

uploaded_file = st.file_uploader('Sube una imagen médica', type=['jpg', 'jpeg', 'png', 'bmp', 'tiff'])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Imagen cargada', use_column_width=True)
    if st.button('Procesar Imagen', key='procesar'):
        with st.spinner('Procesando imagen...'):
            files = {'file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
            try:
                response = requests.post(BACKEND_URL, files=files)
                if response.status_code == 200:
                    st.success('Procesamiento exitoso')
                    st.json(response.json())
                else:
                    st.error(f'Error en el procesamiento: {response.status_code}')
            except Exception as e:
                st.error(f'No se pudo conectar con la API: {e}')
