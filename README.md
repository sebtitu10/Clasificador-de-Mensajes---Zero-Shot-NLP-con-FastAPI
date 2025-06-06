# 🧠 Clasificador de Mensajes - Zero-Shot NLP con FastAPI y Streamlit

Este proyecto es una aplicación web que **clasifica mensajes en categorías de prioridad**: `URGENTE`, `MODERADO` o `NORMAL`. Utiliza un modelo de clasificación **Zero-Shot** (`roberta-large-mnli`) de **Hugging Face Transformers**, expuesto a través de una **API en FastAPI** y una **interfaz web con Streamlit**.

---

## 🚀 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) — Para construir la API REST.
- [Transformers (Hugging Face)](https://huggingface.co/transformers/) — Para clasificación Zero-Shot.
- [Streamlit](https://streamlit.io/) — Para construir una interfaz web simple y rápida.
- [LangChain](https://www.langchain.com/) — Utilizado parcialmente para estructurar prompts.

---

## 📦 Estructura del Proyecto

```
📁 Clasificador/
│
├── fastApi.py          # Backend con FastAPI y modelo de clasificación
├── app.py              # Interfaz frontend con Streamlit
├── requirements.txt    # Lista de dependencias
├── README.md           # Este archivo
```

---

## ⚙️ Instalación y ejecución

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/clasificador-mensajes.git
cd clasificador-mensajes
```

### 2. Crea un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Inicia el servidor FastAPI

```bash
uvicorn fastApi:app --reload --port 8080
```

### 5. En otra terminal, ejecuta la app Streamlit

```bash
streamlit run app.py
```

---

## 📝 Ejemplos de mensajes de prueba

Puedes probar los siguientes mensajes para ver cómo se clasifican:

### URGENTE

- "Mi hijo no respira, necesito ayuda médica inmediata."
- "Tuve un accidente y estoy sangrando."

### MODERADO

- "Tengo fiebre desde ayer, ¿debo ir al médico?"
- "Siento mareos leves desde anoche."

### NORMAL

- "¿A qué hora abre la clínica?"
- "¿Dónde queda la dirección del consultorio?"

---

## ✅ Funcionalidades

- Clasificación Zero-Shot sin necesidad de entrenamiento previo.
- Clasificación en lenguaje natural en tres categorías.
- API REST lista para integrarse con otros sistemas.
- Interfaz web fácil de usar.

---

## 📌 Requisitos

- Python 3.8+
- Acceso a internet (para descargar el modelo `roberta-large-mnli` de Hugging Face la primera vez)

---

## 📚 Dependencias principales

```txt
fastapi
uvicorn
transformers
pydantic
streamlit
requests
langchain
```

---

## 💡 Posibles mejoras

- Reemplazar el modelo Hugging Face por un LLM (como GPT-4) usando LangChain completo.
- Añadir autenticación y control de acceso.
- Guardar el historial de clasificaciones.
- Añadir métricas de uso en la interfaz.

---

## 🧑‍💻 Autor

Desarrollado por Sebastián Adrián Tituaña Chiriboga\
Estudiante de Ingeniería en Sistemas – Universidad Central del Ecuador

---

## 🛡️ Licencia

MIT License
