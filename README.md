# Extractor de Marcadores Facilito

Este script extrae datos de estaciones de servicio desde el sistema Facilito de OSINERGMIN.

## Características

- Extrae información de estaciones de servicio
- Procesa y limpia los datos
- Guarda los resultados en formato JSON
- Maneja caracteres especiales y codificación UTF-8

## Requisitos

```bash
requests
```

## Uso

1. Asegúrate de tener Python instalado
2. Instala las dependencias: `pip install requests`
3. Ejecuta el script: `python script.py`

## Estructura de datos

El script extrae la siguiente información para cada estación:

- Código OSINERGMIN
- Latitud y longitud
- Nombre de la unidad
- Dirección
- Productos y precios 