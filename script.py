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
        
        # Guardar el HTML para inspección
        with open('debug.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("HTML guardado en debug.html para inspección")
        
        # Buscar la línea que contiene grifo
        print("\nBuscando línea con grifo...")
        for line in html_content.split('\n'):
            if 'grifo' in line:
                print("Línea encontrada:")
                print(line[:200] + "..." if len(line) > 200 else line)
                break
        
        # Buscar datos de listaPuntos
        print("\nBuscando datos de listaPuntos...")
        pattern_puntos = r'var\s+listaPuntos\s*=\s*eval\s*\(\s*\'\(\'\s*\+\s*\'(.*?)\'\s*\+\s*\'\)\'\s*\)'
        match_puntos = re.search(pattern_puntos, html_content, re.DOTALL)
        
        # Buscar datos de grifo
        print("\nBuscando datos de grifo...")
        pattern_grifo = r'var\s+grifo\s*=\s*eval\s*\(\s*\'\(\'\s*\+\s*\'(\{.*?\})\'\s*\+\s*\'\)\'\s*\)'
        match_grifo = re.search(pattern_grifo, html_content, re.DOTALL)
        
        result = []
        
        if match_puntos:
            print("Datos de listaPuntos encontrados, procesando...")
            data_string = match_puntos.group(1)
            data_string = data_string.strip()
            try:
                puntos_data = json.loads(data_string)
                print(f"Datos de listaPuntos parseados exitosamente: {len(puntos_data)} registros")
                result.extend(puntos_data)
            except json.JSONDecodeError as e:
                print(f"Error al parsear JSON de listaPuntos: {str(e)}")
        
        if match_grifo:
            print("Datos de grifo encontrados, procesando...")
            data_string = match_grifo.group(1)
            data_string = data_string.strip()
            print(f"Contenido de grifo: {data_string}")
            try:
                grifo_data = json.loads(data_string)
                print("Datos de grifo parseados exitosamente")
                if isinstance(grifo_data, dict):
                    # Normalizar la estructura si es necesario
                    normalized_item = {
                        "codigoOsinergmin": grifo_data.get("codigoOsinergmin", ""),
                        "latitud": grifo_data.get("latitud", 0),
                        "longitud": grifo_data.get("longitud", 0),
                        "unidad": grifo_data.get("unidad", ""),
                        "direccion": grifo_data.get("direccion", ""),
                        "productos": grifo_data.get("productos", [])
                    }
                    result.append(normalized_item)
                    print(f"Agregado registro de grifo: {normalized_item['codigoOsinergmin']}")
            except json.JSONDecodeError as e:
                print(f"Error al parsear JSON de grifo: {str(e)}")
        
        print(f"\nTotal de registros combinados: {len(result)}")
        return result
            
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
    print("\nDatos guardados exitosamente en 'facilito_data.json'")
    print("\nResumen de datos extraídos:")
    print(f"- Puntos encontrados: {len(result)}")
    print("\nPrimeros 500 caracteres del resultado:")
    print(json.dumps(result, ensure_ascii=False)[:500])
else:
    print("No se encontraron datos para guardar.")
