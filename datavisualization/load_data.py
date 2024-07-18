import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datavisualization.settings')
django.setup()

from dashboard.models import DataPoint

with open('path/to/jsondata.json') as file:
    data = json.load(file)
    for entry in data:
        DataPoint.objects.create(
            end_year=entry.get('end_year', ''),
            intensity=entry['intensity'],
            sector=entry.get('sector', ''),
            topic=entry['topic'],
            insight=entry['insight'],
            url=entry['url'],
            region=entry['region'],
            start_year=entry.get('start_year', ''),
            impact=entry.get('impact', ''),
            added=entry['added'],
            published=entry['published'],
            country=entry.get('country', ''),
            relevance=entry['relevance'],
            pestle=entry['pestle'],
            source=entry['source'],
            title=entry['title'],
            likelihood=entry['likelihood']
        )
