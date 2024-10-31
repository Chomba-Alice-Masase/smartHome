from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('doorbell/', views.doorbell_notification, name='doorbell_notification'),
    path('door-status/', views.door_status_view, name='door_status_view'),
    path('light-control/', views.light_control_view, name='light_control'),
    # path('motion-sensor/', views.motion_sensor_view, name='motion_sensor'),
    path('sensor-data/', views.sensor_data_view, name='sensor-data'),
]
