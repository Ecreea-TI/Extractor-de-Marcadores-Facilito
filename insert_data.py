import mysql.connector
import json
import os
from mysql.connector import Error
from datetime import datetime

def insert_data():
    try:
        # Configuración de la conexión
        connection = mysql.connector.connect(
            host='bh7114.banahosting.com',
            port=3306,
            database='fcqngeyc_dataPricingApp',
            user='fcqngeyc_adminApp',
            password='emkappprecios12'
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            cursor = connection.cursor()

            # Leer el archivo JSON de todos los departamentos
            print("Leyendo archivo JSON...")
            with open('json_departamentos/todos_los_departamentos.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
            print(f"Se encontraron {len(data)} registros para procesar")

            # Insertar datos en las tablas
            for index, item in enumerate(data, 1):
                try:
                    print(f"\nProcesando registro {index} de {len(data)}")
                    
                    # Insertar en departamentos
                    print(f"Insertando departamento: {item.get('departamento', '')}")
                    cursor.execute("""
                        INSERT IGNORE INTO departamentos (nombre, codigo_ubigeo)
                        VALUES (%s, %s)
                    """, (item.get('departamento', ''), item.get('codigo_departamento', '')))

                    # Obtener el ID del departamento
                    cursor.execute("SELECT id FROM departamentos WHERE codigo_ubigeo = %s", 
                                 (item.get('codigo_departamento', ''),))
                    departamento_id = cursor.fetchone()[0]
                    print(f"ID de departamento: {departamento_id}")

                    # Insertar en provincias
                    print(f"Insertando provincia: {item.get('provincia', '')}")
                    cursor.execute("""
                        INSERT IGNORE INTO provincias (departamento_id, nombre, codigo_ubigeo)
                        VALUES (%s, %s, %s)
                    """, (departamento_id, item.get('provincia', ''), item.get('codigo_provincia', '')))

                    # Obtener el ID de la provincia
                    cursor.execute("SELECT id FROM provincias WHERE codigo_ubigeo = %s", 
                                 (item.get('codigo_provincia', ''),))
                    provincia_id = cursor.fetchone()[0]
                    print(f"ID de provincia: {provincia_id}")

                    # Insertar en distritos
                    print(f"Insertando distrito: {item.get('distrito', '')}")
                    cursor.execute("""
                        INSERT IGNORE INTO distritos (provincia_id, nombre, codigo_ubigeo)
                        VALUES (%s, %s, %s)
                    """, (provincia_id, item.get('distrito', ''), item.get('codigo_distrito', '')))

                    # Obtener el ID del distrito
                    cursor.execute("SELECT id FROM distritos WHERE codigo_ubigeo = %s", 
                                 (item.get('codigo_distrito', ''),))
                    distrito_id = cursor.fetchone()[0]
                    print(f"ID de distrito: {distrito_id}")

                    # Insertar en establecimientos
                    print(f"Insertando establecimiento: {item.get('nombre_establecimiento', '')}")
                    cursor.execute("""
                        INSERT IGNORE INTO establecimientos 
                        (distrito_id, nombre, direccion, latitud, longitud, codigo_osinergmin)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (distrito_id, 
                          item.get('nombre_establecimiento', ''),
                          item.get('direccion', ''),
                          item.get('latitud', 0),
                          item.get('longitud', 0),
                          item.get('codigo_osinergmin', '')))

                    # Obtener el ID del establecimiento
                    cursor.execute("SELECT id FROM establecimientos WHERE codigo_osinergmin = %s", 
                                 (item.get('codigo_osinergmin', ''),))
                    establecimiento_id = cursor.fetchone()[0]
                    print(f"ID de establecimiento: {establecimiento_id}")

                    # Insertar productos y precios
                    if 'productos' in item:
                        print(f"Procesando {len(item['productos'])} productos")
                        for producto in item['productos']:
                            # Insertar en productos
                            print(f"Insertando producto: {producto.get('nombre', '')}")
                            cursor.execute("""
                                INSERT IGNORE INTO productos (nombre, codigo)
                                VALUES (%s, %s)
                            """, (producto.get('nombre', ''), producto.get('codigo', '')))

                            # Obtener el ID del producto
                            cursor.execute("SELECT id FROM productos WHERE codigo = %s", 
                                         (producto.get('codigo', ''),))
                            producto_id = cursor.fetchone()[0]
                            print(f"ID de producto: {producto_id}")

                            # Verificar si ya existe un precio para este establecimiento y producto
                            cursor.execute("""
                                SELECT id FROM precios 
                                WHERE establecimiento_id = %s 
                                AND producto_id = %s 
                                AND DATE(fecha_actualizacion) = CURDATE()
                            """, (establecimiento_id, producto_id))
                            
                            if cursor.fetchone() is None:
                                # Solo insertar si no existe un precio para hoy
                                print(f"Insertando precio: {producto.get('precio', 0)}")
                                cursor.execute("""
                                    INSERT INTO precios 
                                    (establecimiento_id, producto_id, precio, fecha_actualizacion)
                                    VALUES (%s, %s, %s, NOW())
                                """, (establecimiento_id, 
                                      producto_id,
                                      producto.get('precio', 0)))
                            else:
                                print("Precio ya existe para hoy, omitiendo...")

                except Error as e:
                    print(f"Error al insertar datos: {e}")
                    continue

            # Confirmar los cambios
            connection.commit()
            print("\nDatos insertados exitosamente")

    except Error as e:
        print(f"Error de conexión: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    insert_data() 