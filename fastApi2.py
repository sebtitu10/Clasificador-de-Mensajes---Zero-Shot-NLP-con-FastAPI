import uvicorn
from click import prompt
from fastapi import FastAPI, HTTPException
from pandas import notna
from pydantic import BaseModel
from transformers import pipeline
from sentence_transformers import CrossEncoder
from langchain.prompts import PromptTemplate

#creamos la instancia FastAPI
app = FastAPI(
    title= "API de categorizar mensajes"
)
models = "roberta-large-mnli"   #"facebook/bart-large-mnli  , este modelo tambien lo hace bien"
clasificador = pipeline("zero-shot-classification", model=models)


#Establecemos el esquema de la solicitud
class mensaje_request(BaseModel):
    texto: str # el dato que queremos resibir

#Lo que va a regresar el servicio
class mensaje_response(BaseModel):
    categoria: str


@app.post("/categoria",response_model=mensaje_response)
def evaluar_categoria(request: mensaje_request):
    if not request.texto.strip():
        raise HTTPException(status_code=400, detail="el mesaje no debe estar vacio")
    else:
        label_candidates = ["URGENTE", "MODERADO", "NORMAL"]

        #Integramos un prompt con el mensaje

        plantilla = PromptTemplate.from_template(
            "Clasifica el siguiente mensaje : {mensaje}")


        prompt = plantilla.format(mensaje=request.texto)
        print(prompt)
        resultado = clasificador(
            prompt,
            label_candidates,
        )
        etiqueta_mas_probable = resultado["labels"][0]

        print(resultado)

    return mensaje_response(categoria=etiqueta_mas_probable)




if __name__=="__main__":
    uvicorn.run("fastApi2:app",port=8081,reload=True)