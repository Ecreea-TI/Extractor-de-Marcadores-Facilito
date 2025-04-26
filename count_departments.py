import json

with open('ubigeo_peru_updated.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

departments = data['departamentos']
print(f"Total de departamentos: {len(departments)}")
print("\nLista de departamentos:")
for dept in departments:
    print(f"- {dept['nombre']} (ID: {dept['id']})") 