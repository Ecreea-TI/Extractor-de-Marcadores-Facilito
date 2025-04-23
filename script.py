import requests
import re
import json
import unicodedata

def normalize_text(text):
    """
    Normaliza el texto a UTF-8 y elimina caracteres especiales innecesarios
    """
    if isinstance(text, str):
        # Normalizar caracteres Unicode
        text = unicodedata.normalize('NFKD', text)
        # Convertir a ASCII pero mantener ñ y tildes
        text = text.encode('utf-8').decode('utf-8')
        # Eliminar espacios extras
        text = ' '.join(text.split())
    return text

def extract_facilito_data(url):
    try:
        print("Iniciando petición HTTP...")
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        html_content = response.text
        print("Petición HTTP exitosa")
        
        # Buscar la línea que contiene listaPuntos
        print("\nBuscando datos en el HTML...")
        pattern = r'var\s+listaPuntos\s*=\s*eval\s*\(\s*\'\(\'\s*\+\s*\'(.*?)\'\s*\+\s*\'\)\'\s*\)'
        match = re.search(pattern, html_content, re.DOTALL)
        
        if match:
            print("Datos encontrados, procesando...")
            data_string = match.group(1)
            # Limpiar caracteres no deseados
            data_string = data_string.strip()
            print(f"Datos extraídos (primeros 200 caracteres):")
            print(data_string[:200])
            
            try:
                # Intentar parsear como JSON directamente
                data = json.loads(data_string)
                print("Datos parseados exitosamente")
                return data
            except json.JSONDecodeError:
                print("Error al parsear JSON, intentando limpiar los datos...")
                return []
        else:
            print("No se encontró el patrón en el HTML")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición: {str(e)}")
        return []
    except Exception as e:
        print(f"Error general: {str(e)}")
        return []

def save_json_file(data, filename):
    """
    Guarda los datos en un archivo JSON con codificación UTF-8
    Conserva caracteres especiales como ñ y tildes
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logging.info(f"Datos guardados en '{filename}'")
        print(f"Los datos han sido guardados exitosamente en '{filename}'")
    except Exception as e:
        logging.error(f"Error al guardar el archivo: {str(e)}")
        print(f"Error al guardar el archivo: {str(e)}")

# URL objetivo
url = "https://www.facilito.gob.pe/facilito/actions/MapaAction.do?departamento=150000&provincia=150100&distrito=9999999&producto=126&method=mostrarMapa&subtitulocabecera=1&tipo=LIQ&codigoOSI=84523"

# Ejecutar la extracción
result = extract_facilito_data(url)
if result:
    with open('facilito_data.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print("Los datos han sido guardados exitosamente en 'facilito_data.json'")
    print("\nPrimeros 500 caracteres del resultado:")
    print(json.dumps(result, ensure_ascii=False)[:500])
else:
    print("No se encontraron datos para guardar.")
