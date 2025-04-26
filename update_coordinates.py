import json

# Coordenadas actualizadas de las capitales de los departamentos
updated_coordinates = {
    "03": {
        "nombre": "APURIMAC",
        "coordenadas": {"latitud": -13.6333, "longitud": -73.4000}
    },
    "04": {
        "nombre": "AREQUIPA",
        "coordenadas": {"latitud": -16.3989, "longitud": -71.5350}
    },
    "05": {
        "nombre": "AYACUCHO",
        "coordenadas": {"latitud": -13.1631, "longitud": -74.2244}
    },
    "07": {
        "nombre": "CALLAO",
        "coordenadas": {"latitud": -12.0333, "longitud": -77.1333}
    },
    "16": {
        "nombre": "LORETO",
        "coordenadas": {"latitud": -3.7481, "longitud": -73.2472}
    },
    "17": {
        "nombre": "MADRE DE DIOS",
        "coordenadas": {"latitud": -12.6000, "longitud": -69.1833}
    },
    "18": {
        "nombre": "MOQUEGUA",
        "coordenadas": {"latitud": -17.1956, "longitud": -70.9353}
    },
    "19": {
        "nombre": "PASCO",
        "coordenadas": {"latitud": -10.6833, "longitud": -76.2667}
    },
    "20": {
        "nombre": "PIURA",
        "coordenadas": {"latitud": -5.2000, "longitud": -80.6333}
    },
    "21": {
        "nombre": "PUNO",
        "coordenadas": {"latitud": -15.8433, "longitud": -70.0236}
    },
    "22": {
        "nombre": "SAN MARTIN",
        "coordenadas": {"latitud": -6.5000, "longitud": -76.3667}
    },
    "23": {
        "nombre": "TACNA",
        "coordenadas": {"latitud": -18.0067, "longitud": -70.2461}
    },
    "24": {
        "nombre": "TUMBES",
        "coordenadas": {"latitud": -3.5667, "longitud": -80.4500}
    },
    "25": {
        "nombre": "UCAYALI",
        "coordenadas": {"latitud": -8.3800, "longitud": -74.5200}
    }
}

# Leer el archivo JSON
with open('ubigeo_peru.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Actualizar o agregar departamentos
for dept_id, dept_info in updated_coordinates.items():
    found = False
    for departamento in data['departamentos']:
        if departamento['id'] == dept_id:
            departamento['nombre'] = dept_info['nombre']
            departamento['coordenadas'] = dept_info['coordenadas']
            print(f"Actualizado departamento {dept_info['nombre']} (ID: {dept_id})")
            found = True
            break
    
    if not found:
        # Agregar nuevo departamento
        new_dept = {
            "id": dept_id,
            "nombre": dept_info['nombre'],
            "coordenadas": dept_info['coordenadas'],
            "provincias": []
        }
        data['departamentos'].append(new_dept)
        print(f"Agregado nuevo departamento {dept_info['nombre']} (ID: {dept_id})")

# Ordenar departamentos por ID
data['departamentos'].sort(key=lambda x: x['id'])

# Guardar el archivo actualizado
with open('ubigeo_peru_updated.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\nArchivo actualizado guardado como 'ubigeo_peru_updated.json'") 