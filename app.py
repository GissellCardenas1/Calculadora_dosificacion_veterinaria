# -*- coding: utf-8 -*-
import streamlit as st

# 1. Configuración de la página
st.set_page_config(
    page_title="Guardian Soul - Calculadora de Dosis",
    page_icon="🐾",
    layout="centered"
)

# 2. Inyección de CSS Avanzado para calcar tu diseño original en la Web
st.markdown("""
    <style>
    /* Fondo general de la web */
    .stApp {
        background-color: #dce7e1 !important;
        background-image: radial-gradient(#cadbd0 20%, transparent 20%),
                          radial-gradient(#cadbd0 20%, transparent 20%) !important;
        background-size: 40px 40px !important;
        background-position: 0 0, 20px 20px !important;
    }
    
    /* Ocultar elementos nativos de Streamlit */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Encabezado de Marca */
    .brand-title {
        text-align: center;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-size: 18px;
        font-weight: bold;
        color: #b5945b;
        letter-spacing: 2px;
        margin-top: 10px;
        margin-bottom: 2px;
    }
    .brand-sub {
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
        font-size: 10px;
        color: #7a8a81;
        letter-spacing: 3px;
        font-weight: bold;
        margin-bottom: 25px;
    }
    
    /* Tarjeta Contenedora Principal (Tu panel gris) */
    .main-card {
        background-color: rgba(218, 226, 221, 0.95);
        border-radius: 24px;
        padding: 30px 25px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        max-width: 420px;
        margin: 0 auto;
        font-family: 'Segoe UI', sans-serif;
    }
    
    .card-title {
        text-align: center;
        font-size: 15px;
        font-weight: bold;
        color: #4a544e;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 25px;
    }
    
    /* Forzar estilos sobre los inputs (Cajas blancas redondeadas y texto centrado) */
    .stTextInput div div input {
        background-color: #ffffff !important;
        color: #333333 !important;
        border-radius: 25px !important;
        border: none !important;
        padding: 10px 15px !important;
        text-align: center !important;
        font-size: 14px !important;
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.05) !important;
    }
    
    /* Estilo para las etiquetas de texto de los inputs */
    label {
        color: #4a544e !important;
        font-weight: 500 !important;
        font-size: 13px !important;
        margin-bottom: 4px !important;
        display: block;
        text-align: center;
    }
    
    /* Botón Personalizado (Tu botón verde) */
    div.stButton > button {
        background-color: #8fa495 !important;
        color: #2e3b32 !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-size: 14px !important;
        font-weight: bold !important;
        width: 180px !important;
        display: block !important;
        margin: 25px auto 0 auto !important;
        box-shadow: 0 3px 6px rgba(0,0,0,0.08) !important;
        transition: background 0.2s;
    }
    div.stButton > button:hover {
        background-color: #7e9384 !important;
        color: #2e3b32 !important;
    }
    
    /* Caja Blanca de Resultados */
    .custom-result-box {
        background-color: #ffffff;
        border-radius: 20px;
        padding: 25px 20px;
        text-align: center;
        font-size: 14px;
        color: #333333;
        line-height: 1.6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        max-width: 320px;
        margin: 20px auto;
        border: 1px solid #e6ece8;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Estructura de la Interfaz
st.markdown('<div class="brand-title">🐾 GUARDIAN SOUL</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-sub">ELITE BLOOD</div>', unsafe_allow_html=True)

# Contenedor de la tarjeta
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.markdown('<div class="card-title">Calculadora de Dosis</div>', unsafe_allow_html=True)

# Inicializar estados de la app para el control de pantallas
if 'calculado' not in st.session_state:
    st.session_state.calculado = False

if not st.session_state.calculado:
    # Campos corregidos para evitar confusiones de los usuarios
    medicamento = st.text_input("Medicamento", placeholder="Nombre del fármaco").title()
    mascota = st.text_input("Nombre de la mascota", placeholder="Ej. Max, Freyja...").title()
    
    peso_raw = st.text_input("Peso (kg)", placeholder="Peso del paciente en kg")
    dosis_raw = st.text_input("Dosis (mg/kg)", placeholder="Dosis indicada (mg/kg)")
    concentracion_raw = st.text_input("Concentración (mg/ml)", placeholder="Concentración del fármaco (mg/ml)")

    if st.button("Calcular Dosis"):
        if medicamento == "" or mascota == "" or peso_raw == "" or dosis_raw == "" or concentracion_raw == "":
            st.error("Por favor, complete todos los campos antes de calcular.")
        else:
            try:
                # Soporte para ingreso de comas regionales
                peso = float(peso_raw.replace(',', '.'))
                dosis_mg_kg = float(dosis_raw.replace(',', '.'))
                concentracion_medicamento = float(concentracion_raw.replace(',', '.'))
                
                if peso <= 0 or dosis_mg_kg <= 0 or concentracion_medicamento <= 0:
                    st.error("Los valores numéricos deben ser mayores a cero.")
                else:
                    st.session_state.resultado_ml = round((peso * dosis_mg_kg) / concentracion_medicamento, 2)
                    st.session_state.msg_resultado = f"{mascota} debe recibir {st.session_state.resultado_ml} ml de {medicamento}."
                    st.session_state.calculado = True
                    st.rerun()
            except ValueError:
                st.error("Asegúrate de ingresar solo números válidos en los campos de Peso, Dosis y Concentración.")
else:
    # Pantalla de resultados (Caja blanca idéntica a tu mockup)
    st.markdown(f"""
        <div class="custom-result-box">
            Texto resultado:<br>
            **{st.session_state.msg_resultado}**
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("Realizar nuevo cálculo"):
        st.session_state.calculado = False
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True) # Cierre de la tarjeta principal

# 4. Sección de Descargo Legal abajo
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("Descargo legal"):
    st.caption("""
    **ADVERTENCIA LEGAL Y EXENCIÓN DE RESPONSABILIDAD**
    
    Este software es una herramienta de apoyo al cálculo aritmético con fines estrictamente educativos. La determinación de la dosis definitiva es responsabilidad exclusiva del Médico Veterinario tratante, quien debe validar los resultados con base en el estado fisiológico, patológico y la anamnesis del paciente.
    
    Los cálculos obtenidos no consideran variables críticas como la función renal, hepática o edad del animal. Por lo tanto, el autor se deslinda de toda responsabilidad por efectos adversos o errores derivados del uso de esta información sin supervisión profesional calificada.
    
    Uso sujeto a la normativa de ética profesional (Ley 576 de 2000).
    """)