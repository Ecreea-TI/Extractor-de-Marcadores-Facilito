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
    print("Iniciando conexión a la base de datos...")
    # Conexión a la base de datos
    conn = mysql.connector.connect(
        host='bh7114.banahosting.com',
        port=3306,
        database='fcqngeyc_dataPricingApp',
        user='fcqngeyc_adminApp',
        password='emkappprecios12',
        connect_timeout=60
    )
    print("Conexión exitosa a la base de datos")

    cursor = conn.cursor()

    # Crear tablas si no existen
    print("Creando tablas si no existen...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departamentos (
        id VARCHAR(2) PRIMARY KEY,
        nombre VARCHAR(100),
        latitud DECIMAL(10,6),
        longitud DECIMAL(10,6)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS provincias (
        id VARCHAR(4) PRIMARY KEY,
        departamento_id VARCHAR(2),
        nombre VARCHAR(100),
        latitud DECIMAL(10,6),
        longitud DECIMAL(10,6),
        FOREIGN KEY (departamento_id) REFERENCES departamentos(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS distritos (
        id VARCHAR(6) PRIMARY KEY,
        provincia_id VARCHAR(4),
        nombre VARCHAR(100),
        latitud DECIMAL(10,6),
        longitud DECIMAL(10,6),
        FOREIGN KEY (provincia_id) REFERENCES provincias(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS estaciones (
        codigo_osinergmin VARCHAR(10) PRIMARY KEY,
        distrito_id VARCHAR(6),
        nombre VARCHAR(200),
        direccion TEXT,
        latitud DECIMAL(10,6),
        longitud DECIMAL(10,6),
        FOREIGN KEY (distrito_id) REFERENCES distritos(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS precios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        estacion_id VARCHAR(10),
        producto_id INT,
        precio DECIMAL(10,2),
        fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (estacion_id) REFERENCES estaciones(codigo_osinergmin),
        FOREIGN KEY (producto_id) REFERENCES productos(id)
    )
    """)
    print("Tablas creadas correctamente")

    # Cargar datos de ubigeo para La Libertad
    print("Cargando archivo ubigeo_peru.json...")
    with open('ubigeo_peru.json') as f:
        ubigeo_data = json.load(f)

    print("Procesando datos de La Libertad...")
    # Insertar datos de La Libertad (código 13)
    departamento_encontrado = False
    for departamento in ubigeo_data['departamentos']:
        if departamento['id'] == '13':  # La Libertad
            departamento_encontrado = True
            print(f"Encontrado departamento La Libertad con ID {departamento['id']}")
            try:
                cursor.execute("""
                    INSERT IGNORE INTO departamentos (id, nombre, latitud, longitud)
                    VALUES (%s, %s, %s, %s)
                """, (
                    departamento['id'],
                    departamento['nombre'],
                    departamento['coordenadas']['latitud'],
                    departamento['coordenadas']['longitud']
                ))
                print(f"Departamento insertado: {departamento['nombre']}")
                
                for provincia in departamento['provincias']:
                    print(f"Procesando provincia: {provincia['nombre']}")
                    cursor.execute("""
                        INSERT IGNORE INTO provincias (id, departamento_id, nombre, latitud, longitud)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (
                        provincia['id'],
                        departamento['id'],
                        provincia['nombre'],
                        provincia['coordenadas']['latitud'],
                        provincia['coordenadas']['longitud']
                    ))
                    
                    for distrito in provincia['distritos']:
                        print(f"Procesando distrito: {distrito['nombre']}")
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
                
                conn.commit()
                print("Datos de ubicación insertados correctamente")
            except Exception as e:
                print(f"Error al insertar datos de ubicación: {str(e)}")
                conn.rollback()
                raise

    if not departamento_encontrado:
        print("¡ADVERTENCIA! No se encontró el departamento de La Libertad en el archivo")
        raise Exception("Departamento de La Libertad no encontrado")

    # Cargar datos de estaciones de La Libertad
    print("Cargando archivo de estaciones de La Libertad...")
    with open('json_departamentos/la_libertad.json') as f:
        estaciones_data = json.load(f)

    # Procesar cada estación
    print(f"Procesando {len(estaciones_data)} estaciones...")
    for estacion in estaciones_data:
        try:
            # Verificar si la estación ya existe
            cursor.execute("""
                SELECT codigo_osinergmin, distrito_id FROM estaciones 
                WHERE codigo_osinergmin = %s
            """, (estacion['codigoOsinergmin'],))
            
            estacion_existe = cursor.fetchone()
            
            if not estacion_existe:
                print(f"\nProcesando nueva estación: {estacion['unidad']}")
                print(f"Coordenadas de la estación: {estacion['latitud']}, {estacion['longitud']}")
                
                # Obtener todos los distritos de La Libertad
                cursor.execute("""
                    SELECT id, nombre, latitud, longitud 
                    FROM distritos 
                    WHERE provincia_id LIKE '13%'
                """)
                distritos = cursor.fetchall()
                
                if not distritos:
                    print("¡ADVERTENCIA! No se encontraron distritos para La Libertad")
                    continue
                
                print(f"Se encontraron {len(distritos)} distritos")
                
                distrito_mas_cercano = None
                distancia_minima = float('inf')
                nombre_distrito = None
                
                for distrito in distritos:
                    distancia = calcular_distancia(
                        estacion['latitud'],
                        estacion['longitud'],
                        float(distrito[2]),  # latitud
                        float(distrito[3])   # longitud
                    )
                    if distancia < distancia_minima:
                        distancia_minima = distancia
                        distrito_mas_cercano = distrito[0]
                        nombre_distrito = distrito[1]
                
                if distrito_mas_cercano:
                    print(f"Distrito más cercano encontrado: {nombre_distrito} (ID: {distrito_mas_cercano})")
                    print(f"Distancia: {distancia_minima:.2f} km")
                    
                    # Insertar estación
                    cursor.execute("""
                        INSERT INTO estaciones (codigo_osinergmin, distrito_id, nombre, direccion, latitud, longitud)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """, (
                        estacion['codigoOsinergmin'],
                        distrito_mas_cercano,
                        estacion['unidad'],
                        estacion['direccion'],
                        estacion['latitud'],
                        estacion['longitud']
                    ))
                    print(f"Nueva estación insertada: {estacion['unidad']} en distrito {nombre_distrito}")
                else:
                    print(f"¡ADVERTENCIA! No se pudo encontrar distrito para la estación {estacion['unidad']}")
                    continue
            
            # Insertar productos y precios
            for producto in estacion['productos']:
                # Verificar si el producto existe
                cursor.execute("SELECT id FROM productos WHERE nombre = %s", (producto['producto'],))
                producto_id = cursor.fetchone()
                
                if not producto_id:
                    cursor.execute("INSERT INTO productos (nombre) VALUES (%s)", (producto['producto'],))
                    producto_id = cursor.lastrowid
                else:
                    producto_id = producto_id[0]
                
                # Insertar o actualizar precio
                cursor.execute("""
                    INSERT INTO precios (estacion_id, producto_id, precio)
                    VALUES (%s, %s, %s)
                    ON DUPLICATE KEY UPDATE
                    precio = VALUES(precio),
                    fecha_actualizacion = CURRENT_TIMESTAMP
                """, (estacion['codigoOsinergmin'], producto_id, producto['precioVenta']))
                
            print(f"Precios actualizados para estación {estacion['unidad']}")
            conn.commit()
            
        except Exception as e:
            print(f"Error al procesar estación {estacion['unidad']}: {str(e)}")
            conn.rollback()
            continue

except Exception as e:
    print(f"Error general: {str(e)}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("Conexión cerrada") 