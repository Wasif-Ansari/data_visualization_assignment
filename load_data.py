import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datavisualization.settings')
django.setup()

from dashboard.models import DataPoint

with open('jsondata.json', encoding="utf-8") as file:
    data = json.load(file)
    for entry in data:
        # Handle empty strings for integer fields
        intensity = int(entry['intensity']) if entry['intensity'] else 0
        relevance = int(entry['relevance']) if entry['relevance'] else 0
        likelihood = int(entry['likelihood']) if entry['likelihood'] else 0

        DataPoint.objects.create(
            end_year=entry.get('end_year', ''),
            intensity=intensity,
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
            relevance=relevance,
            pestle=entry['pestle'],
            source=entry['source'],
            title=entry['title'],
            likelihood=likelihood
        )
