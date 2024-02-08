from django.urls import path
from . import views

    # TODO: зарегистрируйте необходимые маршруты
urlpatterns = [
    path('sensors/', views.SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', views.SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', views.TemperatureMeasurementCreateView.as_view(), name='measurement-create'),
]



