import json

# Datos de los departamentos faltantes
missing_departments = {
    "15": {  # LIMA
        "id": "15",
        "nombre": "LIMA",
        "coordenadas": {"latitud": -12.0433, "longitud": -77.0283},
        "provincias": [
            {
                "id": "1501",
                "nombre": "LIMA",
                "coordenadas": {"latitud": -12.0433, "longitud": -77.0283},
                "distritos": [
                    {"id": "150101", "nombre": "LIMA", "coordenadas": {"latitud": -12.0433, "longitud": -77.0283}},
                    {"id": "150102", "nombre": "ANCON", "coordenadas": {"latitud": -11.7667, "longitud": -77.1833}},
                    {"id": "150103", "nombre": "ATE", "coordenadas": {"latitud": -12.0167, "longitud": -76.9167}},
                    {"id": "150104", "nombre": "BARRANCO", "coordenadas": {"latitud": -12.15, "longitud": -77.0167}},
                    {"id": "150105", "nombre": "BREÑA", "coordenadas": {"latitud": -12.05, "longitud": -77.05}},
                    {"id": "150106", "nombre": "CARABAYLLO", "coordenadas": {"latitud": -11.9167, "longitud": -77.05}},
                    {"id": "150107", "nombre": "CHACLACAYO", "coordenadas": {"latitud": -11.9833, "longitud": -76.7667}},
                    {"id": "150108", "nombre": "CHORRILLOS", "coordenadas": {"latitud": -12.1833, "longitud": -77.0167}},
                    {"id": "150109", "nombre": "CIENCIAS", "coordenadas": {"latitud": -12.0833, "longitud": -77.0833}},
                    {"id": "150110", "nombre": "COMAS", "coordenadas": {"latitud": -11.9333, "longitud": -77.05}},
                    {"id": "150111", "nombre": "EL AGUSTINO", "coordenadas": {"latitud": -12.05, "longitud": -76.9833}},
                    {"id": "150112", "nombre": "INDEPENDENCIA", "coordenadas": {"latitud": -11.9833, "longitud": -77.05}},
                    {"id": "150113", "nombre": "JESUS MARIA", "coordenadas": {"latitud": -12.0833, "longitud": -77.05}},
                    {"id": "150114", "nombre": "LA MOLINA", "coordenadas": {"latitud": -12.0833, "longitud": -76.9167}},
                    {"id": "150115", "nombre": "LA VICTORIA", "coordenadas": {"latitud": -12.0667, "longitud": -77.0333}},
                    {"id": "150116", "nombre": "LINCE", "coordenadas": {"latitud": -12.0833, "longitud": -77.0333}},
                    {"id": "150117", "nombre": "LOS OLIVOS", "coordenadas": {"latitud": -11.9667, "longitud": -77.0667}},
                    {"id": "150118", "nombre": "LURIGANCHO", "coordenadas": {"latitud": -11.9667, "longitud": -76.6667}},
                    {"id": "150119", "nombre": "LURIN", "coordenadas": {"latitud": -12.2833, "longitud": -76.8667}},
                    {"id": "150120", "nombre": "MAGDALENA DEL MAR", "coordenadas": {"latitud": -12.1, "longitud": -77.0667}},
                    {"id": "150121", "nombre": "PUEBLO LIBRE", "coordenadas": {"latitud": -12.0667, "longitud": -77.0667}},
                    {"id": "150122", "nombre": "MIRAFLORES", "coordenadas": {"latitud": -12.1167, "longitud": -77.0333}},
                    {"id": "150123", "nombre": "PACHACAMAC", "coordenadas": {"latitud": -12.2333, "longitud": -76.8333}},
                    {"id": "150124", "nombre": "PUCUSANA", "coordenadas": {"latitud": -12.4833, "longitud": -76.8}},
                    {"id": "150125", "nombre": "PUENTE PIEDRA", "coordenadas": {"latitud": -11.8667, "longitud": -77.0833}},
                    {"id": "150126", "nombre": "PUNTA HERMOSA", "coordenadas": {"latitud": -12.35, "longitud": -76.8167}},
                    {"id": "150127", "nombre": "PUNTA NEGRA", "coordenadas": {"latitud": -12.3667, "longitud": -76.8}},
                    {"id": "150128", "nombre": "RIMAC", "coordenadas": {"latitud": -12.0333, "longitud": -77.0333}},
                    {"id": "150129", "nombre": "SAN BARTOLO", "coordenadas": {"latitud": -12.3833, "longitud": -76.7833}},
                    {"id": "150130", "nombre": "SAN BORJA", "coordenadas": {"latitud": -12.1, "longitud": -77.0}},
                    {"id": "150131", "nombre": "SAN ISIDRO", "coordenadas": {"latitud": -12.1, "longitud": -77.0333}},
                    {"id": "150132", "nombre": "SAN JUAN DE LURIGANCHO", "coordenadas": {"latitud": -11.9833, "longitud": -76.9833}},
                    {"id": "150133", "nombre": "SAN JUAN DE MIRAFLORES", "coordenadas": {"latitud": -12.15, "longitud": -76.9667}},
                    {"id": "150134", "nombre": "SAN LUIS", "coordenadas": {"latitud": -12.0833, "longitud": -77.0}},
                    {"id": "150135", "nombre": "SAN MARTIN DE PORRES", "coordenadas": {"latitud": -12.0, "longitud": -77.0833}},
                    {"id": "150136", "nombre": "SAN MIGUEL", "coordenadas": {"latitud": -12.0833, "longitud": -77.0833}},
                    {"id": "150137", "nombre": "SANTA ANITA", "coordenadas": {"latitud": -12.05, "longitud": -76.9667}},
                    {"id": "150138", "nombre": "SANTA MARIA DEL MAR", "coordenadas": {"latitud": -12.3333, "longitud": -76.8}},
                    {"id": "150139", "nombre": "SANTA ROSA", "coordenadas": {"latitud": -12.0667, "longitud": -77.1167}},
                    {"id": "150140", "nombre": "SANTIAGO DE SURCO", "coordenadas": {"latitud": -12.15, "longitud": -76.9833}},
                    {"id": "150141", "nombre": "SURQUILLO", "coordenadas": {"latitud": -12.1167, "longitud": -77.0167}},
                    {"id": "150142", "nombre": "VILLA EL SALVADOR", "coordenadas": {"latitud": -12.2167, "longitud": -76.9333}},
                    {"id": "150143", "nombre": "VILLA MARIA DEL TRIUNFO", "coordenadas": {"latitud": -12.1667, "longitud": -76.95}}
                ]
            },
            {
                "id": "1502",
                "nombre": "BARRANCA",
                "coordenadas": {"latitud": -10.75, "longitud": -77.7667},
                "distritos": [
                    {"id": "150201", "nombre": "BARRANCA", "coordenadas": {"latitud": -10.75, "longitud": -77.7667}},
                    {"id": "150202", "nombre": "PARAMONGA", "coordenadas": {"latitud": -10.6667, "longitud": -77.8333}},
                    {"id": "150203", "nombre": "PATIVILCA", "coordenadas": {"latitud": -10.7, "longitud": -77.7833}},
                    {"id": "150204", "nombre": "SUPE", "coordenadas": {"latitud": -10.8, "longitud": -77.7167}},
                    {"id": "150205", "nombre": "SUPE PUERTO", "coordenadas": {"latitud": -10.8, "longitud": -77.75}}
                ]
            },
            {
                "id": "1503",
                "nombre": "CAJATAMBO",
                "coordenadas": {"latitud": -10.4833, "longitud": -77.0167},
                "distritos": [
                    {"id": "150301", "nombre": "CAJATAMBO", "coordenadas": {"latitud": -10.4833, "longitud": -77.0167}},
                    {"id": "150302", "nombre": "COPA", "coordenadas": {"latitud": -10.3667, "longitud": -77.0}},
                    {"id": "150303", "nombre": "GORGOR", "coordenadas": {"latitud": -10.4333, "longitud": -77.0}},
                    {"id": "150304", "nombre": "HUANCAPON", "coordenadas": {"latitud": -10.5, "longitud": -77.0}},
                    {"id": "150305", "nombre": "MANAS", "coordenadas": {"latitud": -10.5333, "longitud": -77.0}}
                ]
            },
            {
                "id": "1504",
                "nombre": "CANTA",
                "coordenadas": {"latitud": -11.4667, "longitud": -76.6333},
                "distritos": [
                    {"id": "150401", "nombre": "CANTA", "coordenadas": {"latitud": -11.4667, "longitud": -76.6333}},
                    {"id": "150402", "nombre": "ARAHUAY", "coordenadas": {"latitud": -11.5667, "longitud": -76.7}},
                    {"id": "150403", "nombre": "HUAMANTANGA", "coordenadas": {"latitud": -11.4, "longitud": -76.7}},
                    {"id": "150404", "nombre": "HUAROS", "coordenadas": {"latitud": -11.5, "longitud": -76.6}},
                    {"id": "150405", "nombre": "LACHAQUI", "coordenadas": {"latitud": -11.5333, "longitud": -76.6333}},
                    {"id": "150406", "nombre": "SAN BUENAVENTURA", "coordenadas": {"latitud": -11.4333, "longitud": -76.6333}},
                    {"id": "150407", "nombre": "SANTA ROSA DE QUIVES", "coordenadas": {"latitud": -11.4, "longitud": -76.5667}}
                ]
            },
            {
                "id": "1505",
                "nombre": "CAÑETE",
                "coordenadas": {"latitud": -13.0833, "longitud": -76.4},
                "distritos": [
                    {"id": "150501", "nombre": "SAN VICENTE DE CAÑETE", "coordenadas": {"latitud": -13.0833, "longitud": -76.4}},
                    {"id": "150502", "nombre": "ASIA", "coordenadas": {"latitud": -12.8, "longitud": -76.5}},
                    {"id": "150503", "nombre": "CALANGO", "coordenadas": {"latitud": -12.5667, "longitud": -76.4167}},
                    {"id": "150504", "nombre": "CERRO AZUL", "coordenadas": {"latitud": -13.0667, "longitud": -76.5}},
                    {"id": "150505", "nombre": "CHILCA", "coordenadas": {"latitud": -12.5167, "longitud": -76.7333}},
                    {"id": "150506", "nombre": "COAYLLO", "coordenadas": {"latitud": -12.7, "longitud": -76.5833}},
                    {"id": "150507", "nombre": "IMPERIAL", "coordenadas": {"latitud": -13.0667, "longitud": -76.35}},
                    {"id": "150508", "nombre": "LUNAHUANA", "coordenadas": {"latitud": -13.0333, "longitud": -76.1667}},
                    {"id": "150509", "nombre": "MALA", "coordenadas": {"latitud": -12.65, "longitud": -76.6333}},
                    {"id": "150510", "nombre": "NUEVO IMPERIAL", "coordenadas": {"latitud": -13.0833, "longitud": -76.3333}},
                    {"id": "150511", "nombre": "PACARAN", "coordenadas": {"latitud": -12.8667, "longitud": -76.3333}},
                    {"id": "150512", "nombre": "QUILMANA", "coordenadas": {"latitud": -12.95, "longitud": -76.3833}},
                    {"id": "150513", "nombre": "SAN ANTONIO", "coordenadas": {"latitud": -12.6, "longitud": -76.6667}},
                    {"id": "150514", "nombre": "SAN LUIS", "coordenadas": {"latitud": -12.8, "longitud": -76.5}},
                    {"id": "150515", "nombre": "SANTA CRUZ DE FLORES", "coordenadas": {"latitud": -12.6, "longitud": -76.6333}},
                    {"id": "150516", "nombre": "ZUÑIGA", "coordenadas": {"latitud": -12.85, "longitud": -76.3333}}
                ]
            },
            {
                "id": "1506",
                "nombre": "HUARAL",
                "coordenadas": {"latitud": -11.5, "longitud": -77.2},
                "distritos": [
                    {"id": "150601", "nombre": "HUARAL", "coordenadas": {"latitud": -11.5, "longitud": -77.2}},
                    {"id": "150602", "nombre": "ATAVILLOS ALTO", "coordenadas": {"latitud": -11.3333, "longitud": -76.8333}},
                    {"id": "150603", "nombre": "ATAVILLOS BAJO", "coordenadas": {"latitud": -11.3333, "longitud": -76.75}},
                    {"id": "150604", "nombre": "AUCALLAMA", "coordenadas": {"latitud": -11.5667, "longitud": -77.1667}},
                    {"id": "150605", "nombre": "CHANCAY", "coordenadas": {"latitud": -11.5667, "longitud": -77.2667}},
                    {"id": "150606", "nombre": "IHUARI", "coordenadas": {"latitud": -11.4167, "longitud": -76.9167}},
                    {"id": "150607", "nombre": "LAMPIAN", "coordenadas": {"latitud": -11.3333, "longitud": -76.6667}},
                    {"id": "150608", "nombre": "PACARAOS", "coordenadas": {"latitud": -11.1667, "longitud": -76.5}},
                    {"id": "150609", "nombre": "SAN MIGUEL DE ACOS", "coordenadas": {"latitud": -11.3333, "longitud": -76.8333}},
                    {"id": "150610", "nombre": "SANTA CRUZ DE ANDAMARCA", "coordenadas": {"latitud": -11.3333, "longitud": -76.75}},
                    {"id": "150611", "nombre": "SUMBILCA", "coordenadas": {"latitud": -11.3333, "longitud": -76.6667}},
                    {"id": "150612", "nombre": "VEINTISIETE DE NOVIEMBRE", "coordenadas": {"latitud": -11.5, "longitud": -77.1667}}
                ]
            },
            {
                "id": "1507",
                "nombre": "HUAROCHIRI",
                "coordenadas": {"latitud": -11.85, "longitud": -76.3333},
                "distritos": [
                    {"id": "150701", "nombre": "MATUCANA", "coordenadas": {"latitud": -11.85, "longitud": -76.3333}},
                    {"id": "150702", "nombre": "ANTIOQUIA", "coordenadas": {"latitud": -11.8, "longitud": -76.25}},
                    {"id": "150703", "nombre": "CALLAHUANCA", "coordenadas": {"latitud": -11.8333, "longitud": -76.4167}},
                    {"id": "150704", "nombre": "CARAMPOMA", "coordenadas": {"latitud": -11.8333, "longitud": -76.5}},
                    {"id": "150705", "nombre": "CHICLA", "coordenadas": {"latitud": -11.7, "longitud": -76.25}},
                    {"id": "150706", "nombre": "CUENCA", "coordenadas": {"latitud": -11.9167, "longitud": -76.25}},
                    {"id": "150707", "nombre": "HUACHUPAMPA", "coordenadas": {"latitud": -11.9167, "longitud": -76.3333}},
                    {"id": "150708", "nombre": "HUANZA", "coordenadas": {"latitud": -11.9167, "longitud": -76.4167}},
                    {"id": "150709", "nombre": "HUAROCHIRI", "coordenadas": {"latitud": -11.9167, "longitud": -76.5}},
                    {"id": "150710", "nombre": "LAHUAYTAMBO", "coordenadas": {"latitud": -11.8333, "longitud": -76.5833}},
                    {"id": "150711", "nombre": "LANGA", "coordenadas": {"latitud": -11.8333, "longitud": -76.6667}},
                    {"id": "150712", "nombre": "LARAOS", "coordenadas": {"latitud": -11.75, "longitud": -76.5}},
                    {"id": "150713", "nombre": "MARIATANA", "coordenadas": {"latitud": -11.8333, "longitud": -76.75}},
                    {"id": "150714", "nombre": "RICARDO PALMA", "coordenadas": {"latitud": -11.9167, "longitud": -76.6667}},
                    {"id": "150715", "nombre": "SAN ANDRES DE TUPICOCHA", "coordenadas": {"latitud": -11.8333, "longitud": -76.8333}},
                    {"id": "150716", "nombre": "SAN ANTONIO", "coordenadas": {"latitud": -11.9167, "longitud": -76.75}},
                    {"id": "150717", "nombre": "SAN BARTOLOME", "coordenadas": {"latitud": -11.9167, "longitud": -76.8333}},
                    {"id": "150718", "nombre": "SAN DAMIAN", "coordenadas": {"latitud": -11.8333, "longitud": -76.9167}},
                    {"id": "150719", "nombre": "SAN JUAN DE IRIS", "coordenadas": {"latitud": -11.9167, "longitud": -76.9167}},
                    {"id": "150720", "nombre": "SAN JUAN DE TANTARANCHE", "coordenadas": {"latitud": -11.8333, "longitud": -77.0}},
                    {"id": "150721", "nombre": "SAN LORENZO DE QUINTI", "coordenadas": {"latitud": -11.9167, "longitud": -77.0}},
                    {"id": "150722", "nombre": "SAN MATEO", "coordenadas": {"latitud": -11.8333, "longitud": -77.0833}},
                    {"id": "150723", "nombre": "SAN MATEO DE OTAO", "coordenadas": {"latitud": -11.9167, "longitud": -77.0833}},
                    {"id": "150724", "nombre": "SAN PEDRO DE CASTA", "coordenadas": {"latitud": -11.8333, "longitud": -77.1667}},
                    {"id": "150725", "nombre": "SAN PEDRO DE HUANCAYRE", "coordenadas": {"latitud": -11.9167, "longitud": -77.1667}},
                    {"id": "150726", "nombre": "SANGALLAYA", "coordenadas": {"latitud": -11.8333, "longitud": -77.25}},
                    {"id": "150727", "nombre": "SANTA CRUZ DE COCACHACRA", "coordenadas": {"latitud": -11.9167, "longitud": -77.25}},
                    {"id": "150728", "nombre": "SANTA EULALIA", "coordenadas": {"latitud": -11.8333, "longitud": -77.3333}},
                    {"id": "150729", "nombre": "SANTIAGO DE ANCHUCAYA", "coordenadas": {"latitud": -11.9167, "longitud": -77.3333}},
                    {"id": "150730", "nombre": "SANTIAGO DE TUNA", "coordenadas": {"latitud": -11.8333, "longitud": -77.4167}},
                    {"id": "150731", "nombre": "SANTO DOMINGO DE LOS OLLEROS", "coordenadas": {"latitud": -11.9167, "longitud": -77.4167}},
                    {"id": "150732", "nombre": "SURCO", "coordenadas": {"latitud": -11.8333, "longitud": -77.5}}
                ]
            },
            {
                "id": "1508",
                "nombre": "HUAURA",
                "coordenadas": {"latitud": -11.0667, "longitud": -77.6},
                "distritos": [
                    {"id": "150801", "nombre": "HUACHO", "coordenadas": {"latitud": -11.0667, "longitud": -77.6}},
                    {"id": "150802", "nombre": "AMBAR", "coordenadas": {"latitud": -11.0, "longitud": -77.5}},
                    {"id": "150803", "nombre": "CALETA DE CARQUIN", "coordenadas": {"latitud": -11.1, "longitud": -77.6333}},
                    {"id": "150804", "nombre": "CHECRAS", "coordenadas": {"latitud": -10.8333, "longitud": -77.5}},
                    {"id": "150805", "nombre": "HUALMAY", "coordenadas": {"latitud": -11.1, "longitud": -77.6}},
                    {"id": "150806", "nombre": "HUAURA", "coordenadas": {"latitud": -11.0667, "longitud": -77.6}},
                    {"id": "150807", "nombre": "LEONCIO PRADO", "coordenadas": {"latitud": -11.0, "longitud": -77.6}},
                    {"id": "150808", "nombre": "PACCHO", "coordenadas": {"latitud": -10.9167, "longitud": -77.5}},
                    {"id": "150809", "nombre": "SANTA LEONOR", "coordenadas": {"latitud": -10.8333, "longitud": -77.6}},
                    {"id": "150810", "nombre": "SANTA MARIA", "coordenadas": {"latitud": -11.1, "longitud": -77.6667}},
                    {"id": "150811", "nombre": "SAYAN", "coordenadas": {"latitud": -11.1333, "longitud": -77.5}},
                    {"id": "150812", "nombre": "VEGUETA", "coordenadas": {"latitud": -11.0167, "longitud": -77.6333}}
                ]
            },
            {
                "id": "1509",
                "nombre": "OYON",
                "coordenadas": {"latitud": -10.6667, "longitud": -76.7667},
                "distritos": [
                    {"id": "150901", "nombre": "OYON", "coordenadas": {"latitud": -10.6667, "longitud": -76.7667}},
                    {"id": "150902", "nombre": "ANDAJES", "coordenadas": {"latitud": -10.75, "longitud": -76.6667}},
                    {"id": "150903", "nombre": "CAUJUL", "coordenadas": {"latitud": -10.5833, "longitud": -76.6667}},
                    {"id": "150904", "nombre": "COCHAMARCA", "coordenadas": {"latitud": -10.75, "longitud": -76.8333}},
                    {"id": "150905", "nombre": "NAVAN", "coordenadas": {"latitud": -10.6667, "longitud": -76.8333}},
                    {"id": "150906", "nombre": "PACHANGARA", "coordenadas": {"latitud": -10.5833, "longitud": -76.8333}}
                ]
            },
            {
                "id": "1510",
                "nombre": "YAUYOS",
                "coordenadas": {"latitud": -12.4667, "longitud": -75.7333},
                "distritos": [
                    {"id": "151001", "nombre": "YAUYOS", "coordenadas": {"latitud": -12.4667, "longitud": -75.7333}},
                    {"id": "151002", "nombre": "ALIS", "coordenadas": {"latitud": -12.3333, "longitud": -75.8333}},
                    {"id": "151003", "nombre": "ALLAUCA", "coordenadas": {"latitud": -12.5, "longitud": -75.8333}},
                    {"id": "151004", "nombre": "AYAVIRI", "coordenadas": {"latitud": -12.3333, "longitud": -75.75}},
                    {"id": "151005", "nombre": "AZANGARO", "coordenadas": {"latitud": -12.5, "longitud": -75.75}},
                    {"id": "151006", "nombre": "CACRA", "coordenadas": {"latitud": -12.3333, "longitud": -75.6667}},
                    {"id": "151007", "nombre": "CARANIA", "coordenadas": {"latitud": -12.5, "longitud": -75.6667}},
                    {"id": "151008", "nombre": "CATAHUASI", "coordenadas": {"latitud": -12.3333, "longitud": -75.5833}},
                    {"id": "151009", "nombre": "CHOCOS", "coordenadas": {"latitud": -12.5, "longitud": -75.5833}},
                    {"id": "151010", "nombre": "COCHAS", "coordenadas": {"latitud": -12.3333, "longitud": -75.5}},
                    {"id": "151011", "nombre": "COLONIA", "coordenadas": {"latitud": -12.5, "longitud": -75.5}},
                    {"id": "151012", "nombre": "HONGOS", "coordenadas": {"latitud": -12.3333, "longitud": -75.4167}},
                    {"id": "151013", "nombre": "HUAMPARA", "coordenadas": {"latitud": -12.5, "longitud": -75.4167}},
                    {"id": "151014", "nombre": "HUANCAYA", "coordenadas": {"latitud": -12.3333, "longitud": -75.3333}},
                    {"id": "151015", "nombre": "HUANGASCAR", "coordenadas": {"latitud": -12.5, "longitud": -75.3333}},
                    {"id": "151016", "nombre": "HUANTAN", "coordenadas": {"latitud": -12.3333, "longitud": -75.25}},
                    {"id": "151017", "nombre": "HUAÑEC", "coordenadas": {"latitud": -12.5, "longitud": -75.25}},
                    {"id": "151018", "nombre": "LARAOS", "coordenadas": {"latitud": -12.3333, "longitud": -75.1667}},
                    {"id": "151019", "nombre": "LINCHA", "coordenadas": {"latitud": -12.5, "longitud": -75.1667}},
                    {"id": "151020", "nombre": "MADEAN", "coordenadas": {"latitud": -12.3333, "longitud": -75.0833}},
                    {"id": "151021", "nombre": "MIRAFLORES", "coordenadas": {"latitud": -12.5, "longitud": -75.0833}},
                    {"id": "151022", "nombre": "OMAS", "coordenadas": {"latitud": -12.3333, "longitud": -75.0}},
                    {"id": "151023", "nombre": "PUTINZA", "coordenadas": {"latitud": -12.5, "longitud": -75.0}},
                    {"id": "151024", "nombre": "QUINCHES", "coordenadas": {"latitud": -12.3333, "longitud": -74.9167}},
                    {"id": "151025", "nombre": "QUINOCAY", "coordenadas": {"latitud": -12.5, "longitud": -74.9167}},
                    {"id": "151026", "nombre": "SAN JOAQUIN", "coordenadas": {"latitud": -12.3333, "longitud": -74.8333}},
                    {"id": "151027", "nombre": "SAN PEDRO DE PILAS", "coordenadas": {"latitud": -12.5, "longitud": -74.8333}},
                    {"id": "151028", "nombre": "TANTA", "coordenadas": {"latitud": -12.3333, "longitud": -74.75}},
                    {"id": "151029", "nombre": "TAURIPAMPA", "coordenadas": {"latitud": -12.5, "longitud": -74.75}},
                    {"id": "151030", "nombre": "TOMAS", "coordenadas": {"latitud": -12.3333, "longitud": -74.6667}},
                    {"id": "151031", "nombre": "TUPE", "coordenadas": {"latitud": -12.5, "longitud": -74.6667}},
                    {"id": "151032", "nombre": "VIÑAC", "coordenadas": {"latitud": -12.3333, "longitud": -74.5833}},
                    {"id": "151033", "nombre": "VITIS", "coordenadas": {"latitud": -12.5, "longitud": -74.5833}}
                ]
            }
        ]
    },
    "16": {  # LORETO
        "id": "16",
        "nombre": "LORETO",
        "coordenadas": {"latitud": -3.7491, "longitud": -73.2538},
        "provincias": [
            {
                "id": "1601",
                "nombre": "MAYNAS",
                "coordenadas": {"latitud": -3.7491, "longitud": -73.2538},
                "distritos": [
                    {"id": "160101", "nombre": "IQUITOS", "coordenadas": {"latitud": -3.7491, "longitud": -73.2538}},
                    {"id": "160102", "nombre": "ALTO NANAY", "coordenadas": {"latitud": -3.8, "longitud": -73.3}},
                    {"id": "160103", "nombre": "FERNANDO LORES", "coordenadas": {"latitud": -3.7, "longitud": -73.2}},
                    {"id": "160104", "nombre": "INDIANA", "coordenadas": {"latitud": -3.5, "longitud": -73.0}},
                    {"id": "160105", "nombre": "LAS AMAZONAS", "coordenadas": {"latitud": -3.6, "longitud": -73.1}},
                    {"id": "160106", "nombre": "MAZAN", "coordenadas": {"latitud": -3.5, "longitud": -73.1}},
                    {"id": "160107", "nombre": "NAPO", "coordenadas": {"latitud": -3.4, "longitud": -73.2}},
                    {"id": "160108", "nombre": "PUNCHANA", "coordenadas": {"latitud": -3.7, "longitud": -73.3}},
                    {"id": "160109", "nombre": "PUTUMAYO", "coordenadas": {"latitud": -3.3, "longitud": -73.3}},
                    {"id": "160110", "nombre": "TORRES CAUSANA", "coordenadas": {"latitud": -3.2, "longitud": -73.4}},
                    {"id": "160112", "nombre": "BELEN", "coordenadas": {"latitud": -3.8, "longitud": -73.2}},
                    {"id": "160113", "nombre": "SAN JUAN BAUTISTA", "coordenadas": {"latitud": -3.7, "longitud": -73.1}}
                ]
            },
            {
                "id": "1602",
                "nombre": "ALTO AMAZONAS",
                "coordenadas": {"latitud": -5.9, "longitud": -76.1},
                "distritos": [
                    {"id": "160201", "nombre": "YURIMAGUAS", "coordenadas": {"latitud": -5.9, "longitud": -76.1}},
                    {"id": "160202", "nombre": "BALSAPUERTO", "coordenadas": {"latitud": -5.8, "longitud": -76.2}},
                    {"id": "160205", "nombre": "JEBEROS", "coordenadas": {"latitud": -5.7, "longitud": -76.3}},
                    {"id": "160206", "nombre": "LAGUNAS", "coordenadas": {"latitud": -5.6, "longitud": -76.4}},
                    {"id": "160210", "nombre": "SANTA CRUZ", "coordenadas": {"latitud": -5.5, "longitud": -76.5}},
                    {"id": "160211", "nombre": "TENIENTE CESAR LOPEZ ROJAS", "coordenadas": {"latitud": -5.4, "longitud": -76.6}}
                ]
            },
            {
                "id": "1603",
                "nombre": "LORETO",
                "coordenadas": {"latitud": -4.9, "longitud": -73.7},
                "distritos": [
                    {"id": "160301", "nombre": "NAUTA", "coordenadas": {"latitud": -4.9, "longitud": -73.7}},
                    {"id": "160302", "nombre": "PARINARI", "coordenadas": {"latitud": -4.8, "longitud": -73.8}},
                    {"id": "160303", "nombre": "TIGRE", "coordenadas": {"latitud": -4.7, "longitud": -73.9}},
                    {"id": "160304", "nombre": "TROMPETEROS", "coordenadas": {"latitud": -4.6, "longitud": -74.0}},
                    {"id": "160305", "nombre": "URARINAS", "coordenadas": {"latitud": -4.5, "longitud": -74.1}}
                ]
            },
            {
                "id": "1604",
                "nombre": "MARISCAL RAMON CASTILLA",
                "coordenadas": {"latitud": -4.0, "longitud": -70.0},
                "distritos": [
                    {"id": "160401", "nombre": "RAMON CASTILLA", "coordenadas": {"latitud": -4.0, "longitud": -70.0}},
                    {"id": "160402", "nombre": "PEBAS", "coordenadas": {"latitud": -3.9, "longitud": -70.1}},
                    {"id": "160403", "nombre": "YAVARI", "coordenadas": {"latitud": -3.8, "longitud": -70.2}},
                    {"id": "160404", "nombre": "SAN PABLO", "coordenadas": {"latitud": -3.7, "longitud": -70.3}}
                ]
            },
            {
                "id": "1605",
                "nombre": "REQUENA",
                "coordenadas": {"latitud": -5.1, "longitud": -73.9},
                "distritos": [
                    {"id": "160501", "nombre": "REQUENA", "coordenadas": {"latitud": -5.1, "longitud": -73.9}},
                    {"id": "160502", "nombre": "ALTO TAPICHE", "coordenadas": {"latitud": -5.0, "longitud": -74.0}},
                    {"id": "160503", "nombre": "CAPELO", "coordenadas": {"latitud": -4.9, "longitud": -74.1}},
                    {"id": "160504", "nombre": "EMILIO SAN MARTIN", "coordenadas": {"latitud": -4.8, "longitud": -74.2}},
                    {"id": "160505", "nombre": "MAQUIA", "coordenadas": {"latitud": -4.7, "longitud": -74.3}},
                    {"id": "160506", "nombre": "PUINAHUA", "coordenadas": {"latitud": -4.6, "longitud": -74.4}},
                    {"id": "160507", "nombre": "SAQUENA", "coordenadas": {"latitud": -4.5, "longitud": -74.5}},
                    {"id": "160508", "nombre": "SOPLIN", "coordenadas": {"latitud": -4.4, "longitud": -74.6}},
                    {"id": "160509", "nombre": "TAPICHE", "coordenadas": {"latitud": -4.3, "longitud": -74.7}},
                    {"id": "160510", "nombre": "JENARO HERRERA", "coordenadas": {"latitud": -4.2, "longitud": -74.8}}
                ]
            },
            {
                "id": "1606",
                "nombre": "UCAYALI",
                "coordenadas": {"latitud": -8.4, "longitud": -74.5},
                "distritos": [
                    {"id": "160601", "nombre": "CONTAMANA", "coordenadas": {"latitud": -8.4, "longitud": -74.5}},
                    {"id": "160602", "nombre": "INAHUAYA", "coordenadas": {"latitud": -8.3, "longitud": -74.6}},
                    {"id": "160603", "nombre": "PADRE MARQUEZ", "coordenadas": {"latitud": -8.2, "longitud": -74.7}},
                    {"id": "160604", "nombre": "PAMPA HERMOSA", "coordenadas": {"latitud": -8.1, "longitud": -74.8}},
                    {"id": "160605", "nombre": "SARAYACU", "coordenadas": {"latitud": -8.0, "longitud": -74.9}},
                    {"id": "160606", "nombre": "VARGAS GUERRA", "coordenadas": {"latitud": -7.9, "longitud": -75.0}}
                ]
            },
            {
                "id": "1607",
                "nombre": "DATEM DEL MARAÑON",
                "coordenadas": {"latitud": -5.5, "longitud": -75.8},
                "distritos": [
                    {"id": "160701", "nombre": "BARRANCA", "coordenadas": {"latitud": -5.5, "longitud": -75.8}},
                    {"id": "160702", "nombre": "CAHUAPANAS", "coordenadas": {"latitud": -5.4, "longitud": -75.9}},
                    {"id": "160703", "nombre": "MANSERICHE", "coordenadas": {"latitud": -5.3, "longitud": -76.0}},
                    {"id": "160704", "nombre": "MORONA", "coordenadas": {"latitud": -5.2, "longitud": -76.1}},
                    {"id": "160705", "nombre": "PASTAZA", "coordenadas": {"latitud": -5.1, "longitud": -76.2}},
                    {"id": "160706", "nombre": "ANDOAS", "coordenadas": {"latitud": -5.0, "longitud": -76.3}}
                ]
            }
        ]
    },
    "17": {  # MADRE DE DIOS
        "id": "17",
        "nombre": "MADRE DE DIOS",
        "coordenadas": {"latitud": -12.6, "longitud": -69.1833},
        "provincias": [
            {
                "id": "1701",
                "nombre": "TAMBOPATA",
                "coordenadas": {"latitud": -12.6, "longitud": -69.1833},
                "distritos": [
                    {"id": "170101", "nombre": "TAMBOPATA", "coordenadas": {"latitud": -12.6, "longitud": -69.1833}},
                    {"id": "170102", "nombre": "INAMBARI", "coordenadas": {"latitud": -13.0, "longitud": -70.3}},
                    {"id": "170103", "nombre": "LAS PIEDRAS", "coordenadas": {"latitud": -12.3, "longitud": -69.5}},
                    {"id": "170104", "nombre": "LABERINTO", "coordenadas": {"latitud": -12.2, "longitud": -69.3}}
                ]
            },
            {
                "id": "1702",
                "nombre": "MANU",
                "coordenadas": {"latitud": -12.2, "longitud": -70.9},
                "distritos": [
                    {"id": "170201", "nombre": "MANU", "coordenadas": {"latitud": -12.2, "longitud": -70.9}},
                    {"id": "170202", "nombre": "FITZCARRALD", "coordenadas": {"latitud": -11.8, "longitud": -71.3}},
                    {"id": "170203", "nombre": "MADRE DE DIOS", "coordenadas": {"latitud": -11.7, "longitud": -71.5}},
                    {"id": "170204", "nombre": "HUEPETUHE", "coordenadas": {"latitud": -12.0, "longitud": -70.7}}
                ]
            },
            {
                "id": "1703",
                "nombre": "TAHUAMANU",
                "coordenadas": {"latitud": -11.0, "longitud": -69.5},
                "distritos": [
                    {"id": "170301", "nombre": "IÑAPARI", "coordenadas": {"latitud": -11.0, "longitud": -69.5}},
                    {"id": "170302", "nombre": "IBERIA", "coordenadas": {"latitud": -11.3, "longitud": -69.3}},
                    {"id": "170303", "nombre": "TAHUAMANU", "coordenadas": {"latitud": -10.8, "longitud": -69.7}}
                ]
            }
        ]
    },
    "18": {  # MOQUEGUA
        "id": "18",
        "nombre": "MOQUEGUA",
        "coordenadas": {"latitud": -17.2, "longitud": -70.9333},
        "provincias": [
            {
                "id": "1801",
                "nombre": "MARISCAL NIETO",
                "coordenadas": {"latitud": -17.2, "longitud": -70.9333},
                "distritos": [
                    {"id": "180101", "nombre": "MOQUEGUA", "coordenadas": {"latitud": -17.2, "longitud": -70.9333}},
                    {"id": "180102", "nombre": "CARUMAS", "coordenadas": {"latitud": -16.8, "longitud": -70.7}},
                    {"id": "180103", "nombre": "CUCHUMBAYA", "coordenadas": {"latitud": -16.9, "longitud": -70.8}},
                    {"id": "180104", "nombre": "SAN CRISTOBAL", "coordenadas": {"latitud": -17.0, "longitud": -70.9}},
                    {"id": "180105", "nombre": "TORATA", "coordenadas": {"latitud": -17.1, "longitud": -70.8}},
                    {"id": "180106", "nombre": "SAMEGUA", "coordenadas": {"latitud": -17.2, "longitud": -70.8}}
                ]
            },
            {
                "id": "1802",
                "nombre": "GENERAL SANCHEZ CERRO",
                "coordenadas": {"latitud": -16.5, "longitud": -70.8},
                "distritos": [
                    {"id": "180201", "nombre": "OMATE", "coordenadas": {"latitud": -16.5, "longitud": -70.8}},
                    {"id": "180202", "nombre": "CHOJATA", "coordenadas": {"latitud": -16.4, "longitud": -70.7}},
                    {"id": "180203", "nombre": "COALAQUE", "coordenadas": {"latitud": -16.6, "longitud": -70.9}},
                    {"id": "180204", "nombre": "ICHUÑA", "coordenadas": {"latitud": -16.3, "longitud": -70.9}},
                    {"id": "180205", "nombre": "LA CAPILLA", "coordenadas": {"latitud": -16.7, "longitud": -70.7}},
                    {"id": "180206", "nombre": "LLOQUE", "coordenadas": {"latitud": -16.4, "longitud": -70.8}},
                    {"id": "180207", "nombre": "MATALAQUE", "coordenadas": {"latitud": -16.6, "longitud": -70.8}},
                    {"id": "180208", "nombre": "PUQUINA", "coordenadas": {"latitud": -16.5, "longitud": -70.9}},
                    {"id": "180209", "nombre": "QUINISTAQUILLAS", "coordenadas": {"latitud": -16.3, "longitud": -70.7}},
                    {"id": "180210", "nombre": "UBINAS", "coordenadas": {"latitud": -16.7, "longitud": -70.9}},
                    {"id": "180211", "nombre": "YUNGA", "coordenadas": {"latitud": -16.4, "longitud": -70.9}}
                ]
            },
            {
                "id": "1803",
                "nombre": "ILO",
                "coordenadas": {"latitud": -17.6333, "longitud": -71.3333},
                "distritos": [
                    {"id": "180301", "nombre": "ILO", "coordenadas": {"latitud": -17.6333, "longitud": -71.3333}},
                    {"id": "180302", "nombre": "EL ALGARROBAL", "coordenadas": {"latitud": -17.7, "longitud": -71.3}},
                    {"id": "180303", "nombre": "PACOCHA", "coordenadas": {"latitud": -17.6, "longitud": -71.4}}
                ]
            }
        ]
    },
    "19": {  # PASCO
        "id": "19",
        "nombre": "PASCO",
        "coordenadas": {"latitud": -10.6833, "longitud": -76.2667},
        "provincias": [
            {
                "id": "1901",
                "nombre": "PASCO",
                "coordenadas": {"latitud": -10.6833, "longitud": -76.2667},
                "distritos": [
                    {"id": "190101", "nombre": "CHAUPIMARCA", "coordenadas": {"latitud": -10.6833, "longitud": -76.2667}},
                    {"id": "190102", "nombre": "HUACHON", "coordenadas": {"latitud": -10.5, "longitud": -76.3}},
                    {"id": "190103", "nombre": "HUARIACA", "coordenadas": {"latitud": -10.6, "longitud": -76.2}},
                    {"id": "190104", "nombre": "HUAYLLAY", "coordenadas": {"latitud": -10.7, "longitud": -76.3}},
                    {"id": "190105", "nombre": "NINACACA", "coordenadas": {"latitud": -10.8, "longitud": -76.2}},
                    {"id": "190106", "nombre": "PALLANCHACRA", "coordenadas": {"latitud": -10.6, "longitud": -76.1}},
                    {"id": "190107", "nombre": "PAUCARTAMBO", "coordenadas": {"latitud": -10.7, "longitud": -76.1}},
                    {"id": "190108", "nombre": "SAN FRANCISCO DE ASIS DE YARUSYACAN", "coordenadas": {"latitud": -10.5, "longitud": -76.1}},
                    {"id": "190109", "nombre": "SIMON BOLIVAR", "coordenadas": {"latitud": -10.8, "longitud": -76.3}},
                    {"id": "190110", "nombre": "TICLACAYAN", "coordenadas": {"latitud": -10.6, "longitud": -76.4}},
                    {"id": "190111", "nombre": "TINYAHUARCO", "coordenadas": {"latitud": -10.7, "longitud": -76.4}},
                    {"id": "190112", "nombre": "VICCO", "coordenadas": {"latitud": -10.5, "longitud": -76.4}},
                    {"id": "190113", "nombre": "YANACANCHA", "coordenadas": {"latitud": -10.8, "longitud": -76.4}}
                ]
            },
            {
                "id": "1902",
                "nombre": "DANIEL ALCIDES CARRION",
                "coordenadas": {"latitud": -10.5, "longitud": -76.5},
                "distritos": [
                    {"id": "190201", "nombre": "YANAHUANCA", "coordenadas": {"latitud": -10.5, "longitud": -76.5}},
                    {"id": "190202", "nombre": "CHACAYAN", "coordenadas": {"latitud": -10.4, "longitud": -76.6}},
                    {"id": "190203", "nombre": "GOYLLARISQUIZGA", "coordenadas": {"latitud": -10.6, "longitud": -76.6}},
                    {"id": "190204", "nombre": "PAUCAR", "coordenadas": {"latitud": -10.3, "longitud": -76.5}},
                    {"id": "190205", "nombre": "SAN PEDRO DE PILLAO", "coordenadas": {"latitud": -10.4, "longitud": -76.4}},
                    {"id": "190206", "nombre": "SANTA ANA DE TUSI", "coordenadas": {"latitud": -10.3, "longitud": -76.4}},
                    {"id": "190207", "nombre": "TAPUC", "coordenadas": {"latitud": -10.6, "longitud": -76.5}},
                    {"id": "190208", "nombre": "VILCABAMBA", "coordenadas": {"latitud": -10.3, "longitud": -76.6}}
                ]
            },
            {
                "id": "1903",
                "nombre": "OXAPAMPA",
                "coordenadas": {"latitud": -10.5667, "longitud": -75.4},
                "distritos": [
                    {"id": "190301", "nombre": "OXAPAMPA", "coordenadas": {"latitud": -10.5667, "longitud": -75.4}},
                    {"id": "190302", "nombre": "CHONTABAMBA", "coordenadas": {"latitud": -10.5, "longitud": -75.3}},
                    {"id": "190303", "nombre": "HUANCABAMBA", "coordenadas": {"latitud": -10.6, "longitud": -75.3}},
                    {"id": "190304", "nombre": "PALCAZU", "coordenadas": {"latitud": -10.4, "longitud": -75.4}},
                    {"id": "190305", "nombre": "POZUZO", "coordenadas": {"latitud": -10.7, "longitud": -75.5}},
                    {"id": "190306", "nombre": "PUERTO BERMUDEZ", "coordenadas": {"latitud": -10.3, "longitud": -75.5}},
                    {"id": "190307", "nombre": "VILLA RICA", "coordenadas": {"latitud": -10.7, "longitud": -75.4}},
                    {"id": "190308", "nombre": "CONSTITUCION", "coordenadas": {"latitud": -10.4, "longitud": -75.3}}
                ]
            }
        ]
    },
    "20": {  # PIURA
        "id": "20",
        "nombre": "PIURA",
        "coordenadas": {"latitud": -5.2, "longitud": -80.6333},
        "provincias": [
            {
                "id": "2001",
                "nombre": "PIURA",
                "coordenadas": {"latitud": -5.2, "longitud": -80.6333},
                "distritos": [
                    {"id": "200101", "nombre": "PIURA", "coordenadas": {"latitud": -5.2, "longitud": -80.6333}},
                    {"id": "200104", "nombre": "CASTILLA", "coordenadas": {"latitud": -5.2, "longitud": -80.6}},
                    {"id": "200105", "nombre": "CATACAOS", "coordenadas": {"latitud": -5.3, "longitud": -80.7}},
                    {"id": "200107", "nombre": "CURA MORI", "coordenadas": {"latitud": -5.1, "longitud": -80.7}},
                    {"id": "200108", "nombre": "EL TALLAN", "coordenadas": {"latitud": -5.3, "longitud": -80.6}},
                    {"id": "200109", "nombre": "LA ARENA", "coordenadas": {"latitud": -5.2, "longitud": -80.8}},
                    {"id": "200110", "nombre": "LA UNION", "coordenadas": {"latitud": -5.1, "longitud": -80.6}},
                    {"id": "200111", "nombre": "LAS LOMAS", "coordenadas": {"latitud": -5.3, "longitud": -80.5}},
                    {"id": "200114", "nombre": "TAMBO GRANDE", "coordenadas": {"latitud": -5.1, "longitud": -80.5}},
                    {"id": "200115", "nombre": "VEINTISEIS DE OCTUBRE", "coordenadas": {"latitud": -5.2, "longitud": -80.5}}
                ]
            },
            {
                "id": "2002",
                "nombre": "AYABACA",
                "coordenadas": {"latitud": -4.6333, "longitud": -79.7167},
                "distritos": [
                    {"id": "200201", "nombre": "AYABACA", "coordenadas": {"latitud": -4.6333, "longitud": -79.7167}},
                    {"id": "200202", "nombre": "FRIAS", "coordenadas": {"latitud": -4.7, "longitud": -79.8}},
                    {"id": "200203", "nombre": "JILILI", "coordenadas": {"latitud": -4.6, "longitud": -79.8}},
                    {"id": "200204", "nombre": "LAGUNAS", "coordenadas": {"latitud": -4.5, "longitud": -79.7}},
                    {"id": "200205", "nombre": "MONTERO", "coordenadas": {"latitud": -4.7, "longitud": -79.7}},
                    {"id": "200206", "nombre": "PACAIPAMPA", "coordenadas": {"latitud": -4.6, "longitud": -79.6}},
                    {"id": "200207", "nombre": "PAIMAS", "coordenadas": {"latitud": -4.5, "longitud": -79.8}},
                    {"id": "200208", "nombre": "SAPILLICA", "coordenadas": {"latitud": -4.7, "longitud": -79.6}},
                    {"id": "200209", "nombre": "SICCHEZ", "coordenadas": {"latitud": -4.6, "longitud": -79.5}},
                    {"id": "200210", "nombre": "SUYO", "coordenadas": {"latitud": -4.5, "longitud": -79.9}}
                ]
            },
            {
                "id": "2003",
                "nombre": "HUANCABAMBA",
                "coordenadas": {"latitud": -5.2333, "longitud": -79.45},
                "distritos": [
                    {"id": "200301", "nombre": "HUANCABAMBA", "coordenadas": {"latitud": -5.2333, "longitud": -79.45}},
                    {"id": "200302", "nombre": "CANCHAQUE", "coordenadas": {"latitud": -5.3, "longitud": -79.5}},
                    {"id": "200303", "nombre": "EL CARMEN DE LA FRONTERA", "coordenadas": {"latitud": -5.2, "longitud": -79.4}},
                    {"id": "200304", "nombre": "HUARMACA", "coordenadas": {"latitud": -5.1, "longitud": -79.5}},
                    {"id": "200305", "nombre": "LALAQUIZ", "coordenadas": {"latitud": -5.3, "longitud": -79.4}},
                    {"id": "200306", "nombre": "SAN MIGUEL DE EL FAIQUE", "coordenadas": {"latitud": -5.2, "longitud": -79.3}},
                    {"id": "200307", "nombre": "SONDOR", "coordenadas": {"latitud": -5.1, "longitud": -79.4}},
                    {"id": "200308", "nombre": "SONDORILLO", "coordenadas": {"latitud": -5.3, "longitud": -79.3}}
                ]
            },
            {
                "id": "2004",
                "nombre": "MORROPON",
                "coordenadas": {"latitud": -5.1833, "longitud": -79.9667},
                "distritos": [
                    {"id": "200401", "nombre": "CHULUCANAS", "coordenadas": {"latitud": -5.1833, "longitud": -79.9667}},
                    {"id": "200402", "nombre": "BUENOS AIRES", "coordenadas": {"latitud": -5.1, "longitud": -80.0}},
                    {"id": "200403", "nombre": "CHALACO", "coordenadas": {"latitud": -5.2, "longitud": -79.9}},
                    {"id": "200404", "nombre": "LA MATANZA", "coordenadas": {"latitud": -5.1, "longitud": -79.9}},
                    {"id": "200405", "nombre": "MORROPON", "coordenadas": {"latitud": -5.2, "longitud": -80.0}},
                    {"id": "200406", "nombre": "SALITRAL", "coordenadas": {"latitud": -5.3, "longitud": -80.0}},
                    {"id": "200407", "nombre": "SAN JUAN DE BIGOTE", "coordenadas": {"latitud": -5.1, "longitud": -80.1}},
                    {"id": "200408", "nombre": "SANTA CATALINA DE MOSSA", "coordenadas": {"latitud": -5.2, "longitud": -80.1}},
                    {"id": "200409", "nombre": "SANTO DOMINGO", "coordenadas": {"latitud": -5.3, "longitud": -80.1}},
                    {"id": "200410", "nombre": "YAMANGO", "coordenadas": {"latitud": -5.2, "longitud": -79.8}}
                ]
            },
            {
                "id": "2005",
                "nombre": "PAITA",
                "coordenadas": {"latitud": -5.0833, "longitud": -81.1},
                "distritos": [
                    {"id": "200501", "nombre": "PAITA", "coordenadas": {"latitud": -5.0833, "longitud": -81.1}},
                    {"id": "200502", "nombre": "AMOTAPE", "coordenadas": {"latitud": -5.0, "longitud": -81.0}},
                    {"id": "200503", "nombre": "ARENAL", "coordenadas": {"latitud": -5.1, "longitud": -81.0}},
                    {"id": "200504", "nombre": "COLAN", "coordenadas": {"latitud": -5.0, "longitud": -81.1}},
                    {"id": "200505", "nombre": "LA HUACA", "coordenadas": {"latitud": -5.1, "longitud": -81.1}},
                    {"id": "200506", "nombre": "TAMARINDO", "coordenadas": {"latitud": -5.0, "longitud": -81.2}},
                    {"id": "200507", "nombre": "VICHAYAL", "coordenadas": {"latitud": -5.1, "longitud": -81.2}}
                ]
            },
            {
                "id": "2006",
                "nombre": "SULLANA",
                "coordenadas": {"latitud": -4.9, "longitud": -80.6833},
                "distritos": [
                    {"id": "200601", "nombre": "SULLANA", "coordenadas": {"latitud": -4.9, "longitud": -80.6833}},
                    {"id": "200602", "nombre": "BELLAVISTA", "coordenadas": {"latitud": -4.8, "longitud": -80.7}},
                    {"id": "200603", "nombre": "IGNACIO ESCUDERO", "coordenadas": {"latitud": -4.9, "longitud": -80.8}},
                    {"id": "200604", "nombre": "LANCONES", "coordenadas": {"latitud": -4.8, "longitud": -80.8}},
                    {"id": "200605", "nombre": "MARCAVELICA", "coordenadas": {"latitud": -4.9, "longitud": -80.6}},
                    {"id": "200606", "nombre": "MIGUEL CHECA", "coordenadas": {"latitud": -4.8, "longitud": -80.6}},
                    {"id": "200607", "nombre": "QUERECOTILLO", "coordenadas": {"latitud": -4.9, "longitud": -80.5}},
                    {"id": "200608", "nombre": "SALITRAL", "coordenadas": {"latitud": -4.8, "longitud": -80.5}}
                ]
            },
            {
                "id": "2007",
                "nombre": "TALARA",
                "coordenadas": {"latitud": -4.5833, "longitud": -81.2667},
                "distritos": [
                    {"id": "200701", "nombre": "PARIÑAS", "coordenadas": {"latitud": -4.5833, "longitud": -81.2667}},
                    {"id": "200702", "nombre": "EL ALTO", "coordenadas": {"latitud": -4.5, "longitud": -81.2}},
                    {"id": "200703", "nombre": "LA BREA", "coordenadas": {"latitud": -4.6, "longitud": -81.2}},
                    {"id": "200704", "nombre": "LOBITOS", "coordenadas": {"latitud": -4.5, "longitud": -81.3}},
                    {"id": "200705", "nombre": "LOS ORGANOS", "coordenadas": {"latitud": -4.6, "longitud": -81.3}},
                    {"id": "200706", "nombre": "MANCORA", "coordenadas": {"latitud": -4.5, "longitud": -81.4}}
                ]
            },
            {
                "id": "2008",
                "nombre": "SECHURA",
                "coordenadas": {"latitud": -5.5667, "longitud": -80.8167},
                "distritos": [
                    {"id": "200801", "nombre": "SECHURA", "coordenadas": {"latitud": -5.5667, "longitud": -80.8167}},
                    {"id": "200802", "nombre": "BELLAVISTA DE LA UNION", "coordenadas": {"latitud": -5.5, "longitud": -80.8}},
                    {"id": "200803", "nombre": "BERNAL", "coordenadas": {"latitud": -5.6, "longitud": -80.9}},
                    {"id": "200804", "nombre": "CRISTO NOS VALGA", "coordenadas": {"latitud": -5.5, "longitud": -80.9}},
                    {"id": "200805", "nombre": "VICE", "coordenadas": {"latitud": -5.6, "longitud": -80.7}},
                    {"id": "200806", "nombre": "RINCONADA LLICUAR", "coordenadas": {"latitud": -5.5, "longitud": -80.7}}
                ]
            }
        ]
    },
    "21": {  # PUNO
        "id": "21",
        "nombre": "PUNO",
        "coordenadas": {"latitud": -15.8333, "longitud": -70.0333},
        "provincias": [
            {
                "id": "2101",
                "nombre": "PUNO",
                "coordenadas": {"latitud": -15.8333, "longitud": -70.0333},
                "distritos": [
                    {"id": "210101", "nombre": "PUNO", "coordenadas": {"latitud": -15.8333, "longitud": -70.0333}},
                    {"id": "210102", "nombre": "ACORA", "coordenadas": {"latitud": -16.0, "longitud": -69.8333}},
                    {"id": "210103", "nombre": "AMANTANI", "coordenadas": {"latitud": -15.6667, "longitud": -69.6667}},
                    {"id": "210104", "nombre": "ATUNCOLLA", "coordenadas": {"latitud": -15.7, "longitud": -70.15}},
                    {"id": "210105", "nombre": "CAPACHICA", "coordenadas": {"latitud": -15.6333, "longitud": -69.8333}},
                    {"id": "210106", "nombre": "CHUCUITO", "coordenadas": {"latitud": -16.2, "longitud": -69.5}},
                    {"id": "210107", "nombre": "COATA", "coordenadas": {"latitud": -15.5667, "longitud": -70.0333}},
                    {"id": "210108", "nombre": "HUATA", "coordenadas": {"latitud": -15.5, "longitud": -70.15}},
                    {"id": "210109", "nombre": "MAÑAZO", "coordenadas": {"latitud": -15.7, "longitud": -70.25}},
                    {"id": "210110", "nombre": "PAUCARCOLLA", "coordenadas": {"latitud": -15.7, "longitud": -70.0333}},
                    {"id": "210111", "nombre": "PICHACANI", "coordenadas": {"latitud": -15.8, "longitud": -70.15}},
                    {"id": "210112", "nombre": "PLATERIA", "coordenadas": {"latitud": -15.7333, "longitud": -70.15}},
                    {"id": "210113", "nombre": "SAN ANTONIO", "coordenadas": {"latitud": -15.8, "longitud": -70.25}},
                    {"id": "210114", "nombre": "TIQUILLACA", "coordenadas": {"latitud": -15.8, "longitud": -70.15}},
                    {"id": "210115", "nombre": "VILQUE", "coordenadas": {"latitud": -15.9, "longitud": -70.15}}
                ]
            },
            {
                "id": "2102",
                "nombre": "AZANGARO",
                "coordenadas": {"latitud": -14.9167, "longitud": -70.2},
                "distritos": [
                    {"id": "210201", "nombre": "AZANGARO", "coordenadas": {"latitud": -14.9167, "longitud": -70.2}},
                    {"id": "210202", "nombre": "ACHAYA", "coordenadas": {"latitud": -14.8333, "longitud": -70.25}},
                    {"id": "210203", "nombre": "ARAPA", "coordenadas": {"latitud": -15.0, "longitud": -70.15}},
                    {"id": "210204", "nombre": "ASILLO", "coordenadas": {"latitud": -14.8333, "longitud": -70.15}},
                    {"id": "210205", "nombre": "CAMINACA", "coordenadas": {"latitud": -14.75, "longitud": -70.2}},
                    {"id": "210206", "nombre": "CHUPA", "coordenadas": {"latitud": -14.8333, "longitud": -70.1}},
                    {"id": "210207", "nombre": "JOSE DOMINGO CHOQUEHUANCA", "coordenadas": {"latitud": -14.9167, "longitud": -70.1}},
                    {"id": "210208", "nombre": "MUÑANI", "coordenadas": {"latitud": -14.75, "longitud": -70.15}},
                    {"id": "210209", "nombre": "POTONI", "coordenadas": {"latitud": -14.9167, "longitud": -70.3}},
                    {"id": "210210", "nombre": "SAMAN", "coordenadas": {"latitud": -14.8333, "longitud": -70.3}},
                    {"id": "210211", "nombre": "SAN ANTON", "coordenadas": {"latitud": -14.75, "longitud": -70.25}},
                    {"id": "210212", "nombre": "SAN JOSE", "coordenadas": {"latitud": -14.9167, "longitud": -70.25}},
                    {"id": "210213", "nombre": "SAN JUAN DE SALINAS", "coordenadas": {"latitud": -14.8333, "longitud": -70.2}},
                    {"id": "210214", "nombre": "SANTIAGO DE PUPUJA", "coordenadas": {"latitud": -14.75, "longitud": -70.1}},
                    {"id": "210215", "nombre": "TIRAPATA", "coordenadas": {"latitud": -14.9167, "longitud": -70.15}}
                ]
            },
            {
                "id": "2103",
                "nombre": "CARABAYA",
                "coordenadas": {"latitud": -13.8333, "longitud": -70.25},
                "distritos": [
                    {"id": "210301", "nombre": "MACUSANI", "coordenadas": {"latitud": -13.8333, "longitud": -70.25}},
                    {"id": "210302", "nombre": "AJOYANI", "coordenadas": {"latitud": -14.0, "longitud": -70.5}},
                    {"id": "210303", "nombre": "AYAPATA", "coordenadas": {"latitud": -13.9167, "longitud": -70.5}},
                    {"id": "210304", "nombre": "COASA", "coordenadas": {"latitud": -13.75, "longitud": -70.5}},
                    {"id": "210305", "nombre": "CORANI", "coordenadas": {"latitud": -13.9167, "longitud": -70.25}},
                    {"id": "210306", "nombre": "CRUCERO", "coordenadas": {"latitud": -13.75, "longitud": -70.25}},
                    {"id": "210307", "nombre": "ITUATA", "coordenadas": {"latitud": -13.8333, "longitud": -70.5}},
                    {"id": "210308", "nombre": "OLLACHEA", "coordenadas": {"latitud": -13.9167, "longitud": -70.75}},
                    {"id": "210309", "nombre": "SAN GABAN", "coordenadas": {"latitud": -13.75, "longitud": -70.75}},
                    {"id": "210310", "nombre": "USICAYOS", "coordenadas": {"latitud": -13.8333, "longitud": -70.75}}
                ]
            },
            {
                "id": "2104",
                "nombre": "CHUCUITO",
                "coordenadas": {"latitud": -16.2, "longitud": -69.5},
                "distritos": [
                    {"id": "210401", "nombre": "JULI", "coordenadas": {"latitud": -16.2, "longitud": -69.5}},
                    {"id": "210402", "nombre": "DESAGUADERO", "coordenadas": {"latitud": -16.5667, "longitud": -69.0333}},
                    {"id": "210403", "nombre": "HUACULLANI", "coordenadas": {"latitud": -16.3, "longitud": -69.4}},
                    {"id": "210404", "nombre": "KELLUYO", "coordenadas": {"latitud": -16.7333, "longitud": -69.1}},
                    {"id": "210405", "nombre": "PISACOMA", "coordenadas": {"latitud": -16.8333, "longitud": -69.2}},
                    {"id": "210406", "nombre": "POMATA", "coordenadas": {"latitud": -16.2667, "longitud": -69.3}},
                    {"id": "210407", "nombre": "ZEPITA", "coordenadas": {"latitud": -16.5, "longitud": -69.1}}
                ]
            },
            {
                "id": "2105",
                "nombre": "EL COLLAO",
                "coordenadas": {"latitud": -16.0, "longitud": -69.6667},
                "distritos": [
                    {"id": "210501", "nombre": "ILAVE", "coordenadas": {"latitud": -16.0, "longitud": -69.6667}},
                    {"id": "210502", "nombre": "CAPAZO", "coordenadas": {"latitud": -16.1, "longitud": -69.75}},
                    {"id": "210503", "nombre": "PILCUYO", "coordenadas": {"latitud": -15.9167, "longitud": -69.75}},
                    {"id": "210504", "nombre": "SANTA ROSA", "coordenadas": {"latitud": -16.0833, "longitud": -69.5833}},
                    {"id": "210505", "nombre": "CONDURIRI", "coordenadas": {"latitud": -15.9167, "longitud": -69.5833}}
                ]
            },
            {
                "id": "2106",
                "nombre": "HUANCANE",
                "coordenadas": {"latitud": -15.2, "longitud": -69.75},
                "distritos": [
                    {"id": "210601", "nombre": "HUANCANE", "coordenadas": {"latitud": -15.2, "longitud": -69.75}},
                    {"id": "210602", "nombre": "COJATA", "coordenadas": {"latitud": -15.0833, "longitud": -69.8333}},
                    {"id": "210603", "nombre": "HUATASANI", "coordenadas": {"latitud": -15.25, "longitud": -69.8333}},
                    {"id": "210604", "nombre": "INCHUPALLA", "coordenadas": {"latitud": -15.1667, "longitud": -69.6667}},
                    {"id": "210605", "nombre": "PUSI", "coordenadas": {"latitud": -15.25, "longitud": -69.6667}},
                    {"id": "210606", "nombre": "ROSASPATA", "coordenadas": {"latitud": -15.0833, "longitud": -69.6667}},
                    {"id": "210607", "nombre": "TARACO", "coordenadas": {"latitud": -15.1667, "longitud": -69.8333}},
                    {"id": "210608", "nombre": "VILQUE CHICO", "coordenadas": {"latitud": -15.25, "longitud": -69.75}}
                ]
            },
            {
                "id": "2107",
                "nombre": "LAMPA",
                "coordenadas": {"latitud": -15.35, "longitud": -70.3667},
                "distritos": [
                    {"id": "210701", "nombre": "LAMPA", "coordenadas": {"latitud": -15.35, "longitud": -70.3667}},
                    {"id": "210702", "nombre": "CABANILLA", "coordenadas": {"latitud": -15.5, "longitud": -70.25}},
                    {"id": "210703", "nombre": "CALAPUJA", "coordenadas": {"latitud": -15.25, "longitud": -70.25}},
                    {"id": "210704", "nombre": "NICASIO", "coordenadas": {"latitud": -15.4167, "longitud": -70.25}},
                    {"id": "210705", "nombre": "OCUVIRI", "coordenadas": {"latitud": -15.3333, "longitud": -70.5}},
                    {"id": "210706", "nombre": "PALCA", "coordenadas": {"latitud": -15.5, "longitud": -70.5}},
                    {"id": "210707", "nombre": "PARATIA", "coordenadas": {"latitud": -15.4167, "longitud": -70.5}},
                    {"id": "210708", "nombre": "PUCARA", "coordenadas": {"latitud": -15.25, "longitud": -70.5}},
                    {"id": "210709", "nombre": "SANTA LUCIA", "coordenadas": {"latitud": -15.3333, "longitud": -70.25}},
                    {"id": "210710", "nombre": "VILAVILA", "coordenadas": {"latitud": -15.4167, "longitud": -70.25}}
                ]
            },
            {
                "id": "2108",
                "nombre": "MELGAR",
                "coordenadas": {"latitud": -14.8333, "longitud": -70.9167},
                "distritos": [
                    {"id": "210801", "nombre": "AYAVIRI", "coordenadas": {"latitud": -14.8333, "longitud": -70.9167}},
                    {"id": "210802", "nombre": "ANTAUTA", "coordenadas": {"latitud": -14.75, "longitud": -70.8333}},
                    {"id": "210803", "nombre": "CALLANCA", "coordenadas": {"latitud": -14.9167, "longitud": -70.8333}},
                    {"id": "210804", "nombre": "CUPI", "coordenadas": {"latitud": -14.75, "longitud": -70.9167}},
                    {"id": "210805", "nombre": "LLALLI", "coordenadas": {"latitud": -14.9167, "longitud": -70.9167}},
                    {"id": "210806", "nombre": "MACARI", "coordenadas": {"latitud": -14.8333, "longitud": -70.8333}},
                    {"id": "210807", "nombre": "NUÑOA", "coordenadas": {"latitud": -14.75, "longitud": -70.75}},
                    {"id": "210808", "nombre": "ORURILLO", "coordenadas": {"latitud": -14.9167, "longitud": -70.75}},
                    {"id": "210809", "nombre": "SANTA ROSA", "coordenadas": {"latitud": -14.8333, "longitud": -70.75}},
                    {"id": "210810", "nombre": "UMACHIRI", "coordenadas": {"latitud": -14.9167, "longitud": -70.6667}}
                ]
            },
            {
                "id": "2109",
                "nombre": "MOHO",
                "coordenadas": {"latitud": -15.3333, "longitud": -69.5},
                "distritos": [
                    {"id": "210901", "nombre": "MOHO", "coordenadas": {"latitud": -15.3333, "longitud": -69.5}},
                    {"id": "210902", "nombre": "CONIMA", "coordenadas": {"latitud": -15.25, "longitud": -69.4167}},
                    {"id": "210903", "nombre": "HUAYRAPATA", "coordenadas": {"latitud": -15.4167, "longitud": -69.4167}},
                    {"id": "210904", "nombre": "TILALI", "coordenadas": {"latitud": -15.25, "longitud": -69.5}}
                ]
            },
            {
                "id": "2110",
                "nombre": "SAN ANTONIO DE PUTINA",
                "coordenadas": {"latitud": -14.9167, "longitud": -69.6667},
                "distritos": [
                    {"id": "211001", "nombre": "PUTINA", "coordenadas": {"latitud": -14.9167, "longitud": -69.6667}},
                    {"id": "211002", "nombre": "ANANEA", "coordenadas": {"latitud": -14.8333, "longitud": -69.5833}},
                    {"id": "211003", "nombre": "PEDRO VILCA APAZA", "coordenadas": {"latitud": -14.8333, "longitud": -69.75}},
                    {"id": "211004", "nombre": "QUILCAPUNCU", "coordenadas": {"latitud": -14.9167, "longitud": -69.75}},
                    {"id": "211005", "nombre": "SINA", "coordenadas": {"latitud": -14.9167, "longitud": -69.5833}}
                ]
            },
            {
                "id": "2111",
                "nombre": "SAN ROMAN",
                "coordenadas": {"latitud": -15.5, "longitud": -70.1333},
                "distritos": [
                    {"id": "211101", "nombre": "JULIACA", "coordenadas": {"latitud": -15.5, "longitud": -70.1333}},
                    {"id": "211102", "nombre": "CABANA", "coordenadas": {"latitud": -15.4167, "longitud": -70.0833}},
                    {"id": "211103", "nombre": "CABANILLAS", "coordenadas": {"latitud": -15.5833, "longitud": -70.0833}},
                    {"id": "211104", "nombre": "CARACOTO", "coordenadas": {"latitud": -15.4167, "longitud": -70.1667}}
                ]
            },
            {
                "id": "2112",
                "nombre": "SANDIA",
                "coordenadas": {"latitud": -14.25, "longitud": -69.4167},
                "distritos": [
                    {"id": "211201", "nombre": "SANDIA", "coordenadas": {"latitud": -14.25, "longitud": -69.4167}},
                    {"id": "211202", "nombre": "CUYOCUYO", "coordenadas": {"latitud": -14.3333, "longitud": -69.5}},
                    {"id": "211203", "nombre": "LIMBANI", "coordenadas": {"latitud": -14.1667, "longitud": -69.5}},
                    {"id": "211204", "nombre": "PATAMBUCO", "coordenadas": {"latitud": -14.3333, "longitud": -69.3333}},
                    {"id": "211205", "nombre": "PHARA", "coordenadas": {"latitud": -14.1667, "longitud": -69.3333}},
                    {"id": "211206", "nombre": "QUIACA", "coordenadas": {"latitud": -14.25, "longitud": -69.5}},
                    {"id": "211207", "nombre": "SAN JUAN DEL ORO", "coordenadas": {"latitud": -14.1667, "longitud": -69.4167}},
                    {"id": "211208", "nombre": "YANAHUAYA", "coordenadas": {"latitud": -14.3333, "longitud": -69.4167}},
                    {"id": "211209", "nombre": "ALTO INAMBARI", "coordenadas": {"latitud": -14.25, "longitud": -69.3333}}
                ]
            },
            {
                "id": "2113",
                "nombre": "YUNGUYO",
                "coordenadas": {"latitud": -16.25, "longitud": -69.0833},
                "distritos": [
                    {"id": "211301", "nombre": "YUNGUYO", "coordenadas": {"latitud": -16.25, "longitud": -69.0833}},
                    {"id": "211302", "nombre": "ANAPIA", "coordenadas": {"latitud": -16.1667, "longitud": -69.1667}},
                    {"id": "211303", "nombre": "COPANI", "coordenadas": {"latitud": -16.3333, "longitud": -69.1667}},
                    {"id": "211304", "nombre": "CUTTURANI", "coordenadas": {"latitud": -16.1667, "longitud": -69.0833}},
                    {"id": "211305", "nombre": "OLLARAYA", "coordenadas": {"latitud": -16.3333, "longitud": -69.0833}},
                    {"id": "211306", "nombre": "TINICACHI", "coordenadas": {"latitud": -16.25, "longitud": -69.1667}},
                    {"id": "211307", "nombre": "UNICACHI", "coordenadas": {"latitud": -16.25, "longitud": -69.0}}
                ]
            }
        ]
    },
    "22": {  # SAN MARTIN
        "id": "22",
        "nombre": "SAN MARTIN",
        "coordenadas": {"latitud": -6.5, "longitud": -76.3667},
        "provincias": [
            {
                "id": "2201",
                "nombre": "MOYOBAMBA",
                "coordenadas": {"latitud": -6.0333, "longitud": -76.9667},
                "distritos": [
                    {"id": "220101", "nombre": "MOYOBAMBA", "coordenadas": {"latitud": -6.0333, "longitud": -76.9667}},
                    {"id": "220102", "nombre": "CALZADA", "coordenadas": {"latitud": -6.0833, "longitud": -76.9167}},
                    {"id": "220103", "nombre": "HABANA", "coordenadas": {"latitud": -5.9167, "longitud": -76.9167}},
                    {"id": "220104", "nombre": "JEPELACIO", "coordenadas": {"latitud": -6.1167, "longitud": -76.9167}},
                    {"id": "220105", "nombre": "SORITOR", "coordenadas": {"latitud": -6.0, "longitud": -77.0833}},
                    {"id": "220106", "nombre": "YANTALO", "coordenadas": {"latitud": -6.1667, "longitud": -76.9167}}
                ]
            },
            {
                "id": "2202",
                "nombre": "BELLAVISTA",
                "coordenadas": {"latitud": -7.05, "longitud": -76.5833},
                "distritos": [
                    {"id": "220201", "nombre": "BELLAVISTA", "coordenadas": {"latitud": -7.05, "longitud": -76.5833}},
                    {"id": "220202", "nombre": "ALTO BIAVO", "coordenadas": {"latitud": -7.1667, "longitud": -76.5}},
                    {"id": "220203", "nombre": "BAJO BIAVO", "coordenadas": {"latitud": -7.0, "longitud": -76.5}},
                    {"id": "220204", "nombre": "HUALLAGA", "coordenadas": {"latitud": -7.0833, "longitud": -76.6667}},
                    {"id": "220205", "nombre": "SAN PABLO", "coordenadas": {"latitud": -7.0, "longitud": -76.6667}},
                    {"id": "220206", "nombre": "SAN RAFAEL", "coordenadas": {"latitud": -7.1667, "longitud": -76.6667}}
                ]
            },
            {
                "id": "2203",
                "nombre": "EL DORADO",
                "coordenadas": {"latitud": -6.5, "longitud": -76.3667},
                "distritos": [
                    {"id": "220301", "nombre": "SAN JOSE DE SISA", "coordenadas": {"latitud": -6.5, "longitud": -76.3667}},
                    {"id": "220302", "nombre": "AGUA BLANCA", "coordenadas": {"latitud": -6.5833, "longitud": -76.5}},
                    {"id": "220303", "nombre": "SAN MARTIN", "coordenadas": {"latitud": -6.4167, "longitud": -76.5}},
                    {"id": "220304", "nombre": "SANTA ROSA", "coordenadas": {"latitud": -6.5, "longitud": -76.25}},
                    {"id": "220305", "nombre": "SHATOJA", "coordenadas": {"latitud": -6.5833, "longitud": -76.25}}
                ]
            },
            {
                "id": "2204",
                "nombre": "HUALLAGA",
                "coordenadas": {"latitud": -6.9167, "longitud": -76.75},
                "distritos": [
                    {"id": "220401", "nombre": "SAPOSOA", "coordenadas": {"latitud": -6.9167, "longitud": -76.75}},
                    {"id": "220402", "nombre": "ALTO SAPOSOA", "coordenadas": {"latitud": -7.0, "longitud": -76.8333}},
                    {"id": "220403", "nombre": "EL ESLABON", "coordenadas": {"latitud": -6.8333, "longitud": -76.8333}},
                    {"id": "220404", "nombre": "PISCOYACU", "coordenadas": {"latitud": -7.0, "longitud": -76.6667}},
                    {"id": "220405", "nombre": "SACANCHE", "coordenadas": {"latitud": -6.8333, "longitud": -76.6667}},
                    {"id": "220406", "nombre": "TINGO DE SAPOSOA", "coordenadas": {"latitud": -6.9167, "longitud": -76.8333}}
                ]
            },
            {
                "id": "2205",
                "nombre": "LAMAS",
                "coordenadas": {"latitud": -6.4167, "longitud": -76.5333},
                "distritos": [
                    {"id": "220501", "nombre": "LAMAS", "coordenadas": {"latitud": -6.4167, "longitud": -76.5333}},
                    {"id": "220502", "nombre": "ALONSO DE ALVARADO", "coordenadas": {"latitud": -6.5, "longitud": -76.6667}},
                    {"id": "220503", "nombre": "BARRANQUITA", "coordenadas": {"latitud": -6.3333, "longitud": -76.6667}},
                    {"id": "220504", "nombre": "CAYNARACHI", "coordenadas": {"latitud": -6.5, "longitud": -76.4167}},
                    {"id": "220505", "nombre": "CUÑUMBUQUI", "coordenadas": {"latitud": -6.3333, "longitud": -76.4167}},
                    {"id": "220506", "nombre": "PINTO RECODO", "coordenadas": {"latitud": -6.4167, "longitud": -76.6667}},
                    {"id": "220507", "nombre": "RUMISAPA", "coordenadas": {"latitud": -6.4167, "longitud": -76.4167}},
                    {"id": "220508", "nombre": "SAN ROQUE DE CUMBAZA", "coordenadas": {"latitud": -6.5, "longitud": -76.5333}},
                    {"id": "220509", "nombre": "SHANAO", "coordenadas": {"latitud": -6.3333, "longitud": -76.5333}},
                    {"id": "220510", "nombre": "TABALOSOS", "coordenadas": {"latitud": -6.4167, "longitud": -76.5833}},
                    {"id": "220511", "nombre": "ZAPATERO", "coordenadas": {"latitud": -6.3333, "longitud": -76.5833}}
                ]
            },
            {
                "id": "2206",
                "nombre": "MARISCAL CACERES",
                "coordenadas": {"latitud": -7.3333, "longitud": -76.75},
                "distritos": [
                    {"id": "220601", "nombre": "JUANJUI", "coordenadas": {"latitud": -7.3333, "longitud": -76.75}},
                    {"id": "220602", "nombre": "CAMPANILLA", "coordenadas": {"latitud": -7.25, "longitud": -76.8333}},
                    {"id": "220603", "nombre": "HUICUNGO", "coordenadas": {"latitud": -7.4167, "longitud": -76.8333}},
                    {"id": "220604", "nombre": "PACHIZA", "coordenadas": {"latitud": -7.25, "longitud": -76.6667}},
                    {"id": "220605", "nombre": "PAJARILLO", "coordenadas": {"latitud": -7.4167, "longitud": -76.6667}}
                ]
            },
            {
                "id": "2207",
                "nombre": "PICOTA",
                "coordenadas": {"latitud": -6.9167, "longitud": -76.3333},
                "distritos": [
                    {"id": "220701", "nombre": "PICOTA", "coordenadas": {"latitud": -6.9167, "longitud": -76.3333}},
                    {"id": "220702", "nombre": "BUENOS AIRES", "coordenadas": {"latitud": -7.0, "longitud": -76.4167}},
                    {"id": "220703", "nombre": "CASPISAPA", "coordenadas": {"latitud": -6.8333, "longitud": -76.4167}},
                    {"id": "220704", "nombre": "PILLUANA", "coordenadas": {"latitud": -7.0, "longitud": -76.25}},
                    {"id": "220705", "nombre": "PUCACACA", "coordenadas": {"latitud": -6.8333, "longitud": -76.25}},
                    {"id": "220706", "nombre": "SAN CRISTOBAL", "coordenadas": {"latitud": -6.9167, "longitud": -76.4167}},
                    {"id": "220707", "nombre": "SAN HILARION", "coordenadas": {"latitud": -6.9167, "longitud": -76.25}},
                    {"id": "220708", "nombre": "SHAMBOYACU", "coordenadas": {"latitud": -7.0, "longitud": -76.3333}},
                    {"id": "220709", "nombre": "TINGO DE PONASA", "coordenadas": {"latitud": -6.8333, "longitud": -76.3333}},
                    {"id": "220710", "nombre": "TRES UNIDOS", "coordenadas": {"latitud": -6.9167, "longitud": -76.1667}}
                ]
            },
            {
                "id": "2208",
                "nombre": "RIOJA",
                "coordenadas": {"latitud": -6.05, "longitud": -77.1667},
                "distritos": [
                    {"id": "220801", "nombre": "RIOJA", "coordenadas": {"latitud": -6.05, "longitud": -77.1667}},
                    {"id": "220802", "nombre": "AWAJUN", "coordenadas": {"latitud": -5.9167, "longitud": -77.25}},
                    {"id": "220803", "nombre": "ELIAS SOPLIN VARGAS", "coordenadas": {"latitud": -6.1667, "longitud": -77.25}},
                    {"id": "220804", "nombre": "NUEVA CAJAMARCA", "coordenadas": {"latitud": -5.9167, "longitud": -77.1667}},
                    {"id": "220805", "nombre": "PARDO MIGUEL", "coordenadas": {"latitud": -6.1667, "longitud": -77.1667}},
                    {"id": "220806", "nombre": "POSIC", "coordenadas": {"latitud": -6.05, "longitud": -77.25}},
                    {"id": "220807", "nombre": "SAN FERNANDO", "coordenadas": {"latitud": -6.05, "longitud": -77.0833}},
                    {"id": "220808", "nombre": "YORONGOS", "coordenadas": {"latitud": -6.1667, "longitud": -77.0833}},
                    {"id": "220809", "nombre": "YURACYACU", "coordenadas": {"latitud": -5.9167, "longitud": -77.0833}}
                ]
            },
            {
                "id": "2209",
                "nombre": "SAN MARTIN",
                "coordenadas": {"latitud": -6.5, "longitud": -76.3667},
                "distritos": [
                    {"id": "220901", "nombre": "TARAPOTO", "coordenadas": {"latitud": -6.5, "longitud": -76.3667}},
                    {"id": "220902", "nombre": "ALBERTO LEVEAU", "coordenadas": {"latitud": -6.5833, "longitud": -76.5}},
                    {"id": "220903", "nombre": "CACATACHI", "coordenadas": {"latitud": -6.4167, "longitud": -76.5}},
                    {"id": "220904", "nombre": "CHAZUTA", "coordenadas": {"latitud": -6.5833, "longitud": -76.25}},
                    {"id": "220905", "nombre": "CHIPURANA", "coordenadas": {"latitud": -6.4167, "longitud": -76.25}},
                    {"id": "220906", "nombre": "EL PORVENIR", "coordenadas": {"latitud": -6.5, "longitud": -76.5}},
                    {"id": "220907", "nombre": "HUIMBAYOC", "coordenadas": {"latitud": -6.5, "longitud": -76.25}},
                    {"id": "220908", "nombre": "JUAN GUERRA", "coordenadas": {"latitud": -6.5833, "longitud": -76.3667}},
                    {"id": "220909", "nombre": "LA BANDA DE SHILCAYO", "coordenadas": {"latitud": -6.4167, "longitud": -76.3667}},
                    {"id": "220910", "nombre": "MORALES", "coordenadas": {"latitud": -6.5, "longitud": -76.4167}},
                    {"id": "220911", "nombre": "PAPAPLAYA", "coordenadas": {"latitud": -6.5833, "longitud": -76.4167}},
                    {"id": "220912", "nombre": "SAN ANTONIO", "coordenadas": {"latitud": -6.4167, "longitud": -76.4167}},
                    {"id": "220913", "nombre": "SAUCE", "coordenadas": {"latitud": -6.5, "longitud": -76.3333}},
                    {"id": "220914", "nombre": "SHAPAJA", "coordenadas": {"latitud": -6.5833, "longitud": -76.3333}}
                ]
            },
            {
                "id": "2210",
                "nombre": "TOCACHE",
                "coordenadas": {"latitud": -8.1833, "longitud": -76.5167},
                "distritos": [
                    {"id": "221001", "nombre": "TOCACHE", "coordenadas": {"latitud": -8.1833, "longitud": -76.5167}},
                    {"id": "221002", "nombre": "NUEVO PROGRESO", "coordenadas": {"latitud": -8.25, "longitud": -76.5833}},
                    {"id": "221003", "nombre": "POLVORA", "coordenadas": {"latitud": -8.1167, "longitud": -76.5833}},
                    {"id": "221004", "nombre": "SHUNTE", "coordenadas": {"latitud": -8.25, "longitud": -76.45}},
                    {"id": "221005", "nombre": "UCHIZA", "coordenadas": {"latitud": -8.1167, "longitud": -76.45}}
                ]
            }
        ]
    },
    "23": {  # TACNA
        "id": "23",
        "nombre": "TACNA",
        "coordenadas": {
            "latitud": -18.0067,
            "longitud": -70.2467
        },
        "provincias": [
            {
                "id": "2301",
                "nombre": "TACNA",
                "coordenadas": {
                    "latitud": -18.0067,
                    "longitud": -70.2467
                },
                "distritos": [
                    {"id": "230101", "nombre": "TACNA", "coordenadas": {"latitud": -18.0067, "longitud": -70.2467}},
                    {"id": "230102", "nombre": "ALTO DE LA ALIANZA", "coordenadas": {"latitud": -18.0167, "longitud": -70.2667}},
                    {"id": "230103", "nombre": "CALANA", "coordenadas": {"latitud": -18.0167, "longitud": -70.1833}},
                    {"id": "230104", "nombre": "CIUDAD NUEVA", "coordenadas": {"latitud": -18.0167, "longitud": -70.2333}},
                    {"id": "230105", "nombre": "INCLAN", "coordenadas": {"latitud": -18.0167, "longitud": -70.2167}},
                    {"id": "230106", "nombre": "PACHIA", "coordenadas": {"latitud": -18.0167, "longitud": -70.2000}},
                    {"id": "230107", "nombre": "PALCA", "coordenadas": {"latitud": -18.0167, "longitud": -70.2500}},
                    {"id": "230108", "nombre": "POCOLLAY", "coordenadas": {"latitud": -18.0167, "longitud": -70.2333}},
                    {"id": "230109", "nombre": "SAMA", "coordenadas": {"latitud": -18.0167, "longitud": -70.2667}},
                    {"id": "230110", "nombre": "CORONEL GREGORIO ALBARRACIN LANCHIPA", "coordenadas": {"latitud": -18.0167, "longitud": -70.2333}}
                ]
            },
            {
                "id": "2302",
                "nombre": "CANDARAVE",
                "coordenadas": {
                    "latitud": -17.2667,
                    "longitud": -70.2500
                },
                "distritos": [
                    {"id": "230201", "nombre": "CANDARAVE", "coordenadas": {"latitud": -17.2667, "longitud": -70.2500}},
                    {"id": "230202", "nombre": "CAIRANI", "coordenadas": {"latitud": -17.2667, "longitud": -70.2333}},
                    {"id": "230203", "nombre": "CURIBAYA", "coordenadas": {"latitud": -17.2667, "longitud": -70.2667}},
                    {"id": "230204", "nombre": "HUANUARA", "coordenadas": {"latitud": -17.2667, "longitud": -70.2167}},
                    {"id": "230205", "nombre": "QUILAHUANI", "coordenadas": {"latitud": -17.2667, "longitud": -70.2833}}
                ]
            },
            {
                "id": "2303",
                "nombre": "JORGE BASADRE",
                "coordenadas": {
                    "latitud": -17.3333,
                    "longitud": -70.5000
                },
                "distritos": [
                    {"id": "230301", "nombre": "LOCUMBA", "coordenadas": {"latitud": -17.3333, "longitud": -70.5000}},
                    {"id": "230302", "nombre": "ILABAYA", "coordenadas": {"latitud": -17.3333, "longitud": -70.4667}},
                    {"id": "230303", "nombre": "ITE", "coordenadas": {"latitud": -17.3333, "longitud": -70.5333}}
                ]
            },
            {
                "id": "2304",
                "nombre": "TARATA",
                "coordenadas": {
                    "latitud": -17.4833,
                    "longitud": -70.0333
                },
                "distritos": [
                    {"id": "230401", "nombre": "TARATA", "coordenadas": {"latitud": -17.4833, "longitud": -70.0333}},
                    {"id": "230402", "nombre": "HEROES ALBARRACIN", "coordenadas": {"latitud": -17.4833, "longitud": -70.0500}},
                    {"id": "230403", "nombre": "ESTIQUE", "coordenadas": {"latitud": -17.4833, "longitud": -70.0167}},
                    {"id": "230404", "nombre": "ESTIQUE-PAMPA", "coordenadas": {"latitud": -17.4833, "longitud": -70.0000}},
                    {"id": "230405", "nombre": "SITAJARA", "coordenadas": {"latitud": -17.4833, "longitud": -70.0667}},
                    {"id": "230406", "nombre": "SUSAPAYA", "coordenadas": {"latitud": -17.4833, "longitud": -70.0833}},
                    {"id": "230407", "nombre": "TARUCACHI", "coordenadas": {"latitud": -17.4833, "longitud": -70.1000}},
                    {"id": "230408", "nombre": "TICACO", "coordenadas": {"latitud": -17.4833, "longitud": -70.1167}}
                ]
            }
        ]
    },
    "24": {  # TUMBES
        "id": "24",
        "nombre": "TUMBES",
        "coordenadas": {
            "latitud": -3.5667,
            "longitud": -80.4500
        },
        "provincias": [
            {
                "id": "2401",
                "nombre": "TUMBES",
                "coordenadas": {
                    "latitud": -3.5667,
                    "longitud": -80.4500
                },
                "distritos": [
                    {"id": "240101", "nombre": "TUMBES", "coordenadas": {"latitud": -3.5667, "longitud": -80.4500}},
                    {"id": "240102", "nombre": "CORRALES", "coordenadas": {"latitud": -3.5667, "longitud": -80.4333}},
                    {"id": "240103", "nombre": "LA CRUZ", "coordenadas": {"latitud": -3.5667, "longitud": -80.4667}},
                    {"id": "240104", "nombre": "PAMPAS DE HOSPITAL", "coordenadas": {"latitud": -3.5667, "longitud": -80.4833}},
                    {"id": "240105", "nombre": "SAN JACINTO", "coordenadas": {"latitud": -3.5667, "longitud": -80.5000}},
                    {"id": "240106", "nombre": "SAN JUAN DE LA VIRGEN", "coordenadas": {"latitud": -3.5667, "longitud": -80.5167}}
                ]
            },
            {
                "id": "2402",
                "nombre": "CONTRALMIRANTE VILLAR",
                "coordenadas": {
                    "latitud": -3.6833,
                    "longitud": -80.1833
                },
                "distritos": [
                    {"id": "240201", "nombre": "ZORRITOS", "coordenadas": {"latitud": -3.6833, "longitud": -80.1833}},
                    {"id": "240202", "nombre": "CASITAS", "coordenadas": {"latitud": -3.6833, "longitud": -80.2000}},
                    {"id": "240203", "nombre": "CANOAS DE PUNTA SAL", "coordenadas": {"latitud": -3.6833, "longitud": -80.1667}}
                ]
            },
            {
                "id": "2403",
                "nombre": "ZARUMILLA",
                "coordenadas": {
                    "latitud": -3.5000,
                    "longitud": -80.2500
                },
                "distritos": [
                    {"id": "240301", "nombre": "ZARUMILLA", "coordenadas": {"latitud": -3.5000, "longitud": -80.2500}},
                    {"id": "240302", "nombre": "AGUAS VERDES", "coordenadas": {"latitud": -3.5000, "longitud": -80.2667}},
                    {"id": "240303", "nombre": "MATAPALO", "coordenadas": {"latitud": -3.5000, "longitud": -80.2333}},
                    {"id": "240304", "nombre": "PAPAYAL", "coordenadas": {"latitud": -3.5000, "longitud": -80.2167}}
                ]
            }
        ]
    }
}

