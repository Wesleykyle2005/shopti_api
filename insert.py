import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopti_api.settings')
import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopti_api.settings')
django.setup()

from users.models import Department, Municipality

with open('datos.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for entry in data.get('department', []):
    dept_name = entry.get('name')
    municipalities = entry.get('municipalities', [])
    if not dept_name:
        continue

    dept, created = Department.objects.get_or_create(name=dept_name)
    print(f"Department: {dept_name} - {'Created' if created else 'Already exists'}")

    for mun_name in municipalities:
        mun, mun_created = Municipality.objects.get_or_create(name=mun_name, department=dept)
        print(f"  Municipality: {mun_name} - {'Created' if mun_created else 'Already exists'}")
print("Inserted")
