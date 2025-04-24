import mysql.connector
import json
from mysql.connector import Error
from datetime import datetime
import time

def get_or_create_departamento(cursor, nombre, codigo_ubigeo):
    # Buscar departamento existente
    cursor.execute("SELECT id FROM departamentos WHERE codigo_ubigeo = %s", (codigo_ubigeo,))
    result = cursor.fetchone()
    
    if result:
        print(f"Departamento encontrado con ID: {result[0]}")
        return result[0]
    
    # Si no existe, crear uno nuevo
    print(f"Creando nuevo departamento: {nombre}")
    cursor.execute("""
        INSERT INTO departamentos (nombre, codigo_ubigeo)
        VALUES (%s, %s)
    """, (nombre, codigo_ubigeo))
    return cursor.lastrowid

def get_or_create_provincia(cursor, departamento_id, nombre, codigo_ubigeo):
    # Buscar provincia existente
    cursor.execute("SELECT id FROM provincias WHERE codigo_ubigeo = %s", (codigo_ubigeo,))
    result = cursor.fetchone()
    
    if result:
        print(f"Provincia encontrada con ID: {result[0]}")
        return result[0]
    
    # Si no existe, crear una nueva
    print(f"Creando nueva provincia: {nombre}")
    cursor.execute("""
        INSERT INTO provincias (departamento_id, nombre, codigo_ubigeo)
        VALUES (%s, %s, %s)
    """, (departamento_id, nombre, codigo_ubigeo))
    return cursor.lastrowid

def get_or_create_distrito(cursor, provincia_id, nombre, codigo_ubigeo):
    # Buscar distrito existente
    cursor.execute("SELECT id FROM distritos WHERE codigo_ubigeo = %s", (codigo_ubigeo,))
    result = cursor.fetchone()
    
    if result:
        print(f"Distrito encontrado con ID: {result[0]}")
        return result[0]
    
    # Si no existe, crear uno nuevo
    print(f"Creando nuevo distrito: {nombre}")
    cursor.execute("""
        INSERT INTO distritos (provincia_id, nombre, codigo_ubigeo)
        VALUES (%s, %s, %s)
    """, (provincia_id, nombre, codigo_ubigeo))
    return cursor.lastrowid

