<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

$host = 'bh7114.banahosting.com';
$dbname = 'fcqngeyc_dataPricingApp';
$username = 'fcqngeyc_adminApp';
$password = 'emkappprecios12';

try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Obtener el departamento de la URL, por defecto LA LIBERTAD
    $departamento_id = isset($_GET['departamento']) ? $_GET['departamento'] : '13';

    // Primero, verificar si el departamento existe
    $queryDepartamento = "SELECT nombre FROM departamentos WHERE id = ?";
    $stmtDep = $pdo->prepare($queryDepartamento);
    $stmtDep->execute([$departamento_id]);
    $departamento = $stmtDep->fetch(PDO::FETCH_ASSOC);

    if (!$departamento) {
        throw new Exception("Departamento no encontrado");
    }

    $query = "
        SELECT 
            e.codigo_osinergmin,
            e.nombre as nombre_estacion,
            e.direccion,
            e.latitud,
            e.longitud,
            d.nombre as distrito,
            p.nombre as provincia,
            GROUP_CONCAT(
                CONCAT(
                    pr.nombre, ':', 
                    pre.precio
                ) SEPARATOR '|'
            ) as productos_precios
        FROM estaciones e
        JOIN distritos d ON e.distrito_id = d.id
        JOIN provincias p ON d.provincia_id = p.id
        LEFT JOIN precios pre ON e.codigo_osinergmin = pre.estacion_id
        LEFT JOIN productos pr ON pre.producto_id = pr.id
        WHERE p.departamento_id = :departamento_id
        GROUP BY e.codigo_osinergmin
    ";

    $stmt = $pdo->prepare($query);
    $stmt->execute(['departamento_id' => $departamento_id]);
    $estaciones = $stmt->fetchAll(PDO::FETCH_ASSOC);

    $resultado = array_map(function($estacion) {
        $productos = [];
        if ($estacion['productos_precios']) {
            foreach(explode('|', $estacion['productos_precios']) as $producto) {
                list($nombre, $precio) = explode(':', $producto);
                $productos[] = [
                    'nombre' => $nombre,
                    'precio' => floatval($precio)
                ];
            }
        }

        return [
            'codigo' => $estacion['codigo_osinergmin'],
            'nombre' => $estacion['nombre_estacion'],
            'direccion' => $estacion['direccion'],
            'distrito' => $estacion['distrito'],
            'provincia' => $estacion['provincia'],
            'latitud' => floatval($estacion['latitud']),
            'longitud' => floatval($estacion['longitud']),
            'productos' => $productos
        ];
    }, $estaciones);

    echo json_encode([
        'success' => true, 
        'data' => $resultado,
        'departamento' => $departamento['nombre']
    ]);

} catch(Exception $e) {
    echo json_encode(['success' => false, 'error' => $e->getMessage()]);
}
?> 