let map;
let markers = [];
let infoWindow;
let activeMarker = null;
let markerColors = {};

// Coordenadas centrales para cada departamento
const departamentoCoordenadas = {
    'LIMA': { lat: -12.0464, lng: -77.0428, zoom: 12 },
    'LA LIBERTAD': { lat: -8.1161, lng: -79.0333, zoom: 14 }
};

// Colores para las provincias
const colors = [
    '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', 
    '#00FFFF', '#FFA500', '#800080', '#008000', '#FFC0CB',
    '#A52A2A', '#808080', '#FFD700'
];

function getColorForProvince(provincia) {
    if (!markerColors[provincia]) {
        markerColors[provincia] = colors[Object.keys(markerColors).length % colors.length];
    }
    return markerColors[provincia];
}

function createCustomMarker(color) {
    return {
        url: 'point-marker.svg',
        scaledSize: new google.maps.Size(30, 30),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(15, 15)
    };
}

const activeIcon = {
    url: 'active-marker-icon.svg',
    scaledSize: new google.maps.Size(35, 35),
    origin: new google.maps.Point(0, 0),
    anchor: new google.maps.Point(17.5, 17.5)
};

function initMap() {
    const defaultLocation = departamentoCoordenadas['LIMA'];
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: defaultLocation.zoom,
        center: { lat: defaultLocation.lat, lng: defaultLocation.lng },
        styles: [
            {
                featureType: "poi",
                elementType: "labels",
                stylers: [{ visibility: "off" }]
            }
        ]
    });

    infoWindow = new google.maps.InfoWindow();
    
    const regionSelect = document.getElementById('region');
    cargarEstaciones(regionSelect.value);

    regionSelect.addEventListener('change', function() {
        const departamento = this.value;
        console.log('Cambiando a departamento:', departamento);
        const coords = departamentoCoordenadas[departamento];
        if (coords) {
            map.setCenter({ lat: coords.lat, lng: coords.lng });
            map.setZoom(coords.zoom);
        }
        markerColors = {}; // Resetear colores al cambiar de departamento
        cargarEstaciones(departamento);
    });

    document.getElementById('provincia').addEventListener('change', function() {
        actualizarDistritos();
        const provinciaSeleccionada = this.value;
        if (provinciaSeleccionada !== 'todos') {
            const bounds = new google.maps.LatLngBounds();
            let markersInProvince = false;
            
            markers.forEach(marker => {
                if (marker.estacion.provincia === provinciaSeleccionada) {
                    bounds.extend(marker.getPosition());
                    markersInProvince = true;
                }
            });
            
            if (markersInProvince) {
                map.fitBounds(bounds);
                // Ajustar el zoom si está muy cercano
                google.maps.event.addListenerOnce(map, 'bounds_changed', function() {
                    if (map.getZoom() > 15) map.setZoom(15);
                });
            }
        }
        filtrarMarcadores();
    });

    document.getElementById('distrito').addEventListener('change', function() {
        const distritoSeleccionado = this.value;
        if (distritoSeleccionado !== 'todos') {
            const bounds = new google.maps.LatLngBounds();
            let markersInDistrict = false;
            
            markers.forEach(marker => {
                if (marker.estacion.distrito === distritoSeleccionado) {
                    bounds.extend(marker.getPosition());
                    markersInDistrict = true;
                }
            });
            
            if (markersInDistrict) {
                map.fitBounds(bounds);
                // Ajustar el zoom si está muy cercano
                google.maps.event.addListenerOnce(map, 'bounds_changed', function() {
                    if (map.getZoom() > 16) map.setZoom(16);
                });
            }
        }
        filtrarMarcadores();
    });

    document.getElementById('producto').addEventListener('change', filtrarMarcadores);
}

function cargarEstaciones(departamento) {
    console.log('Cargando estaciones para:', departamento);
    
    // Convertir nombre de departamento a ID
    const departamentoIds = {
        'LIMA': '15',
        'LA LIBERTAD': '13'
    };
    
    const departamentoId = departamentoIds[departamento];
    if (!departamentoId) {
        console.error('ID de departamento no encontrado para:', departamento);
        return;
    }

    console.log('Realizando petición para departamento ID:', departamentoId);
    
    // Limpiar marcadores existentes antes de la nueva carga
    limpiarMarcadores();

    fetch(`/get_estaciones?departamento=${departamentoId}`)
        .then(response => {
            console.log('Respuesta recibida:', response.status);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Datos recibidos:', data);
            if (data.success) {
                if (data.data.length === 0) {
                    console.log('No se encontraron estaciones para este departamento');
                    return;
                }
                
                // Obtener productos únicos para el filtro
                const productosUnicos = new Set();
                
                // Crear marcadores para cada estación
                data.data.forEach(estacion => {
                    console.log('Creando marcador para estación:', estacion.nombre);
                    // Agregar productos al set de productos únicos
                    estacion.productos.forEach(producto => {
                        productosUnicos.add(producto.nombre);
                    });
                    
                    crearMarcador(estacion);
                });
                
                // Actualizar el select de productos
                actualizarProductos(Array.from(productosUnicos));
                
                // Actualizar los selects de provincia y distrito
                actualizarFiltrosUbicacion(data);
                
                console.log('Total de marcadores creados:', markers.length);
            } else {
                console.error('Error en la respuesta:', data.error);
            }
        })
        .catch(error => {
            console.error('Error al cargar las estaciones:', error);
        });
}

