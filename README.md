# 🤖 PALACE AI

### Enterprise Document Assistant

PALACE AI es un agente inteligente basado en **Retrieval-Augmented Generation (RAG)** capaz de responder preguntas en lenguaje natural utilizando información contenida en documentos PDF y CSV.

El sistema combina búsqueda semántica mediante embeddings, una base vectorial (ChromaDB) y modelos de lenguaje de OpenAI para proporcionar respuestas precisas y contextualizadas.

---

# Características

✅ Carga de documentos PDF

✅ Carga de documentos CSV

✅ Indexación automática

✅ Embeddings con OpenAI

✅ Almacenamiento vectorial con ChromaDB

✅ Respuestas mediante RAG

✅ Detección de documentos duplicados

✅ Gestión de múltiples documentos

✅ Interfaz web con Streamlit

---

# Arquitectura

```

Usuario

↓

Streamlit

↓

Application Layer

↓

Knowledge Retriever

↓

OpenAI Embeddings

↓

ChromaDB

↓

OpenAI GPT

↓

Respuesta

```

---

# Flujo del sistema

1. El usuario carga un documento.
2. El documento es procesado.
3. El contenido se divide en fragmentos (chunks).
4. Se generan embeddings.
5. Los embeddings se almacenan en ChromaDB.
6. El usuario realiza una pregunta.
7. Se recuperan los fragmentos más relevantes.
8. OpenAI genera una respuesta utilizando únicamente el contexto encontrado.

---

# Arquitectura del proyecto

```

PALACE-AI/

application/
core/
infrastructure/

data/
chromadb/

docs/

streamlit_app.py

requirements.txt

README.md

```

---

# Tecnologías utilizadas

| Tecnología | Uso |
|------------|-------------------------------|
| Python 3.14 | Lenguaje principal |
| Streamlit | Interfaz web |
| OpenAI API | Modelo de lenguaje |
| OpenAI Embeddings | Embeddings |
| ChromaDB | Base vectorial |
| SQLite | Persistencia |
| PyPDF | Lectura de PDF |
| Pandas | Lectura de CSV |

---

# Instalación

Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/PALACE-AI.git
```

Entrar al proyecto

```bash
cd PALACE-AI
```

Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno

Windows

```bash
venv\Scripts\activate
```

Linux

```bash
source venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Variables de entorno

Crear un archivo `.env`

```
OPENAI_API_KEY=tu_api_key
```

---

# Ejecutar

```bash
streamlit run streamlit_app.py
```

---

# Ejemplos de preguntas

### PDF

- ¿Cuál es la política de vacaciones?
- ¿Qué dice el manual sobre licencias?
- ¿Cuáles son las responsabilidades del cargo?

### CSV

- ¿Cuál es el precio del producto A?
- ¿Qué productos pertenecen a la categoría Tecnología?
- ¿Cuántos registros existen?

---

# Ejemplos de respuestas

Pregunta

```
¿Cuál es la política de vacaciones?
```

Respuesta

```
Según el manual, los empleados tienen derecho a 15 días hábiles de vacaciones por cada año trabajado.
```

---

# Futuras mejoras

- Soporte para DOCX
- Soporte para Excel
- Historial de conversaciones
- API REST
- Integración con ERP
- Autenticación de usuarios
- Dashboard administrativo

---

# Capturas

## Página principal

*(Agregar captura aquí)*

---

## Chat

*(Agregar captura aquí)*

---

## Carga de documentos

*(Agregar captura aquí)*

---

# Autor

Desarrollado como parte del **Challenge Alura ONE - Agente Inteligente con IA**.
