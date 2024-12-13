from django.urls import path
from .views import visualization_data

urlpatterns = [
    path('<str:topic_name>/', visualization_data, name='visualization_data'),
]