function crearMarcador(estacion) {
    const color = getColorForProvince(estacion.provincia);
    const marker = new google.maps.Marker({
        position: { lat: estacion.latitud, lng: estacion.longitud },
        map: map,
        title: estacion.nombre,
        icon: createCustomMarker(color)
    });

    marker.estacion = estacion;
    marker.defaultIcon = createCustomMarker(color);

    marker.addListener('click', () => {
        if (activeMarker && activeMarker !== marker) {
            activeMarker.setIcon(activeMarker.defaultIcon);
        }
        
        activeMarker = marker;
        marker.setIcon(activeIcon);

        const productosHTML = estacion.productos
            .map(p => `<tr><td>${p.nombre}</td><td>S/ ${p.precio.toFixed(2)}</td></tr>`)
            .join('');

        const content = `
            <div class="info-window">
                <h3>${estacion.nombre}</h3>
                <p><strong>Dirección:</strong> ${estacion.direccion}</p>
                <p><strong>Distrito:</strong> ${estacion.distrito}</p>
                <p><strong>Provincia:</strong> ${estacion.provincia}</p>
                <table>
                    <thead>
                        <tr>
                            <th>Producto</th>
                            <th>Precio</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${productosHTML}
                    </tbody>
                </table>
            </div>
        `;

        infoWindow.setContent(content);
        infoWindow.open(map, marker);
    });

    google.maps.event.addListener(infoWindow, 'closeclick', () => {
        if (activeMarker) {
            activeMarker.setIcon(activeMarker.defaultIcon);
            activeMarker = null;
        }
    });

    markers.push(marker);
}

function limpiarMarcadores() {
    markers.forEach(marker => marker.setMap(null));
    markers = [];
    markerColors = {};
}

function actualizarProductos(productos) {
    const select = document.getElementById('producto');
    select.innerHTML = '<option value="todos">Todos los productos</option>';
    productos.forEach(producto => {
        const option = document.createElement('option');
        option.value = producto;
        option.textContent = producto;
        select.appendChild(option);
    });
}

function actualizarFiltrosUbicacion(data) {
    const selectProvincia = document.getElementById('provincia');
    selectProvincia.innerHTML = '<option value="todos">Todas las provincias</option>';
    
    // Ordenar provincias por nombre
    const provincias = data.provincias.sort((a, b) => a.nombre.localeCompare(b.nombre));
    
    // Crear Map de distritos
    const distritos = new Map();
    data.data.forEach(estacion => {
        if (!distritos.has(estacion.provincia)) {
            distritos.set(estacion.provincia, new Set());
        }
        if (estacion.distrito) {
            distritos.get(estacion.provincia).add(estacion.distrito);
        }
    });

    // Agregar todas las provincias al selector
    provincias.forEach(provincia => {
        const option = document.createElement('option');
        option.value = provincia.nombre;
        option.textContent = `${provincia.nombre} (${provincia.num_estaciones} estaciones)`;
        selectProvincia.appendChild(option);
    });

    // Guardar los distritos en una variable global para usarlos en actualizarDistritos
    window.distritosData = distritos;
}

function actualizarDistritos() {
    const provinciaSeleccionada = document.getElementById('provincia').value;
    const selectDistrito = document.getElementById('distrito');
    
    selectDistrito.innerHTML = '<option value="todos">Todos los distritos</option>';
    
    if (provinciaSeleccionada !== 'todos' && window.distritosData) {
        const distritosDeProvinciaSeleccionada = window.distritosData.get(provinciaSeleccionada);
        if (distritosDeProvinciaSeleccionada) {
            Array.from(distritosDeProvinciaSeleccionada)
                .sort((a, b) => a.localeCompare(b))
                .forEach(distrito => {
                    const option = document.createElement('option');
                    option.value = distrito;
                    option.textContent = distrito;
                    selectDistrito.appendChild(option);
                });
        }
    }
    
    filtrarMarcadores();
}

function filtrarMarcadores() {
    const provinciaSeleccionada = document.getElementById('provincia').value;
    const distritoSeleccionado = document.getElementById('distrito').value;
    const productoSeleccionado = document.getElementById('producto').value;

    markers.forEach(marker => {
        const estacion = marker.estacion;
        let visible = true;

        // Filtrar por provincia
        if (provinciaSeleccionada !== 'todos' && estacion.provincia !== provinciaSeleccionada) {
            visible = false;
        }

        // Filtrar por distrito
        if (visible && distritoSeleccionado !== 'todos' && estacion.distrito !== distritoSeleccionado) {
            visible = false;
        }

        // Filtrar por producto
        if (visible && productoSeleccionado !== 'todos') {
            const tieneProducto = estacion.productos.some(p => p.nombre === productoSeleccionado);
            if (!tieneProducto) {
                visible = false;
            }
        }

        marker.setVisible(visible);
    });
}

// Inicializar el mapa cuando se cargue la API de Google Maps
google.maps.event.addDomListener(window, 'load', initMap); 