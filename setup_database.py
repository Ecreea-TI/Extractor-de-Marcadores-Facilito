import mysql.connector
from mysql.connector import Error

def setup_database():
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

        # Crear tabla de departamentos
        print("\nCreando tabla de departamentos...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS departamentos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                codigo_ubigeo VARCHAR(6) NOT NULL,
                latitud DECIMAL(10, 8),
                longitud DECIMAL(11, 8),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                UNIQUE KEY unique_codigo_ubigeo (codigo_ubigeo)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """)

        # Crear tabla de provincias
        print("Creando tabla de provincias...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS provincias (
                id INT AUTO_INCREMENT PRIMARY KEY,
                departamento_id INT NOT NULL,
                nombre VARCHAR(100) NOT NULL,
                codigo_ubigeo VARCHAR(6) NOT NULL,
                latitud DECIMAL(10, 8),
                longitud DECIMAL(11, 8),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (departamento_id) REFERENCES departamentos(id),
                UNIQUE KEY unique_codigo_ubigeo (codigo_ubigeo)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """)

        # Crear tabla de distritos
        print("Creando tabla de distritos...")
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS distritos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                provincia_id INT NOT NULL,
                nombre VARCHAR(100) NOT NULL,
                codigo_ubigeo VARCHAR(6) NOT NULL,
                latitud DECIMAL(10, 8),
                longitud DECIMAL(11, 8),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                FOREIGN KEY (provincia_id) REFERENCES provincias(id),
                UNIQUE KEY unique_codigo_ubigeo (codigo_ubigeo)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """)

        # Commit los cambios
        connection.commit()
        print("\n¡Tablas creadas exitosamente!")

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
    setup_database() 