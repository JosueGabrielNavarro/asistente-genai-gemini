#------------------
# @Josue Navarro
# Main.py
#------------------

#Importing \...|.../...-....
import os
from dotenv import load_dotenv
from google.cloud import aiplatform
from vertexai.generative_models import GenerativeModel

#Importing prompt_toolkit \...|.../...-...
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.formatted_text import HTML

# --- CONFIGURACION INICIAL & CARGA DE CREDENCIALES ---
def get_load_credentials():
    """Carga de las variables de entorno desde el archivo .env"""
    load_dotenv()
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    project_id = os.getenv("GCP_PROJECT_ID")
    location = os.getenv("GCP_LOCATION")
    return credentials_path, project_id, location
    
def init_vertexai(credentials_path, project_id, location):
    if not credentials_path or not os.path.exists(credentials_path):
        print("---------------------------------------------------------------------------------------------------")
        print("ERROR: La variable de entorno GOOGLE_APPLICATION_CREDENTIALS no está configurada")
        print("o la ruta al archivo JSON de credenciales no existe.")
        print("Asegúrate de que tu archivo .env tiene la línea:")
        print("GOOGLE_APPLICATION_CREDENTIALS=/ruta/a/tu/cuenta-de-servicio.json")
        print("Y que el archivo JSON existe en esa ruta.")
        print("---------------------------------------------------------------------------------------------------")
        exit()
    if not project_id:
        print("---------------------------------------------------------------------------------------------------")
        print("ERROR: La variable de entorno GCP_PROJECT_ID no está configurada")
        print("o la ruta al archivo JSON de credenciales no existe.")
        print("Asegúrate de que tu archivo .env tiene la línea:")
        print("GCP_PROJECT_ID=id_de_tu_proyecto")
        print("Y que el archivo JSON existe en esa ruta.")
        print("---------------------------------------------------------------------------------------------------")
        exit()
    if not location:
        print("---------------------------------------------------------------------------------------------------")
        print("ERROR: La variable de entorno GCP_LOCATION no está configurada")
        print("o la ruta al archivo JSON de credenciales no existe.")
        print("Asegúrate de que tu archivo .env tiene la línea:")
        print("GCP_LOCATION=region_de_tu_projecto")
        print("Y que el archivo JSON existe en esa ruta.")
        print("---------------------------------------------------------------------------------------------------")
        exit()
    
    try:
        aiplatform.init(project=project_id, location=location)
        print(f"✅ Vertex AI inicializado para el proyecto '{project_id}' en la region '{location}'")
    except Exception as e:
        print(f"---------------------------------------------------------------------------------------------------")
        print(f"ERROR: No se pudo inicializar Vertex AI.")
        print(f"Verifica tu GOOGLE_APPLICATION_CREDENTIALS, PROJECT_ID y LOCATION.")
        print(f"Detalle del error: {e}")
        print(f"---------------------------------------------------------------------------------------------------")
        exit()

    return project_id, location

# --- FUNCION PRINCIPAL DEL PROGRAMA ---
def main():
    credentials_path, project_id, location = get_load_credentials()
    project_id, location = init_vertexai(credentials_path=credentials_path, project_id=project_id, location=location)
    
    # --- CARGA DEL MODELO ---
    model_name = "gemini-2.5-flash"
    try:
        model = GenerativeModel(model_name)
        print(f"✅ Modelo '{model._model_name}' cargado exitosamente.")
    except Exception as e:
        print(f"---------------------------------------------------------------------------------------------------")
        print(f"ERROR: No se pudo cargar correctamente el modelo '{model_name}'.")
        print(f"Asegúrate de que el modelo '{model_name}' está disponible en la región '{location}' para tu proyecto.")
        print(f"Detalle del error: {e}")
        print(f"---------------------------------------------------------------------------------------------------")
        exit()
    
    # --- DEFINIR SU ROL ---
    system_prompt = """
    Eres un asistente de programación experto y amigable.
    Tu objetivo es ayudar a los usuarios con dudas de código, explicar conceptos, depurar pequeños fragmentos y generar ejemplos claros.
    Responde de forma concisa pero completa, y siempre usa bloques de código cuando sea apropiado.
    Si te piden algo fuera de programación, indica amablemente que tu enfoque es el código.
    """

    print("\n🤖 ¡Hola! Soy tu Asistente de Código GenAI. ¿En qué puedo ayudarte hoy?\n")
    print("Puedes escribir 'salir' o 'bye' o 'quit' para terminar la conversación.")
    print("Para enviar código multi-línea, presiona <Mays/Shift>+<Enter> (o <Alt>+<Enter> en algunos terminales).")
    print("Para el historial, usa las flechas arriba/abajo.")

    # PARA EVITAR LA REPETICION INFINITA, EN CASO DE ERRORES (YA ME PASO Y ME ASUSTE MUCHO):
    # ACTIVA SOLO POR PREVENCION
    #calls_count = 0
    #MAX_CALLS_COUNT = 5

    # INICIALIZACION DE prompt_toolkit
    session = PromptSession(history= InMemoryHistory())

    # BUCLE DE CONVERSACION INTERACTIVO
    while True:
        try:
            #calls_count +=1
            #if calls_count >= MAX_CALLS_COUNT:
            #    print("Limite de llamadas alcanzado")
            #    break

            promptColor = HTML("<ansiyellow>💻 Tú:</ansiyellow>")
            userInput = session.prompt(promptColor)

            if userInput.lower() in ['bye', 'salir', 'quit', 'adios', 'exit']:
                print("🤖 ¡Hasta luego! ¡Feliz codificación!")
                break

            fullPrompt = f"{system_prompt}\n\nPregunta del usuario: {userInput}"

            response = model.generate_content(
                fullPrompt,
                generation_config={
                    "temperature": 0.6,
                    "max_output_tokens":  4096
                }
            )
        
            print("\n🤖 Asistente:")
            print("---------------------------------------------------------------------------------------------------")
            if response.candidates:
                if response.candidates[0] and response.candidates[0].content.parts[0]:
                    print(response.candidates[0].content.parts[0].text)
                else:
                    print("El modelo no generó partes de texto válidas para el candidato.")
                    print("Objeto response completo para depuración:")
                    print(response)
            else:
                print("El modelo no genero los cadidatos a la respuesta:")
                print(response)
            print("---------------------------------------------------------------------------------------------------")

        except KeyboardInterrupt:
            print("\nConversacion terminada por el usario")
            break
        except Exception as e:
            print("\n❌ ¡Oops! Hubo un error al comunicarse con el modelo.")
            print(f"Detalles: {e}")
            break

if __name__ == "__main__":
    main()