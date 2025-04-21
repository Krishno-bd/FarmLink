from django.urls import path
from . import views

urlpatterns = [
    path('calculator/', views.fertilizer_calculator, name='fertilizer_calculator'),

]
