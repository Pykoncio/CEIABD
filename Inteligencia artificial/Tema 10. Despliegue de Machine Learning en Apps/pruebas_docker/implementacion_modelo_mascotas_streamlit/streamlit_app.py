import streamlit as st
import joblib
import pandas as pd
import json

st.title("ClassifyPets")
st.write("This is a simple web app to classify pets based on their features.")
st.image("img/mascotas.jpg", use_container_width=True)

# Carga el modelo entrenado y las asignaciones para las etiquetas de color de ojos y largo de pelo
model = joblib.load("model/pets_model.joblib")

with open("model/category_mapping.json", "r") as f:
    category_mapping = json.load(f)

# Extrae los valores categóricos 
eye_color_values = category_mapping["eye_color"]
fur_length_values = category_mapping["fur_length"]

# Pediremos los datos de la mascota
weight = st.number_input("Weight (kg)", min_value=0.0, max_value=100.0, value=0.0)
height = st.number_input("Height (cm)", min_value=0.0, max_value=100.0, value=0.0)
eye_color = st.selectbox("Eye color", eye_color_values)
fur_length = st.selectbox("Fur Length", fur_length_values)

# Si lo hicieramos en español tendriamos que crear un diccionario para mapear los colores de ojos y largo de pelo
# eye_color_map = {"Blue": "Azul", "Green": "Verde", "Brown": "Marrón", "Grey": "Gris"}
# fur_length = {"Short": "Corto", "Medium": "Medio", "Long": "Largo"}
# selected_eye_color = eye_color_map[eye_color]
# selected_fur_length = fur_length_map[fur_length]

# Generamos las columnas binarias para eye_color y fur_length
eye_color_binary = [color == eye_color for color in eye_color_values]
fur_length_binary = [length == fur_length for length in fur_length_values]

# Crea un DataFrame con los datos de la mascota
input_data = [weight, height] + eye_color_binary + fur_length_binary
columns = ["weight_kg", "height_cm"] + [f"eye_color_{color}" for color in eye_color_values]  \
                                     + [f"fur_length_{length}" for length in fur_length_values]
input_df = pd.DataFrame([input_data], columns=columns)

# Realiza la predicción
# Si queremos que el resultado sea en español, podemos hacer un mapeo de la predicción igual que antes
# prediction_map = {"cat": "Gato", "dog": "Perro", "rabbit": "Conejo", "Hamster": "Hámster"}
if (st.button("Classify the pet")):
    prediction = model.predict(input_df)[0] # Solo queremos el primer elemento del vector de la predccion
    st.success(f"Your pet is a {prediction}", icon="✅")


