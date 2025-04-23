<?php
// Configuración de la base de datos
$host = 'bh7114.banahosting.com';
$port = 3306;
$dbname = 'fcqngeyc_dataPricingApp';
$username = 'fcqngeyc_adminApp';
$password = 'emkappprecios12';

try {
    // Crear conexión
    $conn = new PDO("mysql:host=$host;port=$port;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Conexión exitosa a la base de datos\n";

    // Leer el archivo SQL
    $sql = file_get_contents('database_structure.sql');
    
    // Ejecutar las consultas
    $conn->exec($sql);
    echo "Estructura de la base de datos creada exitosamente\n";

} catch(PDOException $e) {
    echo "Error: " . $e->getMessage() . "\n";
}

// Cerrar conexión
$conn = null;
?> 