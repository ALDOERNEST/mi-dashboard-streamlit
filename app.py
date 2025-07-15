
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Título de la app
st.title("👋 ¡Hola mundo con Streamlit!")

# Texto de bienvenida
st.write("Este es un ejemplo básico de dashboard con Streamlit.")

# Crear datos ficticios
data = pd.DataFrame({
    'Día': ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes'],
    'Ventas': [100, 120, 90, 140, 160]
})

# Mostrar tabla
st.subheader("📊 Datos de ejemplo")
st.dataframe(data)

# Mostrar gráfico de líneas
st.subheader("📈 Gráfico de Ventas")
fig, ax = plt.subplots()
ax.plot(data['Día'], data['Ventas'], marker='o')
ax.set_ylabel("Ventas")
ax.set_title("Ventas por Día")
st.pyplot(fig)
