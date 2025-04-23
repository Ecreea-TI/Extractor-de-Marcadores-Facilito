import mysql.connector
from mysql.connector import Error

def test_single_insert():
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

            # Datos de prueba
            test_data = {
                'departamento': 'LIMA',
                'codigo_departamento': '15',
                'provincia': 'LIMA',
                'codigo_provincia': '1501',
                'distrito': 'LIMA',
                'codigo_distrito': '150101',
                'nombre_establecimiento': 'ESTACION DE SERVICIO TEST',
                'direccion': 'AV. TEST 123',
                'latitud': -12.0432,
                'longitud': -77.0282,
                'codigo_osinergmin': 'TEST123',
                'productos': [
                    {
                        'nombre': 'GASOLINA 95',
                        'codigo': 'G95',
                        'precio': 18.50
                    },
                    {
                        'nombre': 'GASOLINA 97',
                        'codigo': 'G97',
                        'precio': 19.50
                    }
                ]
            }

            print("\nIniciando inserción de prueba...")
            
            # Insertar en departamentos
            print(f"Insertando departamento: {test_data['departamento']}")
            cursor.execute("""
                INSERT IGNORE INTO departamentos (nombre, codigo_ubigeo)
                VALUES (%s, %s)
            """, (test_data['departamento'], test_data['codigo_departamento']))

            # Obtener el ID del departamento
            cursor.execute("SELECT id FROM departamentos WHERE codigo_ubigeo = %s", 
                         (test_data['codigo_departamento'],))
            departamento_id = cursor.fetchone()[0]
            print(f"ID de departamento: {departamento_id}")

            # Insertar en provincias
            print(f"Insertando provincia: {test_data['provincia']}")
            cursor.execute("""
                INSERT IGNORE INTO provincias (departamento_id, nombre, codigo_ubigeo)
                VALUES (%s, %s, %s)
            """, (departamento_id, test_data['provincia'], test_data['codigo_provincia']))

            # Obtener el ID de la provincia
            cursor.execute("SELECT id FROM provincias WHERE codigo_ubigeo = %s", 
                         (test_data['codigo_provincia'],))
            provincia_id = cursor.fetchone()[0]
            print(f"ID de provincia: {provincia_id}")

            # Insertar en distritos
            print(f"Insertando distrito: {test_data['distrito']}")
            cursor.execute("""
                INSERT IGNORE INTO distritos (provincia_id, nombre, codigo_ubigeo)
                VALUES (%s, %s, %s)
            """, (provincia_id, test_data['distrito'], test_data['codigo_distrito']))

            # Obtener el ID del distrito
            cursor.execute("SELECT id FROM distritos WHERE codigo_ubigeo = %s", 
                         (test_data['codigo_distrito'],))
            distrito_id = cursor.fetchone()[0]
            print(f"ID de distrito: {distrito_id}")

            # Insertar en establecimientos
            print(f"Insertando establecimiento: {test_data['nombre_establecimiento']}")
            cursor.execute("""
                INSERT IGNORE INTO establecimientos 
                (distrito_id, nombre, direccion, latitud, longitud, codigo_osinergmin)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (distrito_id, 
                  test_data['nombre_establecimiento'],
                  test_data['direccion'],
                  test_data['latitud'],
                  test_data['longitud'],
                  test_data['codigo_osinergmin']))

            # Obtener el ID del establecimiento
            cursor.execute("SELECT id FROM establecimientos WHERE codigo_osinergmin = %s", 
                         (test_data['codigo_osinergmin'],))
            establecimiento_id = cursor.fetchone()[0]
            print(f"ID de establecimiento: {establecimiento_id}")

            # Insertar productos y precios
            for producto in test_data['productos']:
                print(f"Insertando producto: {producto['nombre']}")
                cursor.execute("""
                    INSERT IGNORE INTO productos (nombre, codigo)
                    VALUES (%s, %s)
                """, (producto['nombre'], producto['codigo']))

                # Obtener el ID del producto
                cursor.execute("SELECT id FROM productos WHERE codigo = %s", 
                             (producto['codigo'],))
                producto_id = cursor.fetchone()[0]
                print(f"ID de producto: {producto_id}")

                # Insertar precio
                print(f"Insertando precio: {producto['precio']}")
                cursor.execute("""
                    INSERT INTO precios 
                    (establecimiento_id, producto_id, precio, fecha_actualizacion)
                    VALUES (%s, %s, %s, NOW())
                """, (establecimiento_id, producto_id, producto['precio']))

            # Confirmar los cambios
            connection.commit()
            print("\nInserción de prueba completada exitosamente")

    except Error as e:
        print(f"Error durante la inserción: {e}")
        if 'connection' in locals() and connection.is_connected():
            connection.rollback()
            print("Se realizó rollback de la transacción")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    test_single_insert() 