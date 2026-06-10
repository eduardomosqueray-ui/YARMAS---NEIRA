# Debe direccionar VS Code a la carpeta con los archivos:
# 1.- Archivo
# 2.- Abrir carpeta. Debe dar click en la carpeta que contiene los archivos de interés
#3.- A la izquierda, en el explorador deberá poder visualizar todos los archivos
#------------------------------------------------------------------------------------------------

# CÓDIGO STREAMLIT
# Ir a:   Ver/Terminal
# Crea un ambiente virtual (puedes usar otro nombre en lugar de 'venv'): coloca este código
#   python -m venv venv

#---------------------------------------------------------------------------------------
# Luego de crear el ambiente virtual, lo activas
#   .\venv\Scripts\activate   # En Windows
#---------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------
# Cuando vuelva a iniciar sesión, debe volver a activar el ambiente virtual, ya no lo debe crear.
# En este caso debes abrir la carpeta con los archivos del caso.
#---------------------------------------------------------------------------------------------


# Instala la versión específica de scikit-learn
#   pip install scikit-learn==1.2.2
# Instala otras dependencias, incluyendo Streamlit
#  pip install streamlit pandas joblib
#-------------------------------------------------------------------------------------------------
# Desde la segunda vez: hacer:
# Si da error, debes ir a PowerShell de Window y:
#      Get-ExecutionPolicy                           Si es Restricted; ejecuta
#      Set-ExecutionPolicy RemoteSigned              Colocar Sí
# En consola de VSC:  .\venv\Scripts\activate



import streamlit as st
import pandas as pd
from joblib import load
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler
#import pyautogui

# Cargar el modelo de regresión
regressor = load('modelo_informalidad.joblib')

# Cargar el encoder
#with open('encoderpipeline.pickle', 'rb') as f:
#    encoder = pickle.load(f)

# Inicializar variables
ANIO_ESTUDIO_ACUM = C208 = ingtrabw = C317A = 0.0
C207 = 1

# Streamlit app
st.title("Predicción de Informalidad Laboral")
st.markdown("##### Si colocas un valor negativo, aparecerá un error y no podrás completar otros campos. La predicción será incorrecta.")

# Sidebar para la entrada del usuario
st.sidebar.header("Campos a Evaluar")

# Entrada del usuario para RD_Spend
ANIO_ESTUDIO_ACUM = st.sidebar.number_input(
    "Años de estudio acumulados",
    min_value=0,
    max_value=20,
    value=11
)

C208 = st.sidebar.number_input(
    "Edad",
    min_value=14,
    max_value=94,
    value=30
)

C207 = st.sidebar.selectbox(
    "Sexo",
    options=[1, 2],
    format_func=lambda x: "Hombre" if x == 1 else "Mujer"
)

ingtrabw = st.sidebar.number_input(
    "Ingreso laboral principal",
    min_value=0,
    max_value=93751,
    value=1000
)

C317A = st.sidebar.number_input(
    "N° trabajadores en la empresa",
    min_value=1,
    max_value=9998,
    value=10
)

# Función para resetear las entradas
def reset_inputs():
    global rd_spend, administration, marketing_spend, selected_state
    rd_spend = administration = marketing_spend = 0.0
    selected_state = "New York"

# Botón para predecir
if st.sidebar.button("Predecir"):

    obs = pd.DataFrame({
        'ANIO_ESTUDIO_ACUM': [ANIO_ESTUDIO_ACUM],
        'C208': [C208],
        'C207': [C207],
        'ingtrabw': [ingtrabw],
        'C317A': [C317A]
    })

    st.write("Datos ingresados:")
    st.dataframe(obs)

    prediccion = regressor.predict(obs)

    resultado = prediccion[0]

    if resultado == 1:
        st.error("⚠️ El modelo predice que el trabajador pertenece al sector INFORMAL")
    else:
        st.success("✅ El modelo predice que el trabajador pertenece al sector FORMAL")

        #----------------------Pipeline-------------------------
        # Predecir usando el modelo
        target = regressor.predict(obs)

        # Mostrar la predicción con un tamaño de fuente grande usando markdown
        #st.markdown(f'<p style="font-size: 40px; color: green;">La predicción del Profit será: ${target[0]:,.2f}</p>', unsafe_allow_html=True)


# Colocar el botón "Resetear" debajo del botón "Predecir"
if st.sidebar.button("Resetear"):
    # Resetear inputs
    reset_inputs()

#   R&D Spend	Administration	Marketing Spend  Ciudad  
#	  142107.34  	91391.77	366168.42         Florida    ---->

# Cambiar los valores.
# Para asignar valores: ver los rangos de las cuantitativas ( MÍNIMO --MÁXIMO)
# eso determinan  cómo predice el modelo. 

#  streamlit run streamlitpipelines.py       en la consola
#  pip freeze > requirements.txt