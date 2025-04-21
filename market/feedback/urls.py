from django.urls import path
from . import views

app_name = 'feedback'

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    # path('add/', views.add_review, name='add_review'),
    # path('reviews/', views.reviews, name='reviews'),
]
