# 💻 Asistente de Código GenAI con Google Gemini y Vertex AI

Este proyecto es un asistente de código interactivo impulsado por Inteligencia Artificial, desarrollado en Python, que utiliza el modelo `gemini-2.5-flash` de Google a través de la plataforma Vertex AI. Su objetivo es ayudar a los desarrolladores con preguntas de programación, explicación de conceptos, depuración de fragmentos de código y generación de ejemplos claros en un entorno de consola interactivo.

---

## ✨ Características Principales

* **Asistente de Programación Inteligente:** Responde a tus preguntas de código con la potencia de Google Gemini-Flash 2.5.
* **Gestión de Credenciales Segura:** Carga las credenciales de Google Cloud desde un archivo `.env` para mantener la información sensible fuera del código fuente.
* **Manejo Robusto de Errores:** Incluye validaciones para la configuración de Vertex AI y un sistema de control de llamadas para prevenir bucles infinitos durante el desarrollo.
* **Despliegue en Google Cloud:** Diseñado para interactuar con los servicios de IA de Google Cloud Platform.

---

## 🚀 Cómo Empezar

Sigue estos pasos para configurar y ejecutar el asistente en tu entorno local.

### 📋 Prerrequisitos

Antes de comenzar, asegúrate de tener lo siguiente:

* **Python 3.9+** instalado.
* **`pip`** (administrador de paquetes de Python).
* Una **cuenta de Google Cloud Platform (GCP)**.
* Un **proyecto de GCP** con la facturación habilitada.
* **APIs de Vertex AI y Cloud Build habilitadas** en tu proyecto de GCP.
* **Credenciales de autenticación de GCP:** Un archivo JSON de clave de cuenta de servicio con los roles necesarios (ej. `Vertex AI User`, `Service Account User`).
* **Git** instalado (para clonar este repositorio).

### ⚙️ Configuración del Entorno

1.  **Clona este repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/asistente-genai-gemini.git](https://github.com/TU_USUARIO/asistente-genai-gemini.git)
    cd asistente-genai-gemini
    ```
    *(Asegúrate de reemplazar `TU_USUARIO` con tu nombre de usuario de GitHub y `asistente-genai-gemini` con el nombre real de tu repositorio si es diferente).*

2.  **Crea un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    ```

3.  **Activa el entorno virtual:**
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS / Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configura tus credenciales (archivo `.env`):**
    Crea un archivo llamado `.env` en la raíz de tu proyecto (la misma carpeta donde está `main.py`). Este archivo **NO debe ser subido a GitHub** (ya está incluido en el `.gitignore`).

    Añade las siguientes líneas, reemplazando los valores con tu información de GCP:

    ```
    GOOGLE_APPLICATION_CREDENTIALS=/ruta/a/tu/archivo-de-credenciales.json
    GCP_PROJECT_ID=tu-id-de-proyecto-gcp
    GCP_LOCATION=tu-region-gcp # Ej. us-central1, southamerica-east1
    ```
    *Asegúrate de que la ruta a tu archivo JSON de credenciales sea correcta y accesible.*

### ▶️ Ejecutar el Asistente

Una vez que hayas configurado todo, puedes ejecutar el asistente:

```bash
python main.py
