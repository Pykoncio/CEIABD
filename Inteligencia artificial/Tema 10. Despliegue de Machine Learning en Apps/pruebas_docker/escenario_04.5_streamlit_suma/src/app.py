import streamlit as st

st.title("Ejemplo de suma de dos dígitos.")

digit_1 = st.number_input("Introduce un primer dígito:", value=0)
digit_2 = st.number_input("Introduce un segundo dígito:", value=0)

result = digit_1 + digit_2

st.write(f"La suma de {digit_1} y {digit_2} es: {result}")