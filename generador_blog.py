# Proyecto: Generador de Blogs 📝
# Nota: Adaptado para usar Google Gemini API (Gratis)

import google.generativeai as genai
from dotenv import dotenv_values

# Configuración de seguridad
config = dotenv_values('.env')
genai.configure(api_key=config['API_KEY'])

# Selección automática del modelo disponible
modelos = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
model = genai.GenerativeModel(modelos[0])


def generate_blog(paragraph_topic):
    # El prompt es igual al del tutorial
    prompt = f"Write a professional paragraph about the following topic: {paragraph_topic}"

    # Generamos el contenido
    response = model.generate_content(
        prompt,
        generation_config={
            "max_output_tokens": 400,
            "temperature": 0.3
        }
    )
    return response.text


# Bucle principal para múltiples párrafos
keep_writing = True

while keep_writing:
    answer = input('\n¿Escribir un párrafo? (Y para sí, cualquier otra tecla para salir): ').upper()

    if answer == 'Y':
        paragraph_topic = input('¿De qué debería tratar este párrafo?: ')
        print("\nGenerando...")
        print(generate_blog(paragraph_topic))
    else:
        print("\n¡Gracias por usar el generador! Hasta luego.")
        keep_writing = False