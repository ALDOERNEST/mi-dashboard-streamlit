import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título de la app
st.title("📈 Dashboard Interactivo de Ventas")

# Datos ficticios de ventas
data = {
    "Día": ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
    "Ventas": [120, 150, 90, 200, 170]
}
df = pd.DataFrame(data)

# Selector de días a mostrar
dias_seleccionados = st.multiselect(
    "Selecciona los días que quieres visualizar:",
    options=df["Día"].tolist(),
    default=df["Día"].tolist()
)

# Filtro de datos según selección
df_filtrado = df[df["Día"].isin(dias_seleccionados)]

# Control deslizante para multiplicar ventas
factor = st.slider("Multiplica las ventas por un factor:", 0.5, 3.0, 1.0, 0.1)
df_filtrado["Ventas Ajustadas"] = df_filtrado["Ventas"] * factor

# Mostrar tabla
st.subheader("📊 Datos de Ventas Ajustadas")
st.dataframe(df_filtrado)

# Gráfico
st.subheader("📉 Gráfico de Ventas Ajustadas")
fig, ax = plt.subplots()
ax.plot(df_filtrado["Día"], df_filtrado["Ventas Ajustadas"], marker='o', linestyle='-', color='blue')
ax.set_ylabel("Ventas")
ax.set_title("Ventas por Día (Ajustadas)")
st.pyplot(fig)