# Datos de los departamentos faltantes
departamentos_faltantes = [
    {
        "id": "25",
        "nombre": "UCAYALI",
        "coordenadas": {
            "latitud": -8.3833,
            "longitud": -74.5500
        },
        "provincias": [
            {
                "id": "2501",
                "nombre": "CORONEL PORTILLO",
                "coordenadas": {
                    "latitud": -8.3833,
                    "longitud": -74.5500
                },
                "distritos": [
                    {"id": "250101", "nombre": "CALLERIA", "coordenadas": {"latitud": -8.3833, "longitud": -74.5500}},
                    {"id": "250102", "nombre": "CAMPOVERDE", "coordenadas": {"latitud": -8.3833, "longitud": -74.5333}},
                    {"id": "250103", "nombre": "IPARIA", "coordenadas": {"latitud": -8.3833, "longitud": -74.5667}},
                    {"id": "250104", "nombre": "MASISEA", "coordenadas": {"latitud": -8.3833, "longitud": -74.5833}},
                    {"id": "250105", "nombre": "YARINACOCHA", "coordenadas": {"latitud": -8.3833, "longitud": -74.6000}},
                    {"id": "250106", "nombre": "NUEVA REQUENA", "coordenadas": {"latitud": -8.3833, "longitud": -74.6167}},
                    {"id": "250107", "nombre": "MANANTAY", "coordenadas": {"latitud": -8.3833, "longitud": -74.6333}}
                ]
            },
            {
                "id": "2502",
                "nombre": "ATALAYA",
                "coordenadas": {
                    "latitud": -10.7333,
                    "longitud": -73.7667
                },
                "distritos": [
                    {"id": "250201", "nombre": "RAYMONDI", "coordenadas": {"latitud": -10.7333, "longitud": -73.7667}},
                    {"id": "250202", "nombre": "SEPAHUA", "coordenadas": {"latitud": -10.7333, "longitud": -73.7833}},
                    {"id": "250203", "nombre": "TAHUANIA", "coordenadas": {"latitud": -10.7333, "longitud": -73.7500}},
                    {"id": "250204", "nombre": "YURUA", "coordenadas": {"latitud": -10.7333, "longitud": -73.7333}}
                ]
            },
            {
                "id": "2503",
                "nombre": "PADRE ABAD",
                "coordenadas": {
                    "latitud": -8.6167,
                    "longitud": -75.2333
                },
                "distritos": [
                    {"id": "250301", "nombre": "PADRE ABAD", "coordenadas": {"latitud": -8.6167, "longitud": -75.2333}},
                    {"id": "250302", "nombre": "IRAZOLA", "coordenadas": {"latitud": -8.6167, "longitud": -75.2500}},
                    {"id": "250303", "nombre": "CURIMANA", "coordenadas": {"latitud": -8.6167, "longitud": -75.2167}}
                ]
            },
            {
                "id": "2504",
                "nombre": "PURUS",
                "coordenadas": {
                    "latitud": -9.5000,
                    "longitud": -70.5000
                },
                "distritos": [
                    {"id": "250401", "nombre": "PURUS", "coordenadas": {"latitud": -9.5000, "longitud": -70.5000}}
                ]
            }
        ]
    }
]

# Leer el archivo JSON actual
with open('ubigeo_peru.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Actualizar o agregar los departamentos faltantes
for dept in departamentos_faltantes:
    # Buscar si el departamento ya existe
    dept_exists = False
    for i, existing_dept in enumerate(data['departamentos']):
        if existing_dept['id'] == dept['id']:
            data['departamentos'][i] = dept
            dept_exists = True
            break
    
    # Si no existe, agregarlo
    if not dept_exists:
        data['departamentos'].append(dept)

# Ordenar los departamentos alfabéticamente por nombre
data['departamentos'].sort(key=lambda x: x['nombre'])

# Guardar el archivo actualizado
with open('ubigeo_peru.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("✓ Departamentos actualizados y ordenados alfabéticamente en el archivo ubigeo_peru.json")