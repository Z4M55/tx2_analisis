# -*- coding: utf-8 -*-
import streamlit as st
from textblob import TextBlob
from googletrans import Translator

# =============================
# Configuración de página
# =============================
st.set_page_config(
    page_title="TextBlob · Tech Mode",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="expanded"
)

# =============================
# Estilos personalizados (tech dark + neon)
# =============================
st.markdown("""
<style>
:root {
  --bg: #0a0f1a;
  --panel: #10192b;
  --text: #e6f7ff;
  --accent: #00e5ff;
  --accent2: #00ffa3;
}
html, body, .stApp {
  background: radial-gradient(800px 500px at 10% 0%, #122240 0%, var(--bg) 60%);
  color: var(--text) !important;
}
[data-testid="stSidebar"] {
  background: linear-gradient(180deg, #0f182b 0%, #091021 100%) !important;
  border-right: 1px solid rgba(0,229,255,0.15);
}
h1, h2, h3, h4, h5, h6 {
  color: var(--accent);
  font-family: "JetBrains Mono", monospace;
  letter-spacing: .5px;
}
p, label, span, .stMarkdown {
  color: var(--text) !important;
  font-family: "Inter", system-ui, -apple-system, "Segoe UI", Roboto, Arial, sans-serif;
}
.stButton>button {
  width: 100%;
  background: linear-gradient(90deg, var(--accent) 0%, var(--accent2) 100%) !important;
  color: #00121a !important;
  border: none !important;
  border-radius: 12px !important;
  font-weight: 700 !important;
  box-shadow: 0 0 14px rgba(0,229,255,.35);
  transition: transform .1s ease-in-out, box-shadow .2s ease-in-out;
}
.stButton>button:hover {
  transform: translateY(-1px);
  box-shadow: 0 0 20px rgba(0,229,255,.55);
}
.metric {
  background: var(--panel);
  border-radius: 12px;
  padding: 10px;
  text-align: center;
  box-shadow: 0 0 20px rgba(0,229,255,.15);
  margin-top: 10px;
}
.result {
  background: var(--panel);
  border-left: 3px solid var(--accent);
  border-radius: 8px;
  padding: 15px;
  margin-top: 10px;
  color: var(--text);
  box-shadow: 0 0 15px rgba(0,229,255,.15);
}
</style>
""", unsafe_allow_html=True)

# =============================
# Título principal
# =============================
st.title("💬 Análisis de Sentimientos con TextBlob — Tech Mode")
st.caption("Detección automática de sentimientos, traducida y procesada con IA 💡")

translator = Translator()

# =============================
# Panel lateral
# =============================
with st.sidebar:
    st.subheader("⚙️ Polaridad y Subjetividad")
    st.markdown("""
    **Polaridad:** indica si el sentimiento es positivo, negativo o neutral  
    *(rango de -1 a 1)*  

    **Subjetividad:** mide cuánto del texto es opinión o hecho  
    *(0 es objetivo, 1 es subjetivo)*
    """)

# =============================
# Sección 1 — Análisis
# =============================
with st.expander("⚡ Analizar Polaridad y Subjetividad"):
    text1 = st.text_area("✍️ Escribe una frase en español para analizar:")
    if text1:
        with st.spinner("Analizando sentimiento... ⚙️"):
            translation = translator.translate(text1, src="es", dest="en")
            trans_text = translation.text
            blob = TextBlob(trans_text)
            polarity = round(blob.sentiment.polarity, 2)
            subjectivity = round(blob.sentiment.subjectivity, 2)

            st.markdown(f"""
            <div class='metric'>
            <h4>🔹 Polaridad:</h4> <h3>{polarity}</h3>
            <h4>🔸 Subjetividad:</h4> <h3>{subjectivity}</h3>
            </div>
            """, unsafe_allow_html=True)

            if polarity >= 0.5:
                st.markdown("<div class='result'>😄 **Sentimiento positivo** — reflejas entusiasmo y optimismo.</div>", unsafe_allow_html=True)
            elif polarity <= -0.5:
                st.markdown("<div class='result'>😔 **Sentimiento negativo** — percibo tristeza o descontento.</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='result'>😐 **Sentimiento neutral** — es un mensaje equilibrado y objetivo.</div>", unsafe_allow_html=True)

# =============================
# Sección 2 — Corrección
# =============================
with st.expander("🧠 Corrección en inglés"):
    text2 = st.text_area("✍️ Escribe una frase en inglés para corregir:", key='corr')
    if text2:
        with st.spinner("Corrigiendo con TextBlob... 💡"):
            blob2 = TextBlob(text2)
            st.success("✅ Texto corregido:")
            st.markdown(f"<div class='result'>{blob2.correct()}</div>", unsafe_allow_html=True)

# =============================
# Pie de página
# =============================
st.divider()
st.caption("⚙️ Desarrollado con TextBlob, GoogleTranslate y Streamlit — modo tech 💻")
