from django.urls import path
from . import views

app_name = 'consultation'

urlpatterns = [
    path('request/', views.consultation_request_view, name='consultation_request'),
    path('success/', views.consultation_success_view, name='success'),
]
