import streamlit as st
import requests


#configuramos el URL base de la API de fastAPI

API_URL = "http://localhost:8081"

# Titulo de la aplicacion

st.title("Categorizador de mensajes")

#Descripcion
st.write("Esta aplicacion utiliza un modelo de Zero-Shot de Hugginface roberta-large-mnli")

#Entrada de texto
texto = st.text_area("Ingrese un mensaje para ser clasificado: ")

#boton para enviar el texto

if st.button("Clasificar mensaje"):
    if texto:
        #realiza la solicitud a la API de FastAPI
        response = requests.post(f"{API_URL}/categoria",json={"texto": texto})
        if response.status_code ==200:
            resultado = response.json()

            st.write(f" EL mensaje enviado se categorizo como: {resultado['categoria']}")
        else:
            st.write("Error al categorizar mensaje")
    else:
        st.write("Ingrese un comentario")




