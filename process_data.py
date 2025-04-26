import json
import os
from datetime import datetime
import requests
import re
import unicodedata

def normalize_text(text):
    """
    Normaliza el texto a UTF-8 y elimina caracteres especiales innecesarios
    """
    if isinstance(text, str):
        text = unicodedata.normalize('NFKD', text)
        text = text.encode('utf-8').decode('utf-8')
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
        
        pattern_puntos = r'var\s+listaPuntos\s*=\s*eval\s*\(\s*\'\(\'\s*\+\s*\'(.*?)\'\s*\+\s*\'\)\'\s*\)'
        match_puntos = re.search(pattern_puntos, html_content, re.DOTALL)
        
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

def convert_json_to_txt():
    """
    Convierte el archivo JSON a formato txt para el script original
    """
    try:
        with open('urls-todo-los-departamentos.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        with open('urls-todo-los-departamentos.txt', 'w', encoding='utf-8') as f:
            for departamento, provincias in data.items():
                f.write(f"{departamento}\n")
                
                if "TODOS" in provincias:
                    f.write(f"{provincias['TODOS']}\n")
                else:
                    for provincia, url in provincias.items():
                        if url:
                            f.write(f"{url}\n")
                f.write("\n")
        
        print("Archivo txt creado exitosamente")
    except Exception as e:
        print(f"Error al convertir JSON a txt: {str(e)}")

def verify_data_quality():
    """
    Verifica la calidad de los datos en el archivo JSON
    """
    try:
        total_provincias = 0
        provincias_con_datos = 0
        departamentos_sin_datos = 0
        
        with open('urls-todo-los-departamentos.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for departamento, provincias in data.items():
            if "TODOS" in provincias:
                continue
                
            total_provincias += len(provincias)
            provincias_con_datos += sum(1 for url in provincias.values() if url)
            
            if all(not url for url in provincias.values()):
                departamentos_sin_datos += 1
        
        print(f"\nReporte de Calidad de Datos:")
        print(f"Total de provincias: {total_provincias}")
        print(f"Provincias con datos: {provincias_con_datos}")
        print(f"Provincias sin datos: {total_provincias - provincias_con_datos}")
        print(f"Departamentos sin ningún dato: {departamentos_sin_datos}")
        
        return {
            'total_provincias': total_provincias,
            'provincias_con_datos': provincias_con_datos,
            'provincias_sin_datos': total_provincias - provincias_con_datos,
            'departamentos_sin_datos': departamentos_sin_datos
        }
    except Exception as e:
        print(f"Error al verificar calidad de datos: {str(e)}")
        return None

def clean_province_name(name):
    """
    Limpia el nombre de la provincia eliminando texto innecesario
    """
    return name.replace(' marcadores', '').replace(' provincias que incluyen distritos', '').strip()

def process_departments_with_logging():
    """
    Procesa los departamentos y registra las provincias faltantes
    """
    try:
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        with open('logs/provincias_faltantes.txt', 'w', encoding='utf-8') as log_file:
            with open('urls-todo-los-departamentos.json', 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            for departamento, provincias in json_data.items():
                log_file.write(f"\n=== {departamento} ===\n")
                
                for provincia, url in provincias.items():
                    if not url:
                        log_file.write(f"Provincia sin datos: {provincia}\n")
                
                if all(not url for url in provincias.values()):
                    log_file.write("¡ADVERTENCIA! Departamento sin datos\n")
        
        # Procesar los datos
        if not os.path.exists('json_departamentos'):
            os.makedirs('json_departamentos')
        
        with open('urls-todo-los-departamentos.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        all_data = {}
        current_department = None
        current_url = None
        
        # Conjunto para mantener registro de departamentos ya procesados
        processed_departments = set()
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if 'marcadores' in line:
                current_department = clean_province_name(line)
                if current_department not in processed_departments:
                    print(f"\nProcesando departamento: {current_department}")
                    all_data[current_department] = []
                    processed_departments.add(current_department)
            elif line.startswith('http'):
                current_url = line
                if current_department and current_url:
                    department_data = extract_facilito_data(current_url)
                    if department_data:
                        filename = f'json_departamentos/{current_department.lower().replace(" ", "_")}.json'
                        save_json_file(department_data, filename)
                        all_data[current_department].extend(department_data)
                        print(f"Se encontraron {len(department_data)} registros para {current_department}")
        
        if all_data:
            save_json_file(all_data, 'json_departamentos/todos_los_departamentos.json')
            total_registros = sum(len(datos) for datos in all_data.values())
            print(f"\nTotal de registros en todos los departamentos: {total_registros}")
            print("\nResumen por departamento:")
            # Usamos el orden original del JSON y limpiamos los nombres
            for departamento in json_data.keys():
                departamento_limpio = clean_province_name(departamento)
                registros = len(all_data.get(departamento_limpio, []))
                print(f"- {departamento}: {registros} registros")
        
    except Exception as e:
        print(f"Error en el procesamiento: {str(e)}")

def prepare_for_database():
    """
    Prepara los datos para la base de datos remota
    """
    try:
        database_ready_data = {}
        
        with open('json_departamentos/todos_los_departamentos.json', 'r', encoding='utf-8') as f:
            processed_data = json.load(f)
        
        for departamento, datos in processed_data.items():
            if datos:
                database_ready_data[departamento] = {
                    'total_registros': len(datos),
                    'fecha_actualizacion': datetime.now().isoformat(),
                    'datos': datos
                }
        
        with open('database_ready_data.json', 'w', encoding='utf-8') as f:
            json.dump(database_ready_data, f, indent=2, ensure_ascii=False)
        
        print("Datos preparados para base de datos guardados en 'database_ready_data.json'")
    except Exception as e:
        print(f"Error al preparar datos para base de datos: {str(e)}")

if __name__ == "__main__":
    # Paso 1: Convertir y verificar
    convert_json_to_txt()
    verify_data_quality()
    
    # Paso 2: Procesar datos
    process_departments_with_logging()
    
    # Paso 3: Preparar para base de datos
    prepare_for_database() 