import streamlit as st

st.title("¡Hola mundo desde Streamlit")

st.write("Esta es una aplicación de prueba que usa Streamlit.")

nombre = st.text_input("Introduce tu nombre")

if nombre:
  st.write("¡Hola, ", nombre, "!")