def process_single_record(connection, item, departamento):
    cursor = connection.cursor()
    try:
        print("\nProcesando nuevo registro...")
        print(f"Datos del registro: {json.dumps(item, indent=2)}")
        
        # Obtener o crear departamento
        departamento_id = get_or_create_departamento(
            cursor, 
            departamento,  # Usar el nombre del departamento
            "15"     # Código de Lima
        )
        
        # Obtener o crear provincia
        provincia_id = get_or_create_provincia(
            cursor,
            departamento_id,
            "LIMA",  # Por ahora asumimos que todos son de Lima
            "1501"   # Código de Lima
        )
        
        # Obtener o crear distrito
        distrito_id = get_or_create_distrito(
            cursor,
            provincia_id,
            "LIMA",  # Por ahora asumimos que todos son de Lima
            "150101" # Código de Lima
        )
        
        # Verificar si el establecimiento ya existe
        codigo_osinergmin = item.get('codigoOsinergmin', '')
        print(f"Verificando establecimiento con código: {codigo_osinergmin}")
        
        cursor.execute("""
            SELECT id FROM establecimientos WHERE codigo_osinergmin = %s
        """, (codigo_osinergmin,))
        
        establecimiento_existente = cursor.fetchone()
        
        if establecimiento_existente:
            print(f"Establecimiento ya existe con ID: {establecimiento_existente[0]}")
            establecimiento_id = establecimiento_existente[0]
        else:
            print("Establecimiento no existe, insertando nuevo...")
            # Insertar establecimiento con el distrito_id
            cursor.execute("""
                INSERT INTO establecimientos 
                (distrito_id, nombre, direccion, latitud, longitud, codigo_osinergmin)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                distrito_id,
                item.get('unidad', ''),
                item.get('direccion', ''),
                float(item.get('latitud', 0)),
                float(item.get('longitud', 0)),
                codigo_osinergmin
            ))
            establecimiento_id = cursor.lastrowid
            print(f"Nuevo establecimiento insertado con ID: {establecimiento_id}")

        # Procesar productos
        if 'productos' in item:
            print(f"\nProcesando {len(item['productos'])} productos...")
            for producto in item['productos']:
                nombre_producto = producto.get('producto', '')
                precio = float(producto.get('precioVenta', 0))
                codigo_producto = nombre_producto.replace(' ', '_').upper()
                
                print(f"\nProcesando producto: {nombre_producto}")
                print(f"Precio: {precio}")
                
                # Insertar o obtener producto
                cursor.execute("""
                    INSERT IGNORE INTO productos (nombre, codigo)
                    VALUES (%s, %s)
                """, (nombre_producto, codigo_producto))
                
                cursor.execute("SELECT id FROM productos WHERE codigo = %s", (codigo_producto,))
                producto_id = cursor.fetchone()[0]
                print(f"ID del producto: {producto_id}")
                
                # Insertar o actualizar precio
                cursor.execute("""
                    INSERT INTO precios (establecimiento_id, producto_id, precio, fecha_actualizacion)
                    VALUES (%s, %s, %s, NOW())
                    ON DUPLICATE KEY UPDATE
                    precio = VALUES(precio),
                    fecha_actualizacion = NOW()
                """, (establecimiento_id, producto_id, precio))
                print(f"Precio actualizado/insertado")
                
                connection.commit()
                print("Commit realizado")
                time.sleep(0.1)  # Pequeña pausa para no sobrecargar la BD
        
        return True
        
    except Error as e:
        print(f"Error procesando registro: {e}")
        connection.rollback()
        return False
    finally:
        cursor.close()

def insert_data():
    try:
        print("Iniciando proceso de inserción...")
        
        # Configuración de la conexión
        connection = mysql.connector.connect(
            host='bh7114.banahosting.com',
            port=3306,
            database='fcqngeyc_dataPricingApp',
            user='fcqngeyc_adminApp',
            password='emkappprecios12',
            connect_timeout=60
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            
            # Leer el archivo JSON
            print("\nLeyendo archivo JSON...")
            with open('json_departamentos/todos_los_departamentos.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            total_registros = sum(len(registros) for registros in data.values())
            print(f"Se encontraron {total_registros} registros en total")
            print(f"Distribuidos en {len(data)} departamentos")
            
            # Procesar por departamento
            for departamento, registros in data.items():
                print(f"\n{'='*50}")
                print(f"Procesando departamento: {departamento}")
                print(f"Total de registros en {departamento}: {len(registros)}")
                
                # Procesar en lotes de 50 registros
                batch_size = 50
                total_batches = (len(registros) + batch_size - 1) // batch_size
                
                for batch_num in range(total_batches):
                    start_idx = batch_num * batch_size
                    end_idx = min((batch_num + 1) * batch_size, len(registros))
                    current_batch = registros[start_idx:end_idx]
                    
                    print(f"\nProcesando lote {batch_num + 1} de {total_batches} ({len(current_batch)} registros)")
                    
                    for i, item in enumerate(current_batch, 1):
                        print(f"\nProcesando registro {start_idx + i} de {len(registros)}")
                        if process_single_record(connection, item, departamento):
                            print(f"Registro {start_idx + i} procesado exitosamente")
                        else:
                            print(f"Error procesando registro {start_idx + i}")
                    
                    print(f"{'='*50}\n")
                    if batch_num < total_batches - 1:  # No esperar después del último lote
                        print("Esperando 5 segundos antes del siguiente lote...")
                        time.sleep(5)  # Pausa entre lotes
            
            print("\nProceso completado exitosamente")

    except Error as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insert_data() 