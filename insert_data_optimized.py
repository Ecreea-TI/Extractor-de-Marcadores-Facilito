import mysql.connector
import json
from mysql.connector import Error
from datetime import datetime

def process_batch(connection, batch_data):
    cursor = connection.cursor()
    records_processed = 0
    try:
        for item in batch_data:
            try:
                print(f"Procesando registro {records_processed + 1}...")
                
                # Insertar en departamentos
                print("-> Insertando departamento...")
                cursor.execute("""
                    INSERT IGNORE INTO departamentos (nombre, codigo_ubigeo)
                    VALUES (%s, %s)
                """, (item.get('departamento', ''), item.get('codigo_departamento', '')))

                # Obtener el ID del departamento
                cursor.execute("SELECT id FROM departamentos WHERE codigo_ubigeo = %s", 
                             (item.get('codigo_departamento', ''),))
                result = cursor.fetchone()
                if not result:
                    print(f"Error: No se pudo obtener el ID del departamento para el código {item.get('codigo_departamento', '')}")
                    continue
                departamento_id = result[0]

                # Insertar en provincias
                print("-> Insertando provincia...")
                cursor.execute("""
                    INSERT IGNORE INTO provincias (departamento_id, nombre, codigo_ubigeo)
                    VALUES (%s, %s, %s)
                """, (departamento_id, item.get('provincia', ''), item.get('codigo_provincia', '')))

                # Obtener el ID de la provincia
                cursor.execute("SELECT id FROM provincias WHERE codigo_ubigeo = %s", 
                             (item.get('codigo_provincia', ''),))
                result = cursor.fetchone()
                if not result:
                    print(f"Error: No se pudo obtener el ID de la provincia para el código {item.get('codigo_provincia', '')}")
                    continue
                provincia_id = result[0]

                # Insertar en distritos
                print("-> Insertando distrito...")
                cursor.execute("""
                    INSERT IGNORE INTO distritos (provincia_id, nombre, codigo_ubigeo)
                    VALUES (%s, %s, %s)
                """, (provincia_id, item.get('distrito', ''), item.get('codigo_distrito', '')))

                # Obtener el ID del distrito
                cursor.execute("SELECT id FROM distritos WHERE codigo_ubigeo = %s", 
                             (item.get('codigo_distrito', ''),))
                result = cursor.fetchone()
                if not result:
                    print(f"Error: No se pudo obtener el ID del distrito para el código {item.get('codigo_distrito', '')}")
                    continue
                distrito_id = result[0]

                # Insertar en establecimientos
                print("-> Insertando establecimiento...")
                cursor.execute("""
                    INSERT IGNORE INTO establecimientos 
                    (distrito_id, nombre, direccion, latitud, longitud, codigo_osinergmin)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (distrito_id, 
                      item.get('unidad', ''),  # Cambiado de nombre_establecimiento a unidad
                      item.get('direccion', ''),
                      item.get('latitud', 0),
                      item.get('longitud', 0),
                      item.get('codigoOsinergmin', '')))  # Cambiado de codigo_osinergmin a codigoOsinergmin

                # Obtener el ID del establecimiento
                cursor.execute("SELECT id FROM establecimientos WHERE codigo_osinergmin = %s", 
                             (item.get('codigoOsinergmin', ''),))  # Cambiado aquí también
                result = cursor.fetchone()
                if not result:
                    print(f"Error: No se pudo obtener el ID del establecimiento para el código {item.get('codigoOsinergmin', '')}")
                    continue
                establecimiento_id = result[0]

                # Insertar productos y precios
                if 'productos' in item:
                    print(f"-> Procesando {len(item['productos'])} productos...")
                    for producto in item['productos']:
                        nombre_producto = producto.get('producto', '')  # Cambiado de nombre a producto
                        precio = producto.get('precioVenta', 0)  # Cambiado de precio a precioVenta
                        
                        # Generar un código único para el producto basado en su nombre
                        codigo_producto = nombre_producto.replace(' ', '_').upper()

                        # Insertar en productos
                        cursor.execute("""
                            INSERT IGNORE INTO productos (nombre, codigo)
                            VALUES (%s, %s)
                        """, (nombre_producto, codigo_producto))

                        # Obtener el ID del producto
                        cursor.execute("SELECT id FROM productos WHERE codigo = %s", 
                                     (codigo_producto,))
                        result = cursor.fetchone()
                        if not result:
                            print(f"Error: No se pudo obtener el ID del producto {nombre_producto}")
                            continue
                        producto_id = result[0]

                        # Verificar si ya existe un precio para hoy
                        cursor.execute("""
                            SELECT id FROM precios 
                            WHERE establecimiento_id = %s 
                            AND producto_id = %s 
                            AND DATE(fecha_actualizacion) = CURDATE()
                        """, (establecimiento_id, producto_id))
                        
                        if cursor.fetchone() is None:
                            # Solo insertar si no existe un precio para hoy
                            cursor.execute("""
                                INSERT INTO precios 
                                (establecimiento_id, producto_id, precio, fecha_actualizacion)
                                VALUES (%s, %s, %s, NOW())
                            """, (establecimiento_id, producto_id, precio))
                        else:
                            # Actualizar el precio existente
                            cursor.execute("""
                                UPDATE precios 
                                SET precio = %s, fecha_actualizacion = NOW()
                                WHERE establecimiento_id = %s 
                                AND producto_id = %s 
                                AND DATE(fecha_actualizacion) = CURDATE()
                            """, (precio, establecimiento_id, producto_id))

                records_processed += 1
                if records_processed % 10 == 0:  # Commit cada 10 registros
                    connection.commit()
                    print(f"Commit realizado después de {records_processed} registros")

            except Error as item_error:
                print(f"Error procesando registro: {item_error}")
                continue

        connection.commit()
        return True
    except Error as e:
        print(f"Error en el lote: {e}")
        connection.rollback()
        return False
    finally:
        cursor.close()

def insert_data():
    try:
        # Configuración de la conexión con timeout
        connection = mysql.connector.connect(
            host='bh7114.banahosting.com',
            port=3306,
            database='fcqngeyc_dataPricingApp',
            user='fcqngeyc_adminApp',
            password='emkappprecios12',
            connect_timeout=60,  # 60 segundos de timeout para la conexión
            connection_timeout=60  # 60 segundos de timeout para comandos
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos")

            # Leer el archivo JSON
            print("Leyendo archivo JSON...")
            with open('json_departamentos/todos_los_departamentos.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            print(f"Se encontraron {len(data)} registros para procesar")

            # Procesar en lotes más pequeños
            batch_size = 10  # Reducido de 50 a 10
            total_batches = (len(data) + batch_size - 1) // batch_size
            successful_batches = 0

            for i in range(0, len(data), batch_size):
                batch = data[i:i + batch_size]
                batch_number = (i // batch_size) + 1
                print(f"\nProcesando lote {batch_number} de {total_batches} ({len(batch)} registros)")
                
                if process_batch(connection, batch):
                    successful_batches += 1
                    print(f"Lote {batch_number} procesado exitosamente")
                else:
                    print(f"Error en el lote {batch_number}, continuando con el siguiente...")

            print(f"\nProceso completado. {successful_batches} de {total_batches} lotes procesados exitosamente")

    except Error as e:
        print(f"Error de conexión: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insert_data() 