from rest_framework import generics
from .models import DataPoint
from .serializers import DataPointSerializer
# from django_filters import rest_framework as filters

class DataPointListCreate(generics.ListCreateAPIView):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer
    # filter_backends = [filters.DjangoFilterBackend]
    # filterset_fields = ['end_year', 'topic', 'sector', 'region', 'pestle', 'source', 'country', 'city']

from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/index.html')


# from rest_framework import generics
# from .models import DataPoint
# from .serializers import DataPointSerializer
# from django_filters.rest_framework import DjangoFilterBackend

# class DataPointListCreate(generics.ListCreateAPIView):
#     queryset = DataPoint.objects.all()
#     serializer_class = DataPointSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['end_year', 'topic', 'sector', 'region', 'pestle', 'source', 'country', 'city']
