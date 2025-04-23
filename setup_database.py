import mysql.connector
from mysql.connector import Error

def setup_database():
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

            # Crear cursor
            cursor = connection.cursor()

            # Leer el archivo SQL
            with open('database_structure.sql', 'r', encoding='utf-8') as file:
                sql_script = file.read()

            # Ejecutar cada consulta del script
            for statement in sql_script.split(';'):
                if statement.strip():
                    try:
                        cursor.execute(statement)
                        print(f"Consulta ejecutada: {statement[:50]}...")
                    except Error as e:
                        print(f"Error en la consulta: {e}")
                        continue

            # Confirmar los cambios
            connection.commit()
            print("Estructura de la base de datos creada exitosamente")

    except Error as e:
        print(f"Error de conexión: {e}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

if __name__ == "__main__":
    setup_database() 