import json

# Datos de provincias y distritos por departamento
provinces_districts = {
    "06": {  # CAJAMARCA
        "provincias": [
            {
                "id": "0601",
                "nombre": "CAJAMARCA",
                "coordenadas": {"latitud": -7.1644, "longitud": -78.5106},
                "distritos": [
                    {"id": "060101", "nombre": "CAJAMARCA", "coordenadas": {"latitud": -7.1644, "longitud": -78.5106}},
                    {"id": "060102", "nombre": "ASUNCION", "coordenadas": {"latitud": -7.3167, "longitud": -78.5167}},
                    {"id": "060103", "nombre": "CHETILLA", "coordenadas": {"latitud": -7.1500, "longitud": -78.6667}},
                    {"id": "060104", "nombre": "COSPAN", "coordenadas": {"latitud": -7.4333, "longitud": -78.5500}},
                    {"id": "060105", "nombre": "ENCAÑADA", "coordenadas": {"latitud": -7.0833, "longitud": -78.3500}},
                    {"id": "060106", "nombre": "JESUS", "coordenadas": {"latitud": -7.2500, "longitud": -78.3833}},
                    {"id": "060107", "nombre": "LLACANORA", "coordenadas": {"latitud": -7.1833, "longitud": -78.4333}},
                    {"id": "060108", "nombre": "LOS BAÑOS DEL INCA", "coordenadas": {"latitud": -7.1667, "longitud": -78.4667}},
                    {"id": "060109", "nombre": "MAGDALENA", "coordenadas": {"latitud": -7.2500, "longitud": -78.6500}},
                    {"id": "060110", "nombre": "MATARA", "coordenadas": {"latitud": -7.2567, "longitud": -78.2633}},
                    {"id": "060111", "nombre": "NAMORA", "coordenadas": {"latitud": -7.2000, "longitud": -78.3333}},
                    {"id": "060112", "nombre": "SAN JUAN", "coordenadas": {"latitud": -7.2833, "longitud": -78.5000}}
                ]
            },
            {
                "id": "0602",
                "nombre": "CAJABAMBA",
                "coordenadas": {"latitud": -7.6219, "longitud": -78.0458},
                "distritos": [
                    {"id": "060201", "nombre": "CAJABAMBA", "coordenadas": {"latitud": -7.6219, "longitud": -78.0458}},
                    {"id": "060202", "nombre": "CACHACHI", "coordenadas": {"latitud": -7.4500, "longitud": -78.2667}},
                    {"id": "060203", "nombre": "CONDEBAMBA", "coordenadas": {"latitud": -7.5733, "longitud": -78.0694}},
                    {"id": "060204", "nombre": "SITACOCHA", "coordenadas": {"latitud": -7.5333, "longitud": -77.9667}}
                ]
            },
            {
                "id": "0603",
                "nombre": "CELENDIN",
                "coordenadas": {"latitud": -6.8667, "longitud": -78.1472},
                "distritos": [
                    {"id": "060301", "nombre": "CELENDIN", "coordenadas": {"latitud": -6.8667, "longitud": -78.1472}},
                    {"id": "060302", "nombre": "CHUMUCH", "coordenadas": {"latitud": -6.6000, "longitud": -78.2000}},
                    {"id": "060303", "nombre": "CORTEGANA", "coordenadas": {"latitud": -6.4833, "longitud": -78.3000}},
                    {"id": "060304", "nombre": "HUASMIN", "coordenadas": {"latitud": -6.8389, "longitud": -78.2444}},
                    {"id": "060305", "nombre": "JORGE CHAVEZ", "coordenadas": {"latitud": -6.9389, "longitud": -78.0861}},
                    {"id": "060306", "nombre": "JOSE GALVEZ", "coordenadas": {"latitud": -6.9222, "longitud": -78.1333}},
                    {"id": "060307", "nombre": "MIGUEL IGLESIAS", "coordenadas": {"latitud": -6.6333, "longitud": -78.2333}},
                    {"id": "060308", "nombre": "OXAMARCA", "coordenadas": {"latitud": -7.0333, "longitud": -78.0667}},
                    {"id": "060309", "nombre": "SOROCHUCO", "coordenadas": {"latitud": -6.9111, "longitud": -78.2500}},
                    {"id": "060310", "nombre": "SUCRE", "coordenadas": {"latitud": -6.9389, "longitud": -78.1389}},
                    {"id": "060311", "nombre": "UTCO", "coordenadas": {"latitud": -6.9000, "longitud": -78.0667}},
                    {"id": "060312", "nombre": "LA LIBERTAD DE PALLAN", "coordenadas": {"latitud": -6.7333, "longitud": -78.2333}}
                ]
            },
            {
                "id": "0604",
                "nombre": "CHOTA",
                "coordenadas": {"latitud": -6.5647, "longitud": -78.6481},
                "distritos": [
                    {"id": "060401", "nombre": "CHOTA", "coordenadas": {"latitud": -6.5647, "longitud": -78.6481}},
                    {"id": "060402", "nombre": "ANGUIA", "coordenadas": {"latitud": -6.3333, "longitud": -78.6000}},
                    {"id": "060403", "nombre": "CHADIN", "coordenadas": {"latitud": -6.4333, "longitud": -78.4167}},
                    {"id": "060404", "nombre": "CHIGUIRIP", "coordenadas": {"latitud": -6.4167, "longitud": -78.7167}},
                    {"id": "060405", "nombre": "CHIMBAN", "coordenadas": {"latitud": -6.2833, "longitud": -78.5333}},
                    {"id": "060406", "nombre": "CHOROPAMPA", "coordenadas": {"latitud": -6.4333, "longitud": -78.3500}},
                    {"id": "060407", "nombre": "COCHABAMBA", "coordenadas": {"latitud": -6.4667, "longitud": -78.8833}},
                    {"id": "060408", "nombre": "CONCHAN", "coordenadas": {"latitud": -6.4333, "longitud": -78.6583}},
                    {"id": "060409", "nombre": "HUAMBOS", "coordenadas": {"latitud": -6.4517, "longitud": -78.9644}},
                    {"id": "060410", "nombre": "LAJAS", "coordenadas": {"latitud": -6.5583, "longitud": -78.7389}},
                    {"id": "060411", "nombre": "LLAMA", "coordenadas": {"latitud": -6.5144, "longitud": -79.1219}},
                    {"id": "060412", "nombre": "MIRACOSTA", "coordenadas": {"latitud": -6.4000, "longitud": -79.2833}},
                    {"id": "060413", "nombre": "PACCHA", "coordenadas": {"latitud": -6.5000, "longitud": -78.7167}},
                    {"id": "060414", "nombre": "PION", "coordenadas": {"latitud": -6.1833, "longitud": -78.5000}},
                    {"id": "060415", "nombre": "QUEROCOTO", "coordenadas": {"latitud": -6.3583, "longitud": -79.0333}},
                    {"id": "060416", "nombre": "SAN JUAN DE LICUPIS", "coordenadas": {"latitud": -6.4167, "longitud": -79.2417}},
                    {"id": "060417", "nombre": "TACABAMBA", "coordenadas": {"latitud": -6.3917, "longitud": -78.6111}},
                    {"id": "060418", "nombre": "TOCMOCHE", "coordenadas": {"latitud": -6.4125, "longitud": -79.3583}},
                    {"id": "060419", "nombre": "CHALAMARCA", "coordenadas": {"latitud": -6.5167, "longitud": -78.4667}}
                ]
            },
            {
                "id": "0605",
                "nombre": "CONTUMAZA",
                "coordenadas": {"latitud": -7.3644, "longitud": -78.8067},
                "distritos": [
                    {"id": "060501", "nombre": "CONTUMAZA", "coordenadas": {"latitud": -7.3644, "longitud": -78.8067}},
                    {"id": "060502", "nombre": "CHILETE", "coordenadas": {"latitud": -7.2222, "longitud": -78.8417}},
                    {"id": "060503", "nombre": "CUPISNIQUE", "coordenadas": {"latitud": -7.3500, "longitud": -79.0333}},
                    {"id": "060504", "nombre": "GUZMANGO", "coordenadas": {"latitud": -7.3833, "longitud": -78.9000}},
                    {"id": "060505", "nombre": "SAN BENITO", "coordenadas": {"latitud": -7.4250, "longitud": -78.9333}},
                    {"id": "060506", "nombre": "SANTA CRUZ DE TOLEDO", "coordenadas": {"latitud": -7.3333, "longitud": -78.8333}},
                    {"id": "060507", "nombre": "TANTARICA", "coordenadas": {"latitud": -7.2833, "longitud": -78.9333}},
                    {"id": "060508", "nombre": "YONAN", "coordenadas": {"latitud": -7.2500, "longitud": -79.1333}}
                ]
            },
            {
                "id": "0606",
                "nombre": "CUTERVO",
                "coordenadas": {"latitud": -6.3794, "longitud": -78.8197},
                "distritos": [
                    {"id": "060601", "nombre": "CUTERVO", "coordenadas": {"latitud": -6.3794, "longitud": -78.8197}},
                    {"id": "060602", "nombre": "CALLAYUC", "coordenadas": {"latitud": -6.1750, "longitud": -78.9042}},
                    {"id": "060603", "nombre": "CHOROS", "coordenadas": {"latitud": -6.1500, "longitud": -78.7000}},
                    {"id": "060604", "nombre": "CUJILLO", "coordenadas": {"latitud": -6.1083, "longitud": -78.5917}},
                    {"id": "060605", "nombre": "LA RAMADA", "coordenadas": {"latitud": -6.2167, "longitud": -78.5833}},
                    {"id": "060606", "nombre": "PIMPINGOS", "coordenadas": {"latitud": -6.0667, "longitud": -78.7833}},
                    {"id": "060607", "nombre": "QUEROCOTILLO", "coordenadas": {"latitud": -6.2750, "longitud": -79.0333}},
                    {"id": "060608", "nombre": "SAN ANDRES DE CUTERVO", "coordenadas": {"latitud": -6.2333, "longitud": -78.7167}},
                    {"id": "060609", "nombre": "SAN JUAN DE CUTERVO", "coordenadas": {"latitud": -6.1833, "longitud": -78.6333}},
                    {"id": "060610", "nombre": "SAN LUIS DE LUCMA", "coordenadas": {"latitud": -6.2917, "longitud": -78.6083}},
                    {"id": "060611", "nombre": "SANTA CRUZ", "coordenadas": {"latitud": -6.1167, "longitud": -78.8500}},
                    {"id": "060612", "nombre": "SANTO DOMINGO DE LA CAPILLA", "coordenadas": {"latitud": -6.2500, "longitud": -78.8583}},
                    {"id": "060613", "nombre": "SANTO TOMAS", "coordenadas": {"latitud": -6.1500, "longitud": -78.6833}},
                    {"id": "060614", "nombre": "SOCOTA", "coordenadas": {"latitud": -6.3167, "longitud": -78.7000}},
                    {"id": "060615", "nombre": "TORIBIO CASANOVA", "coordenadas": {"latitud": -6.1667, "longitud": -78.7000}}
                ]
            }
        ]
    },
    "08": {  # CUSCO
        "provincias": [
            {
                "id": "0801",
                "nombre": "CUSCO",
                "coordenadas": {"latitud": -13.5250, "longitud": -71.9722},
                "distritos": [
                    {"id": "080101", "nombre": "CUSCO", "coordenadas": {"latitud": -13.5250, "longitud": -71.9722}},
                    {"id": "080102", "nombre": "CCORCA", "coordenadas": {"latitud": -13.5833, "longitud": -72.0667}},
                    {"id": "080103", "nombre": "POROY", "coordenadas": {"latitud": -13.4972, "longitud": -72.0417}},
                    {"id": "080104", "nombre": "SAN JERONIMO", "coordenadas": {"latitud": -13.5444, "longitud": -71.8875}},
                    {"id": "080105", "nombre": "SAN SEBASTIAN", "coordenadas": {"latitud": -13.5306, "longitud": -71.9333}},
                    {"id": "080106", "nombre": "SANTIAGO", "coordenadas": {"latitud": -13.5278, "longitud": -71.9861}},
                    {"id": "080107", "nombre": "SAYLLA", "coordenadas": {"latitud": -13.5667, "longitud": -71.8333}},
                    {"id": "080108", "nombre": "WANCHAQ", "coordenadas": {"latitud": -13.5222, "longitud": -71.9667}}
                ]
            },
            {
                "id": "0802",
                "nombre": "ACOMAYO",
                "coordenadas": {"latitud": -13.9167, "longitud": -71.6833},
                "distritos": [
                    {"id": "080201", "nombre": "ACOMAYO", "coordenadas": {"latitud": -13.9167, "longitud": -71.6833}},
                    {"id": "080202", "nombre": "ACOPIA", "coordenadas": {"latitud": -13.9500, "longitud": -71.6500}},
                    {"id": "080203", "nombre": "ACOS", "coordenadas": {"latitud": -13.9000, "longitud": -71.7500}},
                    {"id": "080204", "nombre": "MOSOC LLACTA", "coordenadas": {"latitud": -13.9333, "longitud": -71.6000}},
                    {"id": "080205", "nombre": "POMACANCHI", "coordenadas": {"latitud": -13.9667, "longitud": -71.7000}},
                    {"id": "080206", "nombre": "RONDOCAN", "coordenadas": {"latitud": -13.9833, "longitud": -71.6500}},
                    {"id": "080207", "nombre": "SANGARARA", "coordenadas": {"latitud": -13.9500, "longitud": -71.7333}}
                ]
            },
            {
                "id": "0803",
                "nombre": "ANTA",
                "coordenadas": {"latitud": -13.4667, "longitud": -72.1500},
                "distritos": [
                    {"id": "080301", "nombre": "ANTA", "coordenadas": {"latitud": -13.4667, "longitud": -72.1500}},
                    {"id": "080302", "nombre": "ANCAHUASI", "coordenadas": {"latitud": -13.4000, "longitud": -72.2000}},
                    {"id": "080303", "nombre": "CACHIMAYO", "coordenadas": {"latitud": -13.4500, "longitud": -72.1000}},
                    {"id": "080304", "nombre": "CHINCHAYPUJIO", "coordenadas": {"latitud": -13.5000, "longitud": -72.2000}},
                    {"id": "080305", "nombre": "HUAROCONDO", "coordenadas": {"latitud": -13.4333, "longitud": -72.1333}},
                    {"id": "080306", "nombre": "LIMATAMBO", "coordenadas": {"latitud": -13.4167, "longitud": -72.0667}},
                    {"id": "080307", "nombre": "MOLLEPATA", "coordenadas": {"latitud": -13.3500, "longitud": -72.2500}},
                    {"id": "080308", "nombre": "PUCYURA", "coordenadas": {"latitud": -13.4833, "longitud": -72.1167}},
                    {"id": "080309", "nombre": "ZURITE", "coordenadas": {"latitud": -13.4500, "longitud": -72.2000}}
                ]
            },
            {
                "id": "0804",
                "nombre": "CALCA",
                "coordenadas": {"latitud": -13.3333, "longitud": -71.9500},
                "distritos": [
                    {"id": "080401", "nombre": "CALCA", "coordenadas": {"latitud": -13.3333, "longitud": -71.9500}},
                    {"id": "080402", "nombre": "COYA", "coordenadas": {"latitud": -13.3000, "longitud": -71.9167}},
                    {"id": "080403", "nombre": "LAMAY", "coordenadas": {"latitud": -13.3500, "longitud": -71.9000}},
                    {"id": "080404", "nombre": "LARES", "coordenadas": {"latitud": -13.2000, "longitud": -72.0500}},
                    {"id": "080405", "nombre": "PISAC", "coordenadas": {"latitud": -13.4167, "longitud": -71.8500}},
                    {"id": "080406", "nombre": "SAN SALVADOR", "coordenadas": {"latitud": -13.2500, "longitud": -71.8333}},
                    {"id": "080407", "nombre": "TARAY", "coordenadas": {"latitud": -13.3667, "longitud": -71.9000}},
                    {"id": "080408", "nombre": "YANATILE", "coordenadas": {"latitud": -13.2000, "longitud": -71.9000}}
                ]
            },
            {
                "id": "0805",
                "nombre": "CANAS",
                "coordenadas": {"latitud": -14.2167, "longitud": -71.3333},
                "distritos": [
                    {"id": "080501", "nombre": "YANAOCA", "coordenadas": {"latitud": -14.2167, "longitud": -71.3333}},
                    {"id": "080502", "nombre": "CHECCA", "coordenadas": {"latitud": -14.2500, "longitud": -71.3000}},
                    {"id": "080503", "nombre": "KUNTURKANKI", "coordenadas": {"latitud": -14.2000, "longitud": -71.2500}},
                    {"id": "080504", "nombre": "LANGUI", "coordenadas": {"latitud": -14.1833, "longitud": -71.4000}},
                    {"id": "080505", "nombre": "LAYO", "coordenadas": {"latitud": -14.1500, "longitud": -71.3500}},
                    {"id": "080506", "nombre": "PAMPAMARCA", "coordenadas": {"latitud": -14.2333, "longitud": -71.2833}},
                    {"id": "080507", "nombre": "QUEHUE", "coordenadas": {"latitud": -14.2667, "longitud": -71.3500}},
                    {"id": "080508", "nombre": "TUPAC AMARU", "coordenadas": {"latitud": -14.2000, "longitud": -71.3000}}
                ]
            }
        ]
    },
    "09": {  # HUANCAVELICA
        "provincias": [
            {
                "id": "0901",
                "nombre": "HUANCAVELICA",
                "coordenadas": {"latitud": -12.7867, "longitud": -74.9750},
                "distritos": [
                    {"id": "090101", "nombre": "HUANCAVELICA", "coordenadas": {"latitud": -12.7867, "longitud": -74.9750}},
                    {"id": "090102", "nombre": "ACOBAMBILLA", "coordenadas": {"latitud": -12.8333, "longitud": -74.9500}},
                    {"id": "090103", "nombre": "ACORIA", "coordenadas": {"latitud": -12.7500, "longitud": -74.9167}},
                    {"id": "090104", "nombre": "CONAYCA", "coordenadas": {"latitud": -12.7000, "longitud": -74.9333}},
                    {"id": "090105", "nombre": "CUENCA", "coordenadas": {"latitud": -12.7333, "longitud": -74.8500}},
                    {"id": "090106", "nombre": "HUACHOCOLPA", "coordenadas": {"latitud": -12.8000, "longitud": -74.8000}},
                    {"id": "090107", "nombre": "HUAYLLAHUARA", "coordenadas": {"latitud": -12.7667, "longitud": -74.9000}},
                    {"id": "090108", "nombre": "IZCUCHACA", "coordenadas": {"latitud": -12.7000, "longitud": -74.9667}},
                    {"id": "090109", "nombre": "LARIA", "coordenadas": {"latitud": -12.7500, "longitud": -74.8333}},
                    {"id": "090110", "nombre": "MANTA", "coordenadas": {"latitud": -12.8000, "longitud": -74.8667}},
                    {"id": "090111", "nombre": "MARISCAL CACERES", "coordenadas": {"latitud": -12.7667, "longitud": -74.9500}},
                    {"id": "090112", "nombre": "MOYA", "coordenadas": {"latitud": -12.7333, "longitud": -74.9000}},
                    {"id": "090113", "nombre": "NUEVO OCCORO", "coordenadas": {"latitud": -12.7833, "longitud": -74.9167}},
                    {"id": "090114", "nombre": "PALCA", "coordenadas": {"latitud": -12.7500, "longitud": -74.9833}},
                    {"id": "090115", "nombre": "PILCHACA", "coordenadas": {"latitud": -12.7333, "longitud": -74.9667}},
                    {"id": "090116", "nombre": "VILCA", "coordenadas": {"latitud": -12.7667, "longitud": -74.8333}},
                    {"id": "090117", "nombre": "YAULI", "coordenadas": {"latitud": -12.8000, "longitud": -74.9333}}
                ]
            },
            {
                "id": "0902",
                "nombre": "ACOBAMBA",
                "coordenadas": {"latitud": -12.8500, "longitud": -74.5667},
                "distritos": [
                    {"id": "090201", "nombre": "ACOBAMBA", "coordenadas": {"latitud": -12.8500, "longitud": -74.5667}},
                    {"id": "090202", "nombre": "ANDAYMARCA", "coordenadas": {"latitud": -12.8000, "longitud": -74.6000}},
                    {"id": "090203", "nombre": "ANTA", "coordenadas": {"latitud": -12.9000, "longitud": -74.5000}},
                    {"id": "090204", "nombre": "CAJA", "coordenadas": {"latitud": -12.8333, "longitud": -74.5333}},
                    {"id": "090205", "nombre": "MARCAS", "coordenadas": {"latitud": -12.8667, "longitud": -74.5167}},
                    {"id": "090206", "nombre": "PAUCARA", "coordenadas": {"latitud": -12.8167, "longitud": -74.5500}},
                    {"id": "090207", "nombre": "POMACOCHA", "coordenadas": {"latitud": -12.8833, "longitud": -74.5833}},
                    {"id": "090208", "nombre": "ROSARIO", "coordenadas": {"latitud": -12.8333, "longitud": -74.5833}}
                ]
            },
            {
                "id": "0903",
                "nombre": "ANGARAES",
                "coordenadas": {"latitud": -13.0000, "longitud": -74.9000},
                "distritos": [
                    {"id": "090301", "nombre": "LIRCAY", "coordenadas": {"latitud": -13.0000, "longitud": -74.9000}},
                    {"id": "090302", "nombre": "ANCHONGA", "coordenadas": {"latitud": -12.9500, "longitud": -74.8833}},
                    {"id": "090303", "nombre": "CALLANMARCA", "coordenadas": {"latitud": -12.9833, "longitud": -74.8500}},
                    {"id": "090304", "nombre": "CCOCHACCASA", "coordenadas": {"latitud": -13.0167, "longitud": -74.8667}},
                    {"id": "090305", "nombre": "CHINCHO", "coordenadas": {"latitud": -12.9333, "longitud": -74.9167}},
                    {"id": "090306", "nombre": "CONGALLA", "coordenadas": {"latitud": -12.9667, "longitud": -74.9333}},
                    {"id": "090307", "nombre": "HUANCA-HUANCA", "coordenadas": {"latitud": -12.9500, "longitud": -74.9500}},
                    {"id": "090308", "nombre": "HUAYLLAY GRANDE", "coordenadas": {"latitud": -13.0167, "longitud": -74.9167}},
                    {"id": "090309", "nombre": "JULCAMARCA", "coordenadas": {"latitud": -12.9833, "longitud": -74.9833}},
                    {"id": "090310", "nombre": "SAN ANTONIO DE ANTAPARCO", "coordenadas": {"latitud": -12.9333, "longitud": -74.8667}},
                    {"id": "090311", "nombre": "SANTO TOMAS DE PATA", "coordenadas": {"latitud": -12.9667, "longitud": -74.8667}},
                    {"id": "090312", "nombre": "SECCLLA", "coordenadas": {"latitud": -12.9500, "longitud": -74.8333}}
                ]
            }
        ]
    }
}

# Leer el archivo actual
with open('ubigeo_peru.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Actualizar departamentos con provincias y distritos
for dept in data['departamentos']:
    dept_id = dept['id']
    if dept_id in provinces_districts:
        dept['provincias'] = provinces_districts[dept_id]['provincias']

# Guardar el archivo actualizado
with open('ubigeo_peru.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ Provincias y distritos de Cajamarca, Cusco y Huancavelica agregados al archivo ubigeo_peru.json") 