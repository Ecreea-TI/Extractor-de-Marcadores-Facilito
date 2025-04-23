import requests
import re
import json
import unicodedata
import os

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
        print(f"Iniciando petición HTTP para {url}...")
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'
        html_content = response.text
        print("Petición HTTP exitosa")
        
        # Buscar datos de listaPuntos
        pattern_puntos = r'var\s+listaPuntos\s*=\s*eval\s*\(\s*\'\(\'\s*\+\s*\'(.*?)\'\s*\+\s*\'\)\'\s*\)'
        match_puntos = re.search(pattern_puntos, html_content, re.DOTALL)
        
        # Buscar datos de grifo
        pattern_grifo = r'var\s+grifo\s*=\s*eval\s*\(\s*\'\(\'\s*\+\s*\'(\{.*?\})\'\s*\+\s*\'\)\'\s*\)'
        match_grifo = re.search(pattern_grifo, html_content, re.DOTALL)
        
        result = []
        
        if match_puntos:
            data_string = match_puntos.group(1)
            data_string = data_string.strip()
            try:
                puntos_data = json.loads(data_string)
                result.extend(puntos_data)
            except json.JSONDecodeError as e:
                print(f"Error al parsear JSON de listaPuntos: {str(e)}")
        
        if match_grifo:
            data_string = match_grifo.group(1)
            data_string = data_string.strip()
            try:
                grifo_data = json.loads(data_string)
                if isinstance(grifo_data, dict):
                    normalized_item = {
                        "codigoOsinergmin": grifo_data.get("codigoOsinergmin", ""),
                        "latitud": grifo_data.get("latitud", 0),
                        "longitud": grifo_data.get("longitud", 0),
                        "unidad": grifo_data.get("unidad", ""),
                        "direccion": grifo_data.get("direccion", ""),
                        "productos": grifo_data.get("productos", [])
                    }
                    result.append(normalized_item)
            except json.JSONDecodeError as e:
                print(f"Error al parsear JSON de grifo: {str(e)}")
        
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
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Los datos han sido guardados exitosamente en '{filename}'")
    except Exception as e:
        print(f"Error al guardar el archivo: {str(e)}")

def process_departments():
    # Crear directorio para los archivos JSON si no existe
    if not os.path.exists('json_departamentos'):
        os.makedirs('json_departamentos')
    
    # Leer el archivo de URLs
    with open('urls-todo-los-departamentos.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    all_data = []
    current_department = None
    current_url = None
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if 'marcadores' in line:
            # Es una línea de departamento
            current_department = line.replace(' marcadores', '').strip()
            print(f"\nProcesando departamento: {current_department}")
        elif line.startswith('http'):
            # Es una URL
            current_url = line
            if current_department and current_url:
                # Extraer datos del departamento
                department_data = extract_facilito_data(current_url)
                if department_data:
                    # Guardar archivo individual del departamento
                    filename = f'json_departamentos/{current_department.lower().replace(" ", "_")}.json'
                    save_json_file(department_data, filename)
                    all_data.extend(department_data)
                    print(f"Se encontraron {len(department_data)} registros para {current_department}")
    
    # Guardar archivo general con todos los datos
    if all_data:
        save_json_file(all_data, 'json_departamentos/todos_los_departamentos.json')
        print(f"\nTotal de registros en todos los departamentos: {len(all_data)}")

if __name__ == "__main__":
    process_departments()
