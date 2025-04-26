import mysql.connector
import json
from mysql.connector import Error

def get_or_create_departamento(cursor, nombre, codigo_ubigeo, latitud, longitud):
    # Buscar departamento existente
    cursor.execute("SELECT id FROM departamentos WHERE codigo_ubigeo = %s", (codigo_ubigeo,))
    result = cursor.fetchone()
    
    if result:
        print(f"Departamento encontrado con ID: {result[0]}")
        return result[0]
    
    # Si no existe, crear uno nuevo
    print(f"Creando nuevo departamento: {nombre}")
    cursor.execute("""
        INSERT INTO departamentos (nombre, codigo_ubigeo, latitud, longitud)
        VALUES (%s, %s, %s, %s)
    """, (nombre, codigo_ubigeo, latitud, longitud))
    return cursor.lastrowid

def get_or_create_provincia(cursor, departamento_id, nombre, codigo_ubigeo, latitud, longitud):
    # Buscar provincia existente
    cursor.execute("SELECT id FROM provincias WHERE codigo_ubigeo = %s", (codigo_ubigeo,))
    result = cursor.fetchone()
    
    if result:
        print(f"Provincia encontrada con ID: {result[0]}")
        return result[0]
    
    # Si no existe, crear una nueva
    print(f"Creando nueva provincia: {nombre}")
    cursor.execute("""
        INSERT INTO provincias (departamento_id, nombre, codigo_ubigeo, latitud, longitud)
        VALUES (%s, %s, %s, %s, %s)
    """, (departamento_id, nombre, codigo_ubigeo, latitud, longitud))
    return cursor.lastrowid

def get_or_create_distrito(cursor, provincia_id, nombre, codigo_ubigeo, latitud, longitud):
    # Buscar distrito existente
    cursor.execute("SELECT id FROM distritos WHERE codigo_ubigeo = %s", (codigo_ubigeo,))
    result = cursor.fetchone()
    
    if result:
        print(f"Distrito encontrado con ID: {result[0]}")
        return result[0]
    
    # Si no existe, crear uno nuevo
    print(f"Creando nuevo distrito: {nombre}")
    cursor.execute("""
        INSERT INTO distritos (provincia_id, nombre, codigo_ubigeo, latitud, longitud)
        VALUES (%s, %s, %s, %s, %s)
    """, (provincia_id, nombre, codigo_ubigeo, latitud, longitud))
    return cursor.lastrowid

def upload_ubigeo_data():
    try:
        print("Iniciando conexión a la base de datos...")
        # Conexión a la base de datos
        connection = mysql.connector.connect(
            host='bh7114.banahosting.com',
            port=3306,
            database='fcqngeyc_dataPricingApp',
            user='fcqngeyc_adminApp',
            password='emkappprecios12',
            connect_timeout=60
        )
        print("Conexión exitosa a la base de datos")

        cursor = connection.cursor()

        # Leer el archivo JSON
        print("\nLeyendo archivo JSON...")
        with open('ubigeo_peru.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Procesar cada departamento
        for departamento in data['departamentos']:
            print(f"\nProcesando departamento: {departamento['nombre']}")
            
            # Obtener o crear departamento
            departamento_id = get_or_create_departamento(
                cursor,
                departamento['nombre'],
                departamento['id'],
                departamento['coordenadas']['latitud'],
                departamento['coordenadas']['longitud']
            )

            # Procesar cada provincia
            for provincia in departamento['provincias']:
                print(f"  Procesando provincia: {provincia['nombre']}")
                
                # Obtener o crear provincia
                provincia_id = get_or_create_provincia(
                    cursor,
                    departamento_id,
                    provincia['nombre'],
                    provincia['id'],
                    provincia['coordenadas']['latitud'],
                    provincia['coordenadas']['longitud']
                )

                # Procesar cada distrito
                for distrito in provincia['distritos']:
                    print(f"    Procesando distrito: {distrito['nombre']}")
                    
                    # Obtener o crear distrito
                    get_or_create_distrito(
                        cursor,
                        provincia_id,
                        distrito['nombre'],
                        distrito['id'],
                        distrito['coordenadas']['latitud'],
                        distrito['coordenadas']['longitud']
                    )

            # Commit después de cada departamento
            connection.commit()
            print(f"Departamento {departamento['nombre']} procesado exitosamente")

        print("\n¡Proceso completado exitosamente!")

    except Error as e:
        print(f"Error: {e}")
        if 'connection' in locals() and connection.is_connected():
            connection.rollback()

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    upload_ubigeo_data() 