from django.urls import path
from .views import DataPointListCreate, index

urlpatterns = [
    path('data/', DataPointListCreate.as_view(), name='data-list-create'),
    path('', index, name='index'),
]


# from django.urls import path
# from .views import DataPointListCreate, index

# urlpatterns = [
#     path('data/', DataPointListCreate.as_view(), name='data-list-create'),
#     path('', index, name='index'),
# ]
