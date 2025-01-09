import streamlit as st

# Page config
st.set_page_config(
    page_title="Neurona Artificial",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 3rem;
    }
    .title {
        text-align: center;
        color: #1E88E5;
        margin-bottom: 2rem;
    }
    .block-container {
        padding-left: 8rem;
        padding-right: 8rem;
        max-width: 80rem;
        margin: auto;
    }
    .stTabs {
        margin-top: 2rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header layout with title and image
col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown("<h1 class='title'>Neurona Artificial</h1>", unsafe_allow_html=True)
    st.image("neurona.jpg", width=400, use_container_width=False)

st.markdown("---")

# Tabs
pestanas = st.tabs(["🔢 Una entrada", "2️⃣ Dos entradas", "3️⃣ Tres entradas y sesgo"])

# Primera pestaña
with pestanas[0]:
    st.header("Neurona Simple")
    st.markdown("""
    Esta es una neurona artificial básica con:
    - Una entrada (x₀)
    - Un peso (w₀)
    - Una salida (y)
    
    La fórmula es: **y = w₀x₀**
    """)
    
    w0 = st.slider("🎚️ Ajustar w₀:", min_value=0.0, max_value=5.0, value=0.5, step=0.1)
    x0 = st.number_input("🔵 Introduce x₀:", value=0.0)
    
    if st.button("🧮 Calcular", key="calc1"):
        y = w0 * x0
        st.success(f"🎯 La salida de la neurona es: {y:.2f}")

# Segunda pestaña
with pestanas[1]:
    st.header("Neurona con Dos Entradas")
    st.markdown("""
    Neurona artificial con dos entradas:
    - Dos entradas (x₀, x₁)
    - Dos pesos (w₀, w₁)
    
    La fórmula es: **y = w₀x₀ + w₁x₁**
    """)

    col1, col2 = st.columns(2)
    with col1:
        w0 = st.slider("🎚️ Ajustar w₀:", min_value=0.0, max_value=5.0, value=1.5, step=0.1, key="w0_2")
    with col2:
        w1 = st.slider("🎚️ Ajustar w₁:", min_value=0.0, max_value=5.0, value=2.5, step=0.1, key="w1_2")
    
    col1, col2 = st.columns(2)
    with col1:
        x0 = st.number_input("🔵 Introduce x₀:", value=0.0, key="x0_2")
    with col2:
        x1 = st.number_input("🔵 Introduce x₁:", value=0.0, key="x1_2")
    
    if st.button("🧮 Calcular", key="calc2"):
        y = x0 * w0 + x1 * w1
        st.success(f"🎯 La salida de la neurona es: {y:.2f}")

# Tercera pestaña
with pestanas[2]:
    st.header("Neurona con Tres Entradas y Sesgo")
    st.markdown("""
    Neurona artificial compleja:
    - Tres entradas (x₀, x₁, x₂)
    - Tres pesos (w₀, w₁, w₂)
    - Un sesgo (bias)
    
    La fórmula es: **y = w₀x₀ + w₁x₁ + w₂x₂ + bias**
    """)

    col1, col2, col3 = st.columns(3)
    with col1:
        w0 = st.slider("🎚️ Ajustar w₀:", min_value=0.0, max_value=5.0, value=1.0, step=0.1, key="w0_3")
    with col2:
        w1 = st.slider("🎚️ Ajustar w₁:", min_value=0.0, max_value=5.0, value=2.0, step=0.1, key="w1_3")
    with col3:
        w2 = st.slider("🎚️ Ajustar w₂:", min_value=0.0, max_value=5.0, value=3.0, step=0.1, key="w2_3")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        x0 = st.number_input("🔵 Introduce x₀:", value=0.0, key="x0_3")
    with col2:
        x1 = st.number_input("🔵 Introduce x₁:", value=0.0, key="x1_3")
    with col3:
        x2 = st.number_input("🔵 Introduce x₂:", value=0.0, key="x2_3")
    
    bias = st.number_input("🔢 Introduce el sesgo:", value=0.0, step=0.1)
    
    if st.button("🧮 Calcular", key="calc3"):
        y = x0 * w0 + x1 * w1 + x2 * w2 + bias
        st.success(f"🎯 La salida de la neurona es: {y:.2f}")

st.markdown("---")
st.markdown("Hecho con ❤️ por Germán García Estévez")