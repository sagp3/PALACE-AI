# 🤖 PALACE AI

## Enterprise Document Assistant

PALACE AI es un asistente inteligente basado en **Retrieval-Augmented Generation (RAG)** que permite consultar documentos empresariales en lenguaje natural utilizando inteligencia artificial.

El sistema procesa documentos PDF y CSV, genera embeddings mediante OpenAI, almacena la información en una base vectorial (ChromaDB) y responde preguntas utilizando únicamente el contexto encontrado en los documentos.

---

## 🚀 Demo en línea

**Aplicación desplegada en Streamlit**

👉 https://palace.streamlit.app/

---

## 💻 Repositorio

GitHub

👉 https://github.com/sagp3/PALACE-AI.git

---

# Características

- 📄 Carga de documentos PDF
- 📊 Carga de archivos CSV
- 🧠 Búsqueda semántica mediante OpenAI Embeddings
- 🤖 Respuestas generadas con OpenAI GPT
- 📚 Base de datos vectorial con ChromaDB
- 🗄 Persistencia mediante SQLite
- 🚫 Detección automática de documentos duplicados
- 🗑 Eliminación de documentos
- 💬 Interfaz web desarrollada con Streamlit
- 🏗 Arquitectura limpia (Clean Architecture)

---

# Arquitectura

```
                Usuario
                   │
                   ▼
              Streamlit UI
                   │
                   ▼
          Application Layer
                   │
                   ▼
        Knowledge Retriever
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
 OpenAI Embeddings      ChromaDB
        │
        ▼
     Prompt Builder
        │
        ▼
    OpenAI GPT Model
        │
        ▼
       Respuesta
```

---

# Flujo del sistema

1. El usuario carga uno o varios documentos.
2. El sistema extrae el contenido.
3. El documento se divide en pequeños fragmentos (**chunks**).
4. Se genera un **embedding** para cada fragmento.
5. Los embeddings se almacenan en **ChromaDB**.
6. El usuario realiza una pregunta.
7. Se genera el embedding de la pregunta.
8. Se buscan los fragmentos más similares.
9. OpenAI recibe únicamente esos fragmentos como contexto.
10. Se genera una respuesta basada exclusivamente en la información encontrada.

---

# Tecnologías utilizadas

| Tecnología | Descripción |
|------------|-------------|
| Python 3.12 | Lenguaje principal |
| Streamlit | Interfaz web |
| OpenAI GPT | Modelo de lenguaje |
| OpenAI Embeddings | Búsqueda semántica |
| ChromaDB | Base de datos vectorial |
| SQLite | Persistencia |
| Pandas | Lectura de CSV |
| PyPDF | Procesamiento de PDF |

---

# Estructura del proyecto

```
PALACE-AI/

│
├── application/
├── core/
├── infrastructure/
├── data/
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .env
```

La aplicación fue desarrollada siguiendo los principios de **Clean Architecture**, permitiendo una separación clara entre la lógica de negocio, infraestructura e interfaz de usuario. Esto facilita el mantenimiento, el escalamiento y la integración con otros sistemas.

---

# Requisitos

Antes de ejecutar el proyecto debes tener instalado:

- Python **3.12** (recomendado)
- Git

Puedes verificarlo ejecutando:

```bash
python --version
git --version
```

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/sagp3/PALACE-AI.git
```

---

## 2. Ingresar a la carpeta del proyecto

```bash
cd PALACE-AI
```

---

## 3. Crear el entorno virtual

```bash
python -m venv venv
```

Este comando creará una carpeta llamada:

```
venv/
```

---

## 4. Activar el entorno virtual

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

Cuando el entorno esté activo verás algo similar a:

```
(venv) PS C:\PALACE-AI>
```

### Windows (CMD)

```cmd
venv\Scripts\activate.bat
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

## 5. Actualizar pip

```bash
python -m pip install --upgrade pip
```

---

## 6. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Este proceso puede tardar algunos minutos dependiendo de la velocidad de internet.

---

# Configuración

En la carpeta principal del proyecto crea un archivo llamado:

```
.env
```

La estructura debe quedar así:

```
PALACE-AI/

application/
core/
infrastructure/
data/

.env
streamlit_app.py
requirements.txt
```

Dentro del archivo agrega tu API Key de OpenAI:

```text
OPENAI_API_KEY=tu_api_key
```

Ejemplo:

```text
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxx
```

---

# Ejecutar la aplicación

Con el entorno virtual activado ejecuta:

```bash
python -m streamlit run streamlit_app.py
```

La aplicación estará disponible en:

```
http://localhost:8501
```

---

# Primera ejecución

La primera vez que ejecutes PALACE AI el sistema creará automáticamente:

- Base de datos SQLite
- Base vectorial ChromaDB
- Carpetas para almacenamiento de documentos

Este proceso es completamente normal y solo ocurre una vez.

---

# Uso

1. Ejecuta la aplicación.
2. Abre la interfaz web.
3. Carga uno o varios documentos PDF o CSV.
4. Espera a que finalice la indexación.
5. Escribe una pregunta.
6. PALACE AI buscará los fragmentos más relevantes y generará una respuesta utilizando únicamente la información contenida en los documentos.

---

# Ejemplos de preguntas

## Documentos PDF

- ¿Cuál es la política de vacaciones?
- ¿Qué dice el manual sobre el proceso de recepción?
- ¿Cuáles son las responsabilidades del supervisor?
- ¿Cómo funciona el proceso de despacho?

## Archivos CSV

- ¿Cuál es el producto más costoso?
- ¿Cuántos registros existen?
- ¿Cuál es el precio promedio?
- ¿Qué productos están en producción?
- ¿Cuántos pedidos están pendientes?

---

# Solución de problemas

## Streamlit no se reconoce

Si aparece un mensaje similar a:

```
streamlit no se reconoce...
```

Ejecuta:

```bash
python -m streamlit run streamlit_app.py
```

---

## Error al activar el entorno virtual

Si PowerShell bloquea la ejecución de scripts, ejecuta una única vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Después vuelve a activar el entorno:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## OPENAI_API_KEY no encontrada

Verifica que exista un archivo llamado:

```
.env
```

con el siguiente contenido:

```text
OPENAI_API_KEY=tu_api_key
```

---

## Error al instalar dependencias

Actualiza pip:

```bash
python -m pip install --upgrade pip
```

Luego instala nuevamente:

```bash
pip install -r requirements.txt
```

---

# Futuras mejoras

- Soporte para Word (.docx)
- Soporte para Excel (.xlsx)
- Historial de conversaciones
- API REST
- Gestión de usuarios
- Dashboard administrativo
- Integración con sistemas ERP
- Soporte para múltiples modelos LLM

---

# Capturas

## Página principal

*(Agregar captura de la pantalla principal)*

---

## Chat

*(Agregar captura del chat)*

---

## Gestión de documentos

*(Agregar captura de la carga y eliminación de documentos)*

---

# Autor

Desarrollado por **Santiago Andrés** como parte del **Challenge Alura ONE – Agente Inteligente con IA**.

El proyecto implementa una arquitectura **Retrieval-Augmented Generation (RAG)** siguiendo principios de **Clean Architecture**, permitiendo una solución escalable, mantenible y preparada para futuras integraciones empresariales.
