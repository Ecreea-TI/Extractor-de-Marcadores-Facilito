from http.server import HTTPServer, BaseHTTPRequestHandler
import mysql.connector
import json
from urllib.parse import parse_qs, urlparse
import os
import mimetypes

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        # Si la ruta es /get_estaciones, manejar como API
        if parsed_path.path == '/get_estaciones':
            self.handle_api_request()
        else:
            self.handle_static_files()

    def handle_static_files(self):
        # Manejar la ruta raíz
        if self.path == '/':
            self.path = '/index.html'

        try:
            # Eliminar el / inicial para obtener la ruta relativa
            file_path = self.path[1:]
            
            # Verificar si el archivo existe
            if os.path.exists(file_path):
                # Determinar el tipo de contenido
                content_type, _ = mimetypes.guess_type(file_path)
                if content_type is None:
                    content_type = 'application/octet-stream'

                self.send_response(200)
                self.send_header('Content-type', content_type)
                self.end_headers()

                # Leer y enviar el archivo
                with open(file_path, 'rb') as f:
                    self.wfile.write(f.read())
            else:
                self.send_error(404, 'File Not Found')
        except Exception as e:
            self.send_error(500, str(e))

    def handle_api_request(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        try:
            # Parsear el query string para obtener el departamento
            query_components = parse_qs(urlparse(self.path).query)
            departamento_id = query_components.get('departamento', ['13'])[0]  # Default a La Libertad

            # Conexión a la base de datos
            conn = mysql.connector.connect(
                host='bh7114.banahosting.com',
                database='fcqngeyc_dataPricingApp',
                user='fcqngeyc_adminApp',
                password='emkappprecios12'
            )
            cursor = conn.cursor(dictionary=True)

            # Verificar si el departamento existe
            cursor.execute("SELECT nombre FROM departamentos WHERE id = %s", (departamento_id,))
            departamento = cursor.fetchone()

            if not departamento:
                raise Exception("Departamento no encontrado")

            # Primero obtener todas las provincias del departamento
            query_provincias = """
                SELECT id, nombre
                FROM provincias
                WHERE departamento_id = %s
                ORDER BY nombre
            """
            
            cursor.execute(query_provincias, (departamento_id,))
            provincias = cursor.fetchall()

            # Consulta para obtener las estaciones
            query = """
                SELECT DISTINCT
                    e.codigo_osinergmin,
                    e.nombre as nombre_estacion,
                    e.direccion,
                    e.latitud,
                    e.longitud,
                    d.nombre as distrito,
                    p.nombre as provincia,
                    p.id as provincia_id
                FROM estaciones e
                JOIN distritos d ON e.distrito_id = d.id
                JOIN provincias p ON d.provincia_id = p.id
                WHERE p.departamento_id = %s
                    AND e.latitud IS NOT NULL 
                    AND e.longitud IS NOT NULL
                    AND e.latitud != 0 
                    AND e.longitud != 0
            """
            
            cursor.execute(query, (departamento_id,))
            estaciones_base = cursor.fetchall()
            
            # Consulta para obtener los precios
            query_precios = """
                SELECT 
                    e.codigo_osinergmin,
                    GROUP_CONCAT(
                        DISTINCT
                        CONCAT(
                            pr.nombre, ':', 
                            COALESCE(
                                (SELECT precio 
                                FROM precios p2 
                                WHERE p2.estacion_id = e.codigo_osinergmin 
                                AND p2.producto_id = pr.id 
                                ORDER BY p2.fecha_actualizacion DESC 
                                LIMIT 1),
                                pre.precio
                            )
                        ) SEPARATOR '|'
                    ) as productos_precios
                FROM estaciones e
                LEFT JOIN precios pre ON e.codigo_osinergmin = pre.estacion_id
                LEFT JOIN productos pr ON pre.producto_id = pr.id
                WHERE e.codigo_osinergmin IN (
                    SELECT DISTINCT codigo_osinergmin 
                    FROM estaciones e2 
                    JOIN distritos d2 ON e2.distrito_id = d2.id 
                    JOIN provincias p2 ON d2.provincia_id = p2.id 
                    WHERE p2.departamento_id = %s
                )
                GROUP BY e.codigo_osinergmin
            """
            
            cursor.execute(query_precios, (departamento_id,))
            precios_dict = {row['codigo_osinergmin']: row['productos_precios'] for row in cursor.fetchall()}

            # Procesar resultados
            resultado = []
            estaciones_por_provincia = {}

            # Inicializar el contador de estaciones por provincia
            for provincia in provincias:
                estaciones_por_provincia[provincia['nombre']] = 0

            for estacion in estaciones_base:
                productos = []
                productos_precios = precios_dict.get(estacion['codigo_osinergmin'])
                
                if productos_precios:
                    for producto in productos_precios.split('|'):
                        nombre, precio = producto.split(':')
                        try:
                            precio_float = float(precio)
                        except (ValueError, TypeError):
                            precio_float = 0.0
                        productos.append({
                            'nombre': nombre,
                            'precio': precio_float
                        })

                # Incrementar el contador de estaciones para esta provincia
                provincia_nombre = estacion['provincia']
                estaciones_por_provincia[provincia_nombre] = estaciones_por_provincia.get(provincia_nombre, 0) + 1

                resultado.append({
                    'codigo': estacion['codigo_osinergmin'],
                    'nombre': estacion['nombre_estacion'],
                    'direccion': estacion['direccion'] or '',
                    'distrito': estacion['distrito'] or '',
                    'provincia': provincia_nombre,
                    'latitud': float(estacion['latitud']),
                    'longitud': float(estacion['longitud']),
                    'productos': productos
                })

            response_data = {
                'success': True,
                'data': resultado,
                'departamento': departamento['nombre'],
                'provincias': [
                    {
                        'id': p['id'],
                        'nombre': p['nombre'],
                        'num_estaciones': estaciones_por_provincia.get(p['nombre'], 0)
                    }
                    for p in provincias
                ]
            }

        except Exception as e:
            print(f"Error: {str(e)}")  # Agregar log del error
            response_data = {
                'success': False,
                'error': str(e)
            }
        finally:
            if 'conn' in locals():
                conn.close()

        self.wfile.write(json.dumps(response_data).encode())

def run_server(port=8000):
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Servidor iniciado en http://localhost:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server() 