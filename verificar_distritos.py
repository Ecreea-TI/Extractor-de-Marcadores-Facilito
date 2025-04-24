import mysql.connector
import json
from math import radians, sin, cos, sqrt, atan2

def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371  # Radio de la Tierra en kilómetros
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

try:
    print("Conectando a la base de datos...")
    conn = mysql.connector.connect(
        host='bh7114.banahosting.com',
        port=3306,
        database='fcqngeyc_dataPricingApp',
        user='fcqngeyc_adminApp',
        password='emkappprecios12',
        connect_timeout=60
    )
    cursor = conn.cursor()

    # Verificar distritos
    print("\nVerificando distritos de La Libertad...")
    cursor.execute("SELECT COUNT(*) FROM distritos WHERE provincia_id LIKE '13%'")
    count = cursor.fetchone()[0]
    print(f"Número de distritos encontrados: {count}")

    if count == 0:
        print("No hay distritos en la base de datos. Insertando desde ubigeo_peru.json...")
        with open('ubigeo_peru.json') as f:
            ubigeo_data = json.load(f)
            
        for departamento in ubigeo_data['departamentos']:
            if departamento['id'] == '13':  # La Libertad
                for provincia in departamento['provincias']:
                    for distrito in provincia['distritos']:
                        cursor.execute("""
                            INSERT IGNORE INTO distritos (id, provincia_id, nombre, latitud, longitud)
                            VALUES (%s, %s, %s, %s, %s)
                        """, (
                            distrito['id'],
                            provincia['id'],
                            distrito['nombre'],
                            distrito['coordenadas']['latitud'],
                            distrito['coordenadas']['longitud']
                        ))
                print("Distritos insertados correctamente")
                conn.commit()

    # Mostrar algunos distritos para verificar
    print("\nMostrando primeros 5 distritos:")
    cursor.execute("SELECT id, nombre, latitud, longitud FROM distritos WHERE provincia_id LIKE '13%' LIMIT 5")
    for distrito in cursor.fetchall():
        print(f"ID: {distrito[0]}, Nombre: {distrito[1]}, Lat: {distrito[2]}, Long: {distrito[3]}")

    # Verificar estaciones sin distrito
    print("\nVerificando estaciones sin distrito asignado...")
    cursor.execute("SELECT codigo_osinergmin, nombre, latitud, longitud FROM estaciones WHERE distrito_id IS NULL")
    estaciones_sin_distrito = cursor.fetchall()
    print(f"Número de estaciones sin distrito: {len(estaciones_sin_distrito)}")

    # Obtener todos los distritos de La Libertad
    cursor.execute("SELECT id, nombre, latitud, longitud FROM distritos WHERE provincia_id LIKE '13%'")
    distritos = cursor.fetchall()

    # Asignar distritos a las estaciones
    print("\nAsignando distritos a las estaciones...")
    for estacion in estaciones_sin_distrito:
        codigo_osinergmin, nombre, lat_estacion, long_estacion = estacion
        
        distrito_mas_cercano = None
        distancia_minima = float('inf')
        nombre_distrito = None
        
        for distrito in distritos:
            distancia = calcular_distancia(
                float(lat_estacion),
                float(long_estacion),
                float(distrito[2]),  # latitud
                float(distrito[3])   # longitud
            )
            if distancia < distancia_minima:
                distancia_minima = distancia
                distrito_mas_cercano = distrito[0]
                nombre_distrito = distrito[1]
        
        if distrito_mas_cercano:
            print(f"\nEstación: {nombre}")
            print(f"Distrito más cercano: {nombre_distrito}")
            print(f"Distancia: {distancia_minima:.2f} km")
            
            cursor.execute("""
                UPDATE estaciones 
                SET distrito_id = %s 
                WHERE codigo_osinergmin = %s
            """, (distrito_mas_cercano, codigo_osinergmin))
            
            print(f"Actualizada estación {codigo_osinergmin}")
    
    conn.commit()
    print("\nProceso completado.")

except Exception as e:
    print(f"Error: {str(e)}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexión cerrada") 