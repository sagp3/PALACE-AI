# 🤖 PALACE AI

## Enterprise Document Assistant

PALACE AI es un asistente inteligente basado en **Retrieval-Augmented Generation (RAG)** que permite consultar documentos empresariales mediante lenguaje natural utilizando Inteligencia Artificial.

El sistema procesa documentos PDF y CSV, genera embeddings mediante OpenAI, almacena la información en ChromaDB y responde preguntas utilizando únicamente la información encontrada en los documentos.

---

# 🚀 Demo

Puedes probar la aplicación directamente desde el navegador sin instalar nada.

### 🌐 Aplicación

https://palace.streamlit.app/

---

# 💻 Código Fuente

Repositorio oficial:

https://github.com/sagp3/PALACE-AI.git

---

# Características

- 📄 Carga de documentos PDF
- 📊 Carga de archivos CSV
- 🧠 Búsqueda semántica mediante OpenAI Embeddings
- 🤖 Respuestas generadas con OpenAI GPT
- 📚 Base de datos vectorial ChromaDB
- 🗄 Persistencia mediante SQLite
- 🚫 Detección automática de documentos duplicados
- 🗑 Eliminación de documentos
- 💬 Interfaz web desarrollada con Streamlit
- 🏗 Arquitectura basada en Clean Architecture

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
     OpenAI Embeddings       ChromaDB
            │
            ▼
        Prompt Builder
            │
            ▼
      OpenAI GPT-4.1 Mini
            │
            ▼
          Respuesta
```

---

# Flujo del sistema

1. El usuario carga uno o varios documentos.
2. El sistema extrae el texto.
3. El documento se divide en pequeños fragmentos (Chunks).
4. Se genera un embedding para cada fragmento.
5. Los embeddings se almacenan en ChromaDB.
6. El usuario realiza una pregunta.
7. Se genera el embedding de la pregunta.
8. ChromaDB busca los fragmentos más similares.
9. OpenAI recibe únicamente esos fragmentos.
10. Se genera una respuesta utilizando exclusivamente la información encontrada.

---

# Tecnologías utilizadas

| Tecnología | Uso |
|------------|--------------------------------|
| Python 3.12 | Lenguaje principal |
| Streamlit | Interfaz web |
| OpenAI GPT | Modelo de lenguaje |
| OpenAI Embeddings | Embeddings |
| ChromaDB | Base de datos vectorial |
| SQLite | Persistencia |
| Pandas | Procesamiento de CSV |
| PyPDF | Lectura de PDF |

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

La aplicación fue desarrollada siguiendo los principios de **Clean Architecture**, separando la lógica de negocio de la infraestructura y de la interfaz de usuario.

Esto facilita el mantenimiento, el escalamiento y la integración con otros sistemas.

---

# Requisitos

Antes de comenzar debes tener instalado:

- Python 3.12 o superior
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

## 2. Ingresar al proyecto

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

Si aparece el mensaje:

```
La ejecución de scripts está deshabilitada en este sistema.
```

Ejecuta una única vez:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Acepta escribiendo:

```
Y
```

Luego vuelve a ejecutar:

```powershell
.\venv\Scripts\Activate.ps1
```

Cuando el entorno esté activo verás algo parecido a:

```
(venv) PS C:\PALACE-AI>
```

---

### Windows (CMD)

```cmd
venv\Scripts\activate.bat
```

---

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

La instalación puede tardar algunos minutos dependiendo de la velocidad de internet.

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

Dentro del archivo agrega tu API Key de OpenAI.

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
- Carpeta de almacenamiento de documentos

Este proceso es completamente normal y solo ocurre la primera vez.

---

# Uso

1. Ejecuta la aplicación.
2. Abre la interfaz web.
3. Carga uno o varios documentos PDF o CSV.
4. Espera a que finalice la indexación.
5. Escribe una pregunta.
6. El sistema buscará los fragmentos más relevantes y generará una respuesta basada únicamente en la información encontrada.

---

# Ejemplos de preguntas

## PDF

- ¿Cuál es la política de vacaciones?
- ¿Qué dice el manual sobre el proceso de recepción?
- ¿Cuáles son las responsabilidades del supervisor?
- ¿Cómo funciona el proceso de despacho?

## CSV

- ¿Cuál es el producto más costoso?
- ¿Cuál es el precio promedio?
- ¿Cuántos registros existen?
- ¿Cuántos pedidos están pendientes?
- ¿Qué productos están en producción?

---

# Solución de problemas

## Streamlit no se reconoce

Si aparece un error como:

```
streamlit no se reconoce...
```

Ejecuta:

```bash
python -m streamlit run streamlit_app.py
```

---

## Error al activar el entorno virtual

Si PowerShell muestra:

```
La ejecución de scripts está deshabilitada en este sistema.
```

Ejecuta una única vez:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Acepta con:

```
Y
```

Después activa nuevamente el entorno:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## OPENAI_API_KEY no encontrada

Verifica que exista un archivo:

```
.env
```

con el contenido:

```text
OPENAI_API_KEY=tu_api_key
```

---

## Error al instalar dependencias

Actualiza pip:

```bash
python -m pip install --upgrade pip
```

Luego vuelve a instalar:

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

# Autor

Desarrollado por **Santiago Andrés** como parte del **Challenge Alura ONE – Agente Inteligente con IA**.

PALACE AI implementa una arquitectura **Retrieval-Augmented Generation (RAG)** siguiendo los principios de **Clean Architecture**, permitiendo una solución escalable, mantenible y preparada para futuras integraciones empresariales.